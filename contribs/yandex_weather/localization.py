from typing import Any, Dict, Optional, Union

from contribs.yandex_weather.models import (
    DayTimeType,
    ForecastPartType,
    MoonCode,
    SeasonType,
    WeatherCondition,
    WindDirection,
)

WeatherConditionLoc: Dict[str, Any] = {
    WeatherCondition.CLEAR: "ясно",
    WeatherCondition.PARTLY_CLOUDY: "малооблачно",
    WeatherCondition.CLOUDY: "облачно с прояснениями",
    WeatherCondition.OVERCAST: "пасмурно",
    WeatherCondition.DRIZZLE: "морось",
    WeatherCondition.LIGHT_RAIN: "небольшой дождь",
    WeatherCondition.RAIN: "дождь",
    WeatherCondition.MODERATE_RAIN: "умеренно сильный дождь",
    WeatherCondition.HEAVY_RAIN: "сильный дождь",
    WeatherCondition.CONTINUOUS_HEAVY_RAIN: "длительный сильный дождь",
    WeatherCondition.SHOWERS: "ливень",
    WeatherCondition.WET_SNOW: "дождь со снегом",
    WeatherCondition.LIGHT_SNOW: "небольшой снег",
    WeatherCondition.SNOW: "снег",
    WeatherCondition.SNOW_SHOWERS: "снегопад",
    WeatherCondition.HAIL: "град",
    WeatherCondition.THUNDERSTORM: "гроза",
    WeatherCondition.THUNDERSTORM_WITH_RAIN: "дождь с грозой",
    WeatherCondition.THUNDERSTORM_WITH_HAIL: "гроза с градом",
}

WindDirectionLoc: Dict[str, Any] = {
    WindDirection.NORTH_WEST: "северо-западное",
    WindDirection.NORTH: "северное",
    WindDirection.NORTH_EAST: "северо-восточное",
    WindDirection.EAST: "восточное",
    WindDirection.SOUTH_EAST: "юго-восточное",
    WindDirection.SOUTH: "южное",
    WindDirection.SOUTH_WEST: "юго-западное",
    WindDirection.WEST: "западное",
    WindDirection.CALM: "штиль",
}

DayTimeTypeLoc: Dict[str, Any] = {
    DayTimeType.DAY: "светлое время суток",
    DayTimeType.NIGHT: "темное время суток",
}

SeasonTypeLoc: Dict[str, Any] = {
    SeasonType.SUMMER: "лето",
    SeasonType.AUTUMN: "осень",
    SeasonType.WINTER: "зима",
    SeasonType.SPRING: "весна",
}

MoonCodeLoc: Dict[str, Any] = {
    MoonCode.MOON_CODE_0: "полнолуние",
    MoonCode.MOON_CODE_1: "убывающая луна",
    MoonCode.MOON_CODE_2: "убывающая луна",
    MoonCode.MOON_CODE_3: "убывающая луна",
    MoonCode.MOON_CODE_4: "последняя четверть",
    MoonCode.MOON_CODE_5: "убывающая луна",
    MoonCode.MOON_CODE_6: "убывающая луна",
    MoonCode.MOON_CODE_7: "убывающая луна",
    MoonCode.MOON_CODE_8: "новолуние",
    MoonCode.MOON_CODE_9: "растущая луна",
    MoonCode.MOON_CODE_10: "растущая луна",
    MoonCode.MOON_CODE_11: "растущая луна",
    MoonCode.MOON_CODE_12: "первая четверть",
    MoonCode.MOON_CODE_13: "растущая луна",
    MoonCode.MOON_CODE_14: "растущая луна",
    MoonCode.MOON_CODE_15: "растущая луна",
}

ForecastPartTypeLoc: Dict[str, Any] = {
    ForecastPartType.NIGHT: "ночь",
    ForecastPartType.MORNING: "утро",
    ForecastPartType.DAY: "день",
    ForecastPartType.EVENING: "вечер",
}

LocType = Union[WeatherCondition, WindDirection, DayTimeType, SeasonType, MoonCode, ForecastPartType]


def get_localized_value(value: LocType) -> Optional[str]:
    loc_map = {
        WeatherCondition.__name__: WeatherConditionLoc,
        WindDirection.__name__: WindDirectionLoc,
        DayTimeType.__name__: DayTimeTypeLoc,
        SeasonType.__name__: SeasonTypeLoc,
        MoonCode.__name__: MoonCodeLoc,
        ForecastPartType.__name__: ForecastPartTypeLoc,
    }

    current_loc_map = loc_map.get(value.__class__.__name__) or {}

    return current_loc_map.get(value)
