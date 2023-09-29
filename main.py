#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
open-MaStR - Main file

Bulk: Download XML-Dump and fill in local SQLite database.
API: Download latest entries using the SOAP-API.

SPDX-License-Identifier: AGPL-3.0-or-later
"""
import os
from sshtunnel import SSHTunnelForwarder
from dotenv import load_dotenv
from sqlalchemy import create_engine
from open_mastr import Mastr


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
    db.download(data=["solar", "wind", "hydro", "biomass", "permit"])


if __name__ == "__main__":
    # update MaStR
    mastr_temp_update()
