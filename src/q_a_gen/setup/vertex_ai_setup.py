import sys
sys.path.append("../../../../")
from typing import Optional
from dotenv import load_dotenv
from google.oauth2 import service_account
import vertexai
import os

load_dotenv()
VERTEXAI_PROJECT = os.environ["VERTEXAI_PROJECT"]
CREDENTIALS_FILEPATH = os.getcwd() + '/../../../config/application_default_credentials.json'


def initialize_vertexai_params(location: Optional[str] = "us-central1"):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_FILEPATH

    service_account.Credentials.from_service_account_file(
        filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    vertexai.init(project=VERTEXAI_PROJECT, location=location)
