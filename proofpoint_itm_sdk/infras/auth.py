import requests

from proofpoint_itm_sdk.lib import api


def login(base_url: str, username: str, password: str) -> str:
    result = requests.post(
        f"{base_url}/auth/logins",
        data={"username": username, "password": password},
        verify=False,
    )
    return result.json()["access_token"]


def health(token: str, base_url: str) -> str:
    return api.get(token, f"{base_url}/auth/_health")


def alive(token: str, base_url: str) -> str:
    return api.get(token, f"{base_url}/auth/_alive")


def error(token: str, base_url: str) -> str:
    return api.get(token, f"{base_url}/auth/_error")


def status(token: str, base_url: str) -> str:
    return api.get(token, f"{base_url}/auth/_status")


def clients(token: str, base_url: str) -> str:
    return api.get(token, f"{base_url}/auth/clients")


def authorizations(token: str, base_url: str) -> str:
    return api.get(token, f"{base_url}/auth/authorizations")
