from proofpoint_itm_sdk.infras import auth
from proofpoint_itm_sdk.infras import report


class Itm(object):
    def __init__(self, console_ip: str, username: str, password: str) -> None:
        self.base_url: str = f"https://{console_ip}/v2/apis"
        self.username: str = username
        self.password: str = password
        self.access_token: str = auth.login(self.base_url, self.username, self.password)

    def test(self):
        return self.access_token

    def check_health(self):
        return auth.health(self.access_token, self.base_url)

    def check_alive(self):
        return auth.alive(self.access_token, self.base_url)

    def check_error(self):
        return auth.error(self.access_token, self.base_url)

    def check_status(self):
        return auth.status(self.access_token, self.base_url)

    def check_clients(self):
        return auth.clients(self.access_token, self.base_url)

    def check_authorizations(self):
        return auth.authorizations(self.access_token, self.base_url)

    def check_report_health(self):
        return report.health(self.access_token, self.base_url)

    def fetch_report_types(self, details: str = "false"):
        return report.types(self.access_token, self.base_url, details)

    def fetch_reports(self):
        pass
