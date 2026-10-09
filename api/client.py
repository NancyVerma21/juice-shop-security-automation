from pathlib import Path

import requests


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json"
        })

    def request(self, method: str, endpoint: str, **kwargs):
        timeout = kwargs.pop("timeout", 10)

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        return self.session.request(
            method=method.upper(),
            url=url,
            timeout=timeout,
            **kwargs
        )

    def close(self):
        self.session.close()
