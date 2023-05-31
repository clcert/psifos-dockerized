import os

from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

ADMIN_USER = os.environ.get("ADMIN_USER")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

NAME_ELECTION = os.environ.get("NAME_ELECTION")

INFO_URL = os.environ.get("INFO_URL")
OPERATIVE_URL = os.environ.get("OPERATIVE_URL")
URL_ADMIN = os.environ.get("URL_ADMIN")

TRUSTEE_NAME = os.environ.get("TRUSTEE_NAME")
TRUSTEE_PASSWORD = os.environ.get("TRUSTEE_PASSWORD")
TRUSTEE_EMAIL = os.environ.get("TRUSTEE_EMAIL")

VOTER_NAME = os.environ.get("VOTER_NAME")
VOTER_PASSWORD = os.environ.get("VOTER_PASSWORD")

DIRECTORY_PATH = os.environ.get("DIRECTORY_PATH")
VOTERS_FILE_NAME = os.environ.get("VOTERS_FILE_NAME")

TIMEOUT = os.environ.get("TIMEOUT")
LOGIN_SITE = os.environ.get("LOGIN_SITE")
