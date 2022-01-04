import urllib3
from urllib3.exceptions import InsecureRequestWarning

import requests

urllib3.disable_warnings(InsecureRequestWarning)

HEADER: dict[str, str] = {
    "content-type": "application/json",
    "cache-control": "no-cache",
}


def get(token: str, url: str):
    HEADER["Authorization"] = f"Bearer {token}"
    result = requests.get(url, headers=HEADER, verify=False)
    return result.json()


def post(token: str, url: str, data: dict[str, any]):
    HEADER["Authorization"] = f"Bearer {token}"
    result = requests.post(url, data, headers=HEADER, verify=False)
    return result.json()
