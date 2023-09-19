from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Sequence,
    DateTime,
    Boolean,
    func,
    Date,
    JSON,
)

meta = MetaData()
Base = declarative_base(metadata=meta)


class Extended(object):
    NetzbetreiberMastrNummer = Column(String)
    Registrierungsdatum = Column(Date)
    EinheitMastrNummer = Column(String, primary_key=True)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    LokationMastrNummer = Column(String)
    NetzbetreiberpruefungStatus = Column(String)
    NetzbetreiberpruefungDatum = Column(Date)
    AnlagenbetreiberMastrNummer = Column(String)
    Land = Column(String)
    Bundesland = Column(String)
    Landkreis = Column(String)
    Gemeinde = Column(String)
    Gemeindeschluessel = Column(String)
    Postleitzahl = Column(String)
    Gemarkung = Column(String)
    FlurFlurstuecknummern = Column(String)
    Strasse = Column(String)
    StrasseNichtGefunden = Column(Boolean)
    Hausnummer = Column(String)
    HausnummerNichtGefunden = Column(Boolean)
    Adresszusatz = Column(String)
    Ort = Column(String)
    Laengengrad = Column(Float)
    Breitengrad = Column(Float)
    UtmZonenwert = Column(String)
    UtmEast = Column(Float)
    UtmNorth = Column(Float)
    GaussKruegerHoch = Column(Float)
    GaussKruegerRechts = Column(Float)
    Meldedatum = Column(Date)
    GeplantesInbetriebnahmedatum = Column(Date)
    Inbetriebnahmedatum = Column(Date)
    DatumEndgueltigeStilllegung = Column(Date)
    DatumBeginnVoruebergehendeStilllegung = Column(Date)
    DatumBeendigungVorlaeufigenStilllegung = Column(Date)
    DatumWiederaufnahmeBetrieb = Column(Date)
    EinheitSystemstatus = Column(String)
    EinheitBetriebsstatus = Column(String)
    BestandsanlageMastrNummer = Column(String)
    NichtVorhandenInMigriertenEinheiten = Column(Boolean)
    AltAnlagenbetreiberMastrNummer = Column(String)
    DatumDesBetreiberwechsels = Column(Date)
    DatumRegistrierungDesBetreiberwechsels = Column(Date)
    NameStromerzeugungseinheit = Column(String)
    Weic = Column(String)
    WeicDisplayName = Column(String)
    Kraftwerksnummer = Column(String)
    Energietraeger = Column(String)
    Bruttoleistung = Column(Float)
    Nettonennleistung = Column(Float)
    AnschlussAnHoechstOderHochSpannung = Column(Boolean)
    Schwarzstartfaehigkeit = Column(Boolean)
    Inselbetriebsfaehigkeit = Column(Boolean)
    Einsatzverantwortlicher = Column(String)
    FernsteuerbarkeitNb = Column(Boolean)
    FernsteuerbarkeitDv = Column(Boolean)
    FernsteuerbarkeitDr = Column(Boolean)
    Einspeisungsart = Column(String)
    PraequalifiziertFuerRegelenergie = Column(Boolean)
    GenMastrNummer = Column(String)
    Netzbetreiberzuordnungen = Column(String)
    # from bulk download
    Hausnummer_nv = Column(Boolean)
    Weic_nv = Column(Boolean)
    Kraftwerksnummer_nv = Column(Boolean)


class WindExtended(Extended, Base):
    __tablename__ = "wind_extended"

    # wind specific attributes
    NameWindpark = Column(String)
    Lage = Column(String)
    Seelage = Column(String)
    ClusterOstsee = Column(String)
    ClusterNordsee = Column(String)
    Hersteller = Column(String)
    HerstellerId = Column(String)
    Technologie = Column(String)
    Typenbezeichnung = Column(String)
    Nabenhoehe = Column(Float)
    Rotordurchmesser = Column(Float)
    Rotorblattenteisungssystem = Column(Boolean)
    AuflageAbschaltungLeistungsbegrenzung = Column(Boolean)
    AuflagenAbschaltungSchallimmissionsschutzNachts = Column(Boolean)
    AuflagenAbschaltungSchallimmissionsschutzTagsueber = Column(Boolean)
    AuflagenAbschaltungSchattenwurf = Column(Boolean)
    AuflagenAbschaltungTierschutz = Column(Boolean)
    AuflagenAbschaltungEiswurf = Column(Boolean)
    AuflagenAbschaltungSonstige = Column(Boolean)
    Wassertiefe = Column(Float)
    Kuestenentfernung = Column(Float)
    Buergerenergie = Column(Boolean)
    Nachtkennzeichen = Column(Boolean)
    EegMastrNummer = Column(String)


class SolarExtended(Extended, Base):
    __tablename__ = "solar_extended"

    ZugeordneteWirkleistungWechselrichter = Column(Float)
    GemeinsamerWechselrichterMitSpeicher = Column(String)
    AnzahlModule = Column(Integer)
    Lage = Column(String)
    Leistungsbegrenzung = Column(String)
    EinheitlicheAusrichtungUndNeigungswinkel = Column(Boolean)
    Hauptausrichtung = Column(String)
    HauptausrichtungNeigungswinkel = Column(String)
    Nebenausrichtung = Column(String)
    NebenausrichtungNeigungswinkel = Column(String)
    InAnspruchGenommeneFlaeche = Column(Float)
    ArtDerFlaeche = Column(String)
    InAnspruchGenommeneAckerflaeche = Column(Float)
    Nutzungsbereich = Column(String)
    Buergerenergie = Column(Boolean)
    EegMastrNummer = Column(String)
    ArtDerFlaecheIds = Column(String)


class BiomassExtended(Extended, Base):
    __tablename__ = "biomass_extended"

    Hauptbrennstoff = Column(String)
    Biomasseart = Column(String)
    Technologie = Column(String)
    EegMastrNummer = Column(String)
    KwkMastrNummer = Column(String)


class HydroExtended(Extended, Base):
    __tablename__ = "hydro_extended"

    NameKraftwerk = Column(String)
    ArtDerWasserkraftanlage = Column(String)
    AnzeigeEinerStilllegung = Column(Boolean)
    ArtDerStilllegung = Column(String)
    DatumBeginnVorlaeufigenOderEndgueltigenStilllegung = Column(Date)
    MinderungStromerzeugung = Column(Boolean)
    BestandteilGrenzkraftwerk = Column(Boolean)
    NettonennleistungDeutschland = Column(Float)
    ArtDesZuflusses = Column(String)
    EegMastrNummer = Column(String)


class Eeg(object):
    Registrierungsdatum = Column(Date)
    EegMastrNummer = Column(String, primary_key=True)
    Meldedatum = Column(Date)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    EegInbetriebnahmedatum = Column(Date)
    VerknuepfteEinheit = Column(String)
    AnlagenschluesselEeg = Column(String)
    AusschreibungZuschlag = Column(Boolean)
    AnlagenkennzifferAnlagenregister = Column(String)
    AnlagenkennzifferAnlagenregister_nv = Column(Boolean)
    Netzbetreiberzuordnungen = Column(String)


class WindEeg(Eeg, Base):
    __tablename__ = "wind_eeg"

    PrototypAnlage = Column(Boolean)
    PilotAnlage = Column(Boolean)
    InstallierteLeistung = Column(Float)
    VerhaeltnisErtragsschaetzungReferenzertrag = Column(Float)
    VerhaeltnisReferenzertragErtrag5Jahre = Column(Float)
    VerhaeltnisReferenzertragErtrag10Jahre = Column(Float)
    VerhaeltnisReferenzertragErtrag15Jahre = Column(Float)
    Zuschlagsnummer = Column(String)
    AnlageBetriebsstatus = Column(String)
    VerhaeltnisErtragsschaetzungReferenzertrag_nv = Column(Boolean)
    VerhaeltnisReferenzertragErtrag5Jahre_nv = Column(Boolean)
    VerhaeltnisReferenzertragErtrag10Jahre_nv = Column(Boolean)
    VerhaeltnisReferenzertragErtrag15Jahre_nv = Column(Boolean)


class SolarEeg(Eeg, Base):
    __tablename__ = "solar_eeg"

    InanspruchnahmeZahlungNachEeg = Column(Boolean)
    InstallierteLeistung = Column(Float)
    RegistrierungsnummerPvMeldeportal = Column(String)
    MieterstromRegistrierungsdatum = Column(Date)
    MieterstromZugeordnet = Column(Boolean)
    MieterstromMeldedatum = Column(Date)
    MieterstromErsteZuordnungZuschlag = Column(Date)
    ZugeordneteGebotsmenge = Column(Float)
    Zuschlagsnummer = Column(String)
    AnlageBetriebsstatus = Column(String)
    RegistrierungsnummerPvMeldeportal_nv = Column(Boolean)


class BiomassEeg(Eeg, Base):
    __tablename__ = "biomass_eeg"

    InstallierteLeistung = Column(Float)
    AusschliesslicheVerwendungBiomasse = Column(Boolean)
    Zuschlagsnummer = Column(String)
    BiogasInanspruchnahmeFlexiPraemie = Column(Boolean)
    BiogasDatumInanspruchnahmeFlexiPraemie = Column(Date)
    BiogasLeistungserhoehung = Column(Boolean)
    BiogasDatumLeistungserhoehung = Column(Date)
    BiogasUmfangLeistungserhoehung = Column(Float)
    BiogasGaserzeugungskapazitaet = Column(Float)
    Hoechstbemessungsleistung = Column(Float)
    BiomethanErstmaligerEinsatz = Column(Date)
    AnlageBetriebsstatus = Column(String)
    BiogasGaserzeugungskapazitaet_nv = Column(Boolean)
    BiomethanErstmaligerEinsatz_nv = Column(Boolean)


class HydroEeg(Eeg, Base):
    __tablename__ = "hydro_eeg"

    InstallierteLeistung = Column(Float)
    AnlageBetriebsstatus = Column(String)
    Ertuechtigung = Column(JSON)
    ErtuechtigungIds = Column(String)


tablename_mapping = {
    "anlageneegbiomasse": {
        "__name__": BiomassEeg.__tablename__,
        "__class__": BiomassEeg,
        "replace_column_names": {
            "EegMaStRNummer": "EegMastrNummer",
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit",
            "BiogasHoechstbemessungsleistung": "Hoechstbemessungsleistung",
        },
    },
    "einheitenbiomasse": {
        "__name__": BiomassExtended.__tablename__,
        "__class__": BiomassExtended,
        "replace_column_names": {
            "EegMaStRNummer": "EegMastrNummer",
            "KwkMaStRNummer": "KwkMastrNummer",
            "LokationMaStRNummer": "LokationMastrNummer",
        },
    },
    "anlageneegsolar": {
        "__name__": SolarEeg.__tablename__,
        "__class__": SolarEeg,
        "replace_column_names": {
            "EegMaStRNummer": "EegMastrNummer",
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit",
        },
    },
    "einheitensolar": {
        "__name__": SolarExtended.__tablename__,
        "__class__": SolarExtended,
        "replace_column_names": {
            "EegMaStRNummer": "EegMastrNummer",
            "LokationMaStRNummer": "LokationMastrNummer",
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit",
        },
    },
    "anlageneegwasser": {
        "__name__": HydroEeg.__tablename__,
        "__class__": HydroEeg,
        "replace_column_names": {
            "EegMaStRNummer": "EegMastrNummer",
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit",
        },
    },
    "einheitenwasser": {
        "__name__": HydroExtended.__tablename__,
        "__class__": HydroExtended,
        "replace_column_names": {
            "EegMaStRNummer": "EegMastrNummer",
            "LokationMaStRNummer": "LokationMastrNummer",
        },
    },
    "anlageneegwind": {
        "__name__": WindEeg.__tablename__,
        "__class__": WindEeg,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit",
            "EegMaStRNummer": "EegMastrNummer",
        },
    },
    "einheitenwind": {
        "__name__": WindExtended.__tablename__,
        "__class__": WindExtended,
        "replace_column_names": {
            "LokationMaStRNummer": "LokationMastrNummer",
            "EegMaStRNummer": "EegMastrNummer",
            "Nachtkennzeichnung": "Nachtkennzeichen",
        },
    },
    "katalogkategorien": {
        "__name__": "katalogkategorien",
        "__class__": None,
        "replace_column_names": None,
    },
    "katalogwerte": {
        "__name__": "katalogwerte",
        "__class__": None,
        "replace_column_names": None,
    },
    "einheitentypen": {
        "__name__": "einheitentypen",
        "__class__": None,
        "replace_column_names": None,
    },
}
