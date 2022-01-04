from proofpoint_itm_sdk.lib import api


def health(token: str, base_url: str) -> str:
    return api.get(token, f"{base_url}/report;realm=observeit/_health")


def types(token: str, base_url: str, details: bool) -> str:
    return api.get(token, f"{base_url}/report;realm=observeit/reports?detail={details}")


def get(token: str, base_url: str, id: str, limit: int = 100) -> str:
    return api.get(
        token,
        f"{base_url}/report;realm=observeit/reports/{id}/stream?limit={limit}&since=0",
    )
