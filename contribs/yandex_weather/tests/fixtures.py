import pytest

from contribs.yandex_weather.api_client import YandexWeatherClient
from contribs.yandex_weather.yandex_weather_service import YandexWeatherService
from settings import settings


@pytest.fixture
def yandex_weather_client() -> YandexWeatherClient:
    return YandexWeatherClient(
        lat=settings.LOCATION_LAT, lon=settings.LOCATION_LON, api_key=settings.YANDEX_WEATHER_API_KEY
    )


@pytest.fixture
def yandex_weather_service() -> YandexWeatherService:
    return YandexWeatherService(
        lat=settings.LOCATION_LAT, lon=settings.LOCATION_LON, api_key=settings.YANDEX_WEATHER_API_KEY
    )
