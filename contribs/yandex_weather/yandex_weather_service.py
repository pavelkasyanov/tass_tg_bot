import datetime
import json
import logging
from typing import Any, Dict, Optional

from contribs.yandex_weather.api_client import YandexWeatherClient
from contribs.yandex_weather.models import YandexWeatherInfo

logger = logging.getLogger(__name__)


class YandexWeatherService:
    _filename = "yandex_data.txt"

    def __init__(self, lat: int, lon: int, api_key: str, lang: str = "ru_RU"):
        self._api_client = YandexWeatherClient(lat, lon, api_key, lang)

    def get_weather_info(self) -> Optional[YandexWeatherInfo]:
        weather_info = self._load_weather_info()

        if not weather_info:
            return self._get_actual_weather_info()

        if weather_info.now_dt + datetime.timedelta(hours=1) > datetime.datetime.now(datetime.timezone.utc):
            return self._load_weather_info()

        return self._get_actual_weather_info()

    def _get_actual_weather_info(self) -> Optional[YandexWeatherInfo]:
        raw_weather_info = self._api_client.get_weather_info()

        if not raw_weather_info:
            return None

        self._save_weather_info(raw_weather_info)

        return YandexWeatherInfo.parse_obj(raw_weather_info)

    def _load_weather_info(self) -> Optional[YandexWeatherInfo]:
        try:
            with open(self._filename, "r") as file:
                raw_weather_info = file.read()
                return YandexWeatherInfo.parse_obj(json.loads(raw_weather_info))
        except Exception as ex:
            logger.exception("Error load yandex cache file! %s", str(ex))
            return None

    def _save_weather_info(self, weather_info: Dict[str, Any]) -> None:
        with open(self._filename, "w") as file:
            file.write(json.dumps(weather_info))
