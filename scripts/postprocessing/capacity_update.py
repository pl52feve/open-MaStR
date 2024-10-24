from sshtunnel import SSHTunnelForwarder
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os

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

def get_engine():
    server = SSHTunnelForwarder(
        ssh_address_or_host=(SSH_ADDRESS, SSH_PORT),
        ssh_pkey=PATH_PKEY_SSH,
        ssh_username=SSH_USERNAME,
        ssh_password=SSH_PASSPHRASE,
        remote_bind_address=(LOCAL_HOST, LOCAL_PORT),
    )
    server.start()
    local_port = str(server.local_bind_port)

    engine = create_engine(
        f"postgresql://{USERNAME_POSTGRES}:{PASSWORD_POSTGRES}@{LOCAL_HOST}:"
        f"{local_port}/{POSTGRES_DB}",
        echo=True,
        connect_args={"options": f"-c search_path={FACT_SCHEMA}"},
        execution_options={"schema_translate_map": {None: FACT_SCHEMA}},
    )
    return engine

# Function to read and replace the placeholder in the SQL query
def read_and_replace_query(filepath, replacement):
    with open(filepath, 'r') as file:
        query = file.read()
    # Replace all occurrences of the placeholder with the actual value
    query = query.replace('{{gen_type}}', replacement)
    return query

def update_capacities():
    for gen_type in ['solar', 'wind']:
        sql_query = read_and_replace_query(os.path.join(os.getcwd(),
                                                        "scripts", "postprocessing",
                                                        "queries",'capacity_ratios.sql'),
                                                        gen_type)

        with get_engine().begin() as connection:
            connection.execute(text(sql_query))