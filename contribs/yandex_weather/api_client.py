import logging
from typing import Any, Dict, Optional

import httpx

logger = logging.getLogger(__name__)


class YandexWeatherClient:
    _url = "https://api.weather.yandex.ru/v2/informers"

    def __init__(self, lat: int, lon: int, api_key: str, lang: str = "ru_RU"):
        self._lat = lat
        self._lon = lon
        self._lang = lang
        self._api_key = api_key

    def get_weather_info(self) -> Optional[Dict[str, Any]]:
        try:
            params = {"lat": self._lat, "lon": self._lat, "lang": self._lang}

            headers = {
                "X-Yandex-API-Key": self._api_key,
                "Content-Type": "application/json",
            }

            resp = httpx.get(url=self._url, params=params, headers=headers)  # type: ignore
            resp.raise_for_status()
            return resp.json()
        except Exception as ex:
            logger.exception("Error get weather info, %s", str(ex))
            return None
