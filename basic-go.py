import requests
import os
import json
from rich import print

# Environment variables
BASE_URL = os.getenv("BASE_URL", "http://localhost:8007")
LOGIN_URL = f"{BASE_URL}/login"
ALL_SERVICES_URL = f"{BASE_URL}/prod/all/{{attachment_id}}?provider={{provider}}"
SECRET_TOKEN = "pq2_smFS_kQ8wrmP5beIo3mxKpWbHZH8z7klx2uUxxM="

# Login payload and headers
login_payload = json.dumps({"secret_token": SECRET_TOKEN})
login_headers = {
    'Content-Type': 'application/json'
}

# Perform login
response = requests.post(LOGIN_URL, headers=login_headers, data=login_payload)
response.raise_for_status()
bearer_token_json = response.json()
token = bearer_token_json['accessToken']

# Fetch image data
atacchment_id = "50072560"
provider = "ehg"
url = ALL_SERVICES_URL.format(attachment_id=atacchment_id, provider=provider.lower())
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("Successfully fetched image data")
    print(response.json())
else:
    print(f"Failed to fetch image data, status code: {response.status_code}")
    print(response.text)