from contribs.yandex_weather.tests.data import WEATHER_JSON_RESPONSE


def test_get_info_success(yandex_weather_client, httpx_mock) -> None:
    httpx_mock.add_response(json=WEATHER_JSON_RESPONSE)

    resp = yandex_weather_client.get_weather_info()
    assert resp is not None
