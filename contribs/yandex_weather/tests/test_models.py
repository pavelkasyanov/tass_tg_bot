from contribs.yandex_weather.models import YandexWeatherInfo
from contribs.yandex_weather.tests.data import WEATHER_JSON_RESPONSE


def test_success_model() -> None:
    model = YandexWeatherInfo.parse_obj(WEATHER_JSON_RESPONSE)
    assert model is not None


def test_model_localization() -> None:
    model = YandexWeatherInfo.parse_obj(WEATHER_JSON_RESPONSE)
    assert model is not None

    assert model.fact.condition_localized is not None
