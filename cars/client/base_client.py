import enum
from dataclasses import dataclass, field
from typing import Dict

import httpx


@dataclass
class ClientConfig:
    base_url: str
    user_agent: str
    basic_auth: httpx.BasicAuth = field(default=None)
    base_headers: Dict[str, str] = field(default_factory=dict)


async def raise_on_4xx_5xx(response):
    response.raise_for_status()


class BaseClient:
    def __init__(self, client_config: ClientConfig):
        self._base_url = client_config.base_url

        timeout = httpx.Timeout(timeout=10)

        headers = {"User-Agent": client_config.user_agent}
        if client_config.base_headers:
            headers.update(client_config.base_headers)

        self._session = httpx.AsyncClient(
            auth=client_config.basic_auth,
            headers=headers,
            timeout=timeout,
            event_hooks={"response": [raise_on_4xx_5xx]},
        )

    def _url_for(self, endpoint: enum.Enum):
        return self._base_url + endpoint.value

    def close_session(self):
        return self._session.aclose()
