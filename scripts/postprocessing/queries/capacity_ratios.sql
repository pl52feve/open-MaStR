
TRUNCATE TABLE temp_mastr.{{gen_type}}_capa;
INSERT INTO temp_mastr.{{gen_type}}_capa (date_id, capa)
WITH RECURSIVE date_series AS (
    SELECT
        generate_series('2018-06-01'::date, CURRENT_DATE, '1 day'::interval)::date AS date_id
),
daily_start_grouped AS (
    SELECT
        COALESCE("Inbetriebnahmedatum", "DatumLetzteAktualisierung")::date AS start_date,
        SUM("Bruttoleistung") AS daily_sum
    FROM
        temp_mastr.{{gen_type}}_extended
	 WHERE
        NOT ("Inbetriebnahmedatum" IS NULL AND "DatumEndgueltigeStilllegung" IS NULL)
    GROUP BY
        start_date
    ORDER BY
        start_date
),
cumsum_start_plants AS (
    SELECT
        start_date,
        daily_sum,
        SUM(daily_sum) OVER (ORDER BY start_date) AS start_netto_cumsum
    FROM
        daily_start_grouped
    ORDER BY
        start_date
),
-- Recursive CTE to forward-fill the missing values in netto_cumsum
filled_start_data AS (
    -- Base case: Start with the first date and the corresponding netto_cumsum value
    SELECT
        ds.date_id ,
        cp.start_netto_cumsum
    FROM
        date_series ds
    LEFT JOIN
        cumsum_start_plants cp ON cp.start_date = ds.date_id
    WHERE
        ds.date_id = (SELECT MIN(date_id) FROM date_series)

    UNION ALL

    -- Recursive case: Carry forward the last non-null netto_cumsum value for missing dates
    SELECT
        ds.date_id,
        COALESCE(cp.start_netto_cumsum, fd.start_netto_cumsum) AS start_netto_cumsum
    FROM
        date_series ds
    LEFT JOIN
        cumsum_start_plants cp ON cp.start_date = ds.date_id
    JOIN
        filled_start_data fd ON ds.date_id = fd.date_id + INTERVAL '1 day'
    WHERE
        ds.date_id > (SELECT MIN(date_id) FROM date_series)
),
---------------------------------------------------------------------------------------------------------
daily_end_grouped AS (
    SELECT
        COALESCE("DatumEndgueltigeStilllegung", CURRENT_DATE + INTERVAL '1 day')::date AS end_date,
        SUM("Bruttoleistung") AS daily_sum
    FROM
        temp_mastr.{{gen_type}}_extended
	WHERE
        NOT ("Inbetriebnahmedatum" IS NULL AND "DatumEndgueltigeStilllegung" IS NULL)
    GROUP BY
        end_date
    ORDER BY
        end_date
),
cumsum_end_plants AS (
    SELECT
        end_date,
        daily_sum,
        SUM(daily_sum) OVER (ORDER BY end_date) AS end_netto_cumsum
    FROM
        daily_end_grouped
    ORDER BY
        end_date
),
-- Recursive CTE to forward-fill the missing values in netto_cumsum
filled_end_data AS (
    -- Base case: Start with the first date and the corresponding netto_cumsum value
    SELECT
        ds.date_id ,
        cp.end_netto_cumsum
    FROM
        date_series ds
    LEFT JOIN
        cumsum_end_plants cp ON cp.end_date = ds.date_id
    WHERE
        ds.date_id = (SELECT MIN(date_id) FROM date_series)

    UNION ALL

    -- Recursive case: Carry forward the last non-null netto_cumsum value for missing dates
    SELECT
        ds.date_id,
        COALESCE(cp.end_netto_cumsum, fd.end_netto_cumsum) AS end_netto_cumsum
    FROM
        date_series ds
    LEFT JOIN
        cumsum_end_plants cp ON cp.end_date = ds.date_id
    JOIN
        filled_end_data fd ON ds.date_id = fd.date_id + INTERVAL '1 day'
    WHERE
        ds.date_id > (SELECT MIN(date_id) FROM date_series)
)
SELECT
    fd_start.date_id,
    (fd_start.start_netto_cumsum-fd_end.end_netto_cumsum)::numeric(18,3) AS capa
FROM
    filled_start_data fd_start
FULL OUTER JOIN
    filled_end_data fd_end ON fd_start.date_id = fd_end.date_id
	where fd_start.date_id >= '2019-01-01'::date;
