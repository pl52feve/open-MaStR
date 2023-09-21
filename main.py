#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
open-MaStR - Main file

Bulk: Download XML-Dump and fill in local SQLite database.
API: Download latest entries using the SOAP-API.

SPDX-License-Identifier: AGPL-3.0-or-later
"""

from open_mastr import Mastr
from sqlalchemy import create_engine, text
from sshtunnel import SSHTunnelForwarder
from dotenv import load_dotenv
import os

## specify download parameter

# bulk download
bulk_date = "today"
bulk_cleansing = True
data_bulk = [
    "biomass",
    "combustion",
    "gsgk",
    "hydro",
    "nuclear",
    "solar",
    "storage",
    "wind",
    "balancing_area",
    "electricity_consumer",
    "gas",
    "grid",
    "location",
    "market",
    "permit",
]

# API download
# for parameter explanation see: https://open-mastr.readthedocs.io/en/latest/getting_started.html#api-download

api_date = "latest"
api_chunksize = 10
api_limit = 10
api_processes = None

data_api = [
    "biomass",
    "combustion",
    "gsgk",
    "hydro",
    "nuclear",
    "solar",
    "storage",
    "wind",
]

api_data_types = ["unit_data", "eeg_data", "kwk_data", "permit_data"]

api_location_types = [
    "location_elec_generation",
    "location_elec_consumption",
    "location_gas_generation",
    "location_gas_consumption",
]


def mastr_temp_update():
    """Update the temporary MaStR version."""
    load_dotenv()

    SSH_ADDRESS = os.getenv("SSH_HOST")
    SSH_PORT = int(os.getenv("SSH_PORT"))
    PATH_PKEY_SSH = os.getenv("PATH_PKEY_SSH")
    SSH_USERNAME = os.getenv("SSH_USERNAME")
    SSH_PASSPHRASE = os.getenv("SSH_PASSPHRASE")
    LOCAL_HOST = os.getenv("LOCAL_HOST")
    LOCAL_PORT = int(os.getenv("LOCAL_PORT"))
    USERNAME_POSTGRES = os.getenv("USERNAME_POSTGRES")
    PASSWORD_POSTGRES = os.getenv("PASSWORD_POSTGRES")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    FACT_SCHEMA = os.getenv("FACT_SCHEMA")

    server = SSHTunnelForwarder(
        ssh_address_or_host=(SSH_ADDRESS, SSH_PORT),
        ssh_pkey=PATH_PKEY_SSH,
        ssh_username=SSH_USERNAME,
        ssh_password=SSH_PASSPHRASE,
        remote_bind_address=(LOCAL_HOST, LOCAL_PORT),
    )
    server.start()
    LOCAL_PORT = str(server.local_bind_port)

    engine = create_engine(
        f"postgresql://{USERNAME_POSTGRES}:{PASSWORD_POSTGRES}@{LOCAL_HOST}:"
        f"{LOCAL_PORT}/{POSTGRES_DB}",
        echo=True,
        execution_options={"schema_translate_map": {None: FACT_SCHEMA}},
    )

    db = Mastr(engine=engine)
    db.download(data=["solar", "wind", "hydro", "biomass"])


if __name__ == "__main__":
    # update MaStR
    mastr_temp_update()
