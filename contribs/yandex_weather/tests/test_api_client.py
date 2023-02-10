from unittest.mock import patch

from contribs.yandex_weather.api_client import YandexWeatherClient
from contribs.yandex_weather.tests.data import WEATHER_JSON_RESPONSE


def test_get_info_success(yandex_weather_client, httpx_mock) -> None:
    with patch.object(YandexWeatherClient, "get_weather_info", return_value=WEATHER_JSON_RESPONSE):
        resp = yandex_weather_client.get_weather_info()
        assert resp is not None
        assert resp == WEATHER_JSON_RESPONSE
