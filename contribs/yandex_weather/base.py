from enum import Enum


class WeatherCondition(str, Enum):
    CLEAR = "clear"
    PARTLY_CLOUDY = "partly-cloudy"
    CLOUDY = "cloudy"
    OVERCAST = "overcast"
    DRIZZLE = "drizzle"
    LIGHT_RAIN = "light-rain"
    RAIN = "rain"
    MODERATE_RAIN = "moderate-rain"
    HEAVY_RAIN = "heavy-rain"
    CONTINUOUS_HEAVY_RAIN = "continuous-heavy-rain"
    SHOWERS = "showers"
    WET_SNOW = "wet-snow"
    LIGHT_SNOW = "light-snow"
    SNOW = "snow"
    SNOW_SHOWERS = "snow-showers"
    HAIL = "hail"
    THUNDERSTORM = "thunderstorm"
    THUNDERSTORM_WITH_RAIN = "thunderstorm-with-rain"
    THUNDERSTORM_WITH_HAIL = "thunderstorm-with-hail"


class WindDirection(str, Enum):
    NORTH_WEST = "nw"
    NORTH = "n"
    NORTH_EAST = "ne"
    EAST = "e"
    SOUTH_EAST = "se"
    SOUTH = "s"
    SOUTH_WEST = "sw"
    WEST = "w"
    CALM = "c"


class DayTimeType(str, Enum):
    DAY = "d"
    NIGHT = "n"


class SeasonType(str, Enum):
    SUMMER = "summer"
    AUTUMN = "autumn"
    WINTER = "winter"
    SPRING = "spring"


class MoonCode(str, Enum):
    MOON_CODE_0 = "moon-code-0"
    MOON_CODE_1 = "moon-code-1"
    MOON_CODE_2 = "moon-code-2"
    MOON_CODE_3 = "moon-code-3"
    MOON_CODE_4 = "moon-code-4"
    MOON_CODE_5 = "moon-code-5"
    MOON_CODE_6 = "moon-code-6"
    MOON_CODE_7 = "moon-code-7"
    MOON_CODE_8 = "moon-code-8"
    MOON_CODE_9 = "moon-code-9"
    MOON_CODE_10 = "moon-code-10"
    MOON_CODE_11 = "moon-code-11"
    MOON_CODE_12 = "moon-code-12"
    MOON_CODE_13 = "moon-code-13"
    MOON_CODE_14 = "moon-code-14"
    MOON_CODE_15 = "moon-code-15"


class ForecastPartType(str, Enum):
    NIGHT = "night"
    MORNING = "morning"
    DAY = "day"
    EVENING = "evening"
