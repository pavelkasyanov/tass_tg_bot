from datetime import date, datetime, time
from typing import List, Optional

from pydantic import BaseModel, validator

from contribs.yandex_weather.base import (
    DayTimeType,
    ForecastPartType,
    MoonCode,
    SeasonType,
    WeatherCondition,
    WindDirection,
)
from contribs.yandex_weather.localization import get_localized_value


class YandexWeatherLocationInfo(BaseModel):
    lat: int
    lon: int
    url: str


class YandexWeatherFactInfo(BaseModel):
    temp: int
    feels_like: int
    temp_water: Optional[int]
    icon: str
    condition: WeatherCondition
    wind_speed: int
    wind_gust: int
    wind_dir: Optional[WindDirection]
    pressure_mm: int
    pressure_pa: int
    humidity: int
    daytime: DayTimeType
    polar: bool
    season: SeasonType
    obs_time: int

    @property
    def condition_localized(self) -> str:
        return get_localized_value(self.condition) or self.condition.value

    @property
    def wind_dir_localized(self) -> str:
        if self.wind_dir:
            return get_localized_value(self.wind_dir) or self.wind_dir.value
        return ""

    @property
    def daytime_localized(self) -> str:
        return get_localized_value(self.daytime) or self.daytime.value

    @property
    def season_localized(self) -> str:
        return get_localized_value(self.season) or self.season.value

    @validator("humidity")
    def humidity_validator(cls, v) -> int:  # type: ignore
        assert 0 <= v <= 100, "invalid humidity"
        return v


class YandexWeatherForecastPartInfo(BaseModel):
    part_name: ForecastPartType
    temp_min: int
    temp_max: int
    temp_avg: int
    feels_like: int
    icon: str
    condition: WeatherCondition
    daytime: DayTimeType
    polar: bool
    wind_speed: int
    wind_gust: int
    wind_dir: WindDirection
    pressure_mm: int
    pressure_pa: int
    humidity: int
    prec_mm: int
    prec_period: int  # change to timestamp
    prec_prob: int


class YandexWeatherForecastInfo(BaseModel):
    date: date
    date_ts: int
    week: int
    sunrise: Optional[time]
    sunset: Optional[time]
    moon_code: int
    moon_text: MoonCode
    parts: List[YandexWeatherForecastPartInfo]


class YandexWeatherInfo(BaseModel):
    now: int
    now_dt: datetime
    info: YandexWeatherLocationInfo
    fact: YandexWeatherFactInfo
    forecast: YandexWeatherForecastInfo
