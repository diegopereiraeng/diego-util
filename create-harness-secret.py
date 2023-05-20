import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

def create_secret( name, value, identifier, tags, description):

    api_key = os.getenv("API_KEY")
    account_identifier = os.getenv("ACCOUNT_IDENTIFIER")
    org_identifier = os.getenv("ORG_IDENTIFIER")
    project_identifier = os.getenv("PROJECT_IDENTIFIER")

    url = "https://app.harness.io/gateway/ng/api/v2/secrets?accountIdentifier="+account_identifier+"&orgIdentifier="+org_identifier+"&projectIdentifier="+project_identifier+"&privateSecret=false"

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }

    payload = {
        "secret": {
            "type": "SecretText",
            "name": name,
            "identifier": identifier,
            "orgIdentifier": org_identifier,
            "projectIdentifier": project_identifier,
            "tags": tags,
            "description": description,
            "spec": {
                "errorMessageForInvalidYaml": "Invalid Yaml",
                "type": "SecretTextSpec",
                "secretManagerIdentifier": "harnessSecretManager",
                "valueType": "Inline",
                "value": value
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    print(data)

# Usage
name = os.getenv("SECRET_NAME", "change-it")
value = os.getenv("SECRET_VALUE","change-it")
identifier = os.getenv("SECRET_NAME", "change_it").replace("-","_").replace(" ","_")
tags = os.getenv("SECRET_TAGS", '{"property1": "value1", "property2": "value2"}')
description = os.getenv("SECRET_DESCRIPTION", "Change it")

create_secret( name, value, identifier, tags, description)