import datetime
from copy import deepcopy
from unittest.mock import patch

from pytest_httpx import HTTPXMock

from contribs.yandex_weather.api_client import YandexWeatherClient
from contribs.yandex_weather.models import YandexWeatherInfo
from contribs.yandex_weather.tests.data import WEATHER_JSON_RESPONSE
from contribs.yandex_weather.yandex_weather_service import YandexWeatherService


def test_get_info_success(yandex_weather_service: YandexWeatherService, httpx_mock: HTTPXMock) -> None:
    with patch.object(YandexWeatherClient, "get_weather_info", return_value=WEATHER_JSON_RESPONSE) as mock_method:
        with patch.object(yandex_weather_service, "_save_weather_info", return_value=None) as mocked:
            resp = yandex_weather_service.get_weather_info()

            assert resp is not None

            assert resp == YandexWeatherInfo.parse_obj(WEATHER_JSON_RESPONSE)

    assert mocked.call_count == 1


def test_get_info_fail(yandex_weather_service: YandexWeatherService, httpx_mock: HTTPXMock) -> None:
    with patch.object(YandexWeatherClient, "get_weather_info", return_value={}) as mock_method:
        resp = yandex_weather_service.get_weather_info()

        assert resp is None


def test_get_info_from_cache_success(yandex_weather_service: YandexWeatherService, httpx_mock: HTTPXMock) -> None:
    with patch.object(YandexWeatherClient, "get_weather_info", return_value={}) as mock_method:
        api_response = deepcopy(WEATHER_JSON_RESPONSE)
        api_response["now_dt"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        mock_return_value = YandexWeatherInfo.parse_obj(api_response)
        with patch.object(yandex_weather_service, "_load_weather_info", return_value=mock_return_value):
            resp = yandex_weather_service.get_weather_info()

            assert resp is not None
            assert resp == mock_return_value

    assert mock_method.call_count == 0
