"""Consts for the OpenCWB."""
# pylint: disable=line too long
from homeassistant.components.weather import (
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_EXCEPTIONAL,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_HAIL,
    ATTR_CONDITION_LIGHTNING,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
    ATTR_CONDITION_SUNNY,
    ATTR_CONDITION_WINDY,
    ATTR_CONDITION_WINDY_VARIANT,
    ATTR_FORECAST_CONDITION,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_PRECIPITATION_PROBABILITY,
    # ATTR_FORECAST_PRESSURE,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_TIME,
    ATTR_FORECAST_WIND_BEARING,
    ATTR_FORECAST_WIND_SPEED,
)
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import (
    DEGREE,
    UnitOfLength,
    PERCENTAGE,
    # PRESSURE_HPA,
    UnitOfSpeed,
    UnitOfTemperature,
    UV_INDEX,
)

DOMAIN = "opencwb"
CONF_TRACK_HOME = "track_home"

DEFAULT_NAME = "OpenCWB"
DEFAULT_LANGUAGE = "zh_tw"
ATTRIBUTION = "Data provided by Opendata CWA"
MANUFACTURER = "OpenCWB (中央氣象局氣象資料開放平臺)"
CONF_LANGUAGE = "language"
CONF_LOCATION_NAME = "location_name"
CONFIG_FLOW_VERSION = 1
ENTRY_NAME = "name"
ENTRY_WEATHER_COORDINATOR = "weather_coordinator"
ATTR_API_PRECIPITATION = "precipitation"
ATTR_API_PRECIPITATION_KIND = "precipitation_kind"
ATTR_API_DATETIME = "datetime"
ATTR_API_DEW_POINT = "dew_point"
ATTR_API_WEATHER = "weather"
ATTR_API_TEMPERATURE = "temperature"
ATTR_API_FEELS_LIKE_TEMPERATURE = "feels_like_temperature"
ATTR_API_WIND_GUST = "wind_gust"
ATTR_API_WIND_SPEED = "wind_speed"
ATTR_API_WIND_BEARING = "wind_bearing"
ATTR_API_HUMIDITY = "humidity"
ATTR_API_PRESSURE = "pressure"
ATTR_API_CONDITION = "condition"
ATTR_API_CLOUDS = "clouds"
ATTR_API_RAIN = "rain"
ATTR_API_SNOW = "snow"
ATTR_API_UV_INDEX = "uv_index"
ATTR_API_WEATHER_CODE = "weather_code"
ATTR_API_FORECAST = "forecast"
SENSOR_NAME = "sensor_name"
SENSOR_UNIT = "sensor_unit"
SENSOR_DEVICE_CLASS = "sensor_device_class"
UPDATE_LISTENER = "update_listener"
PLATFORMS = ["sensor", "weather"]

ATTR_API_FORECAST_CLOUDS = "clouds"
ATTR_API_FORECAST_CONDITION = "condition"
ATTR_API_FORECAST_FEELS_LIKE_TEMPERATURE = "feels_like_temperature"
ATTR_API_FORECAST_HUMIDITY = "humidity"
ATTR_API_FORECAST_PRECIPITATION = "precipitation"
ATTR_API_FORECAST_PRECIPITATION_PROBABILITY = "precipitation_probability"
ATTR_API_FORECAST_PRESSURE = "pressure"
ATTR_API_FORECAST_TEMP = "temperature"
ATTR_API_FORECAST_TEMP_LOW = "templow"
ATTR_API_FORECAST_TIME = "datetime"
ATTR_API_FORECAST_WIND_BEARING = "wind_bearing"
ATTR_API_FORECAST_WIND_SPEED = "wind_speed"

FORECAST_MODE_HOURLY = "hourly"
FORECAST_MODE_DAILY = "daily"
FORECAST_MODE_FREE_DAILY = "freedaily"
FORECAST_MODE_ONECALL_HOURLY = "onecall_hourly"
FORECAST_MODE_ONECALL_DAILY = "onecall_daily"
FORECAST_MODES = [
    FORECAST_MODE_HOURLY,
    FORECAST_MODE_DAILY,
    FORECAST_MODE_ONECALL_HOURLY,
    FORECAST_MODE_ONECALL_DAILY,
]
DEFAULT_FORECAST_MODE = FORECAST_MODE_HOURLY

MONITORED_CONDITIONS = [
    ATTR_API_WEATHER,
    ATTR_API_DEW_POINT,
    ATTR_API_TEMPERATURE,
    ATTR_API_FEELS_LIKE_TEMPERATURE,
    ATTR_API_WIND_SPEED,
    ATTR_API_WIND_BEARING,
    ATTR_API_HUMIDITY,
    # ATTR_API_PRESSURE,
    # ATTR_API_CLOUDS,
    # ATTR_API_RAIN,
    # ATTR_API_SNOW,
    # ATTR_API_PRECIPITATION_KIND,
    ATTR_API_UV_INDEX,
    ATTR_API_CONDITION,
    ATTR_API_WEATHER_CODE,
]
FORECAST_MONITORED_CONDITIONS = [
    ATTR_FORECAST_CONDITION,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_PRECIPITATION_PROBABILITY,
    # ATTR_FORECAST_PRESSURE,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_TIME,
    ATTR_FORECAST_WIND_BEARING,
    ATTR_FORECAST_WIND_SPEED,
]
LANGUAGES = [
    "en",
    "zh_tw",
]
WEATHER_CODE_SUNNY_OR_CLEAR_NIGHT = 0
CONDITION_CLASSES = {
    ATTR_CONDITION_CLOUDY: [7],
    ATTR_CONDITION_FOG: [
        24, 25, 26, 27, 28, 31, 32, 33, 34, 35, 36, 38, 39, 41],
    ATTR_CONDITION_HAIL: [42],
    ATTR_CONDITION_LIGHTNING: [15, 16, 17],
    ATTR_CONDITION_LIGHTNING_RAINY: [18],
    ATTR_CONDITION_PARTLYCLOUDY: [4, 5, 6],
    ATTR_CONDITION_POURING: [18],
    ATTR_CONDITION_RAINY: [
        8, 9, 10, 11, 12, 13, 14, 19, 20, 21, 22, 29, 30, 31],
    ATTR_CONDITION_SNOWY: [42],
    ATTR_CONDITION_SNOWY_RAINY: [23, 37],
    ATTR_CONDITION_SUNNY: [1],
    ATTR_CONDITION_WINDY: [2],
    ATTR_CONDITION_WINDY_VARIANT: [3],
    ATTR_CONDITION_EXCEPTIONAL: [
        40
    ],
}
WEATHER_SENSOR_TYPES = {
    ATTR_API_WEATHER: {SENSOR_NAME: "Weather"},
    ATTR_API_DEW_POINT: {
        SENSOR_NAME: "Dew Point",
        SENSOR_UNIT: UnitOfTemperature.CELSIUS,
        SENSOR_DEVICE_CLASS: SensorDeviceClass.TEMPERATURE,
    },
    ATTR_API_TEMPERATURE: {
        SENSOR_NAME: "Temperature",
        SENSOR_UNIT: UnitOfTemperature.CELSIUS,
        SENSOR_DEVICE_CLASS: SensorDeviceClass.TEMPERATURE,
    },
    ATTR_API_FEELS_LIKE_TEMPERATURE: {
        SENSOR_NAME: "Feels like temperature",
        SENSOR_UNIT: UnitOfTemperature.CELSIUS,
        SENSOR_DEVICE_CLASS: SensorDeviceClass.TEMPERATURE,
    },
    ATTR_API_WIND_SPEED: {
        SENSOR_NAME: "Wind speed",
        SENSOR_UNIT: UnitOfSpeed.METERS_PER_SECOND,
    },
    ATTR_API_WIND_BEARING: {SENSOR_NAME: "Wind bearing", SENSOR_UNIT: DEGREE},
    ATTR_API_HUMIDITY: {
        SENSOR_NAME: "Humidity",
        SENSOR_UNIT: PERCENTAGE,
        SENSOR_DEVICE_CLASS: SensorDeviceClass.HUMIDITY,
    },
    # ATTR_API_PRESSURE: {
    #     SENSOR_NAME: "Pressure",
    #    SENSOR_UNIT: PRESSURE_HPA,
    #     SENSOR_DEVICE_CLASS: SensorDeviceClass.PRESSURE,
    # },
    # ATTR_API_CLOUDS: {SENSOR_NAME: "Cloud coverage", SENSOR_UNIT: PERCENTAGE},
    # ATTR_API_RAIN: {SENSOR_NAME: "Rain", SENSOR_UNIT: UnitOfLength.MILLIMETERS},
    # ATTR_API_SNOW: {SENSOR_NAME: "Snow", SENSOR_UNIT: UnitOfLength.MILLIMETERS},
    # ATTR_API_PRECIPITATION_KIND: {SENSOR_NAME: "Precipitation kind"},
    ATTR_API_UV_INDEX: {
        SENSOR_NAME: "UV Index",
        SENSOR_UNIT: UV_INDEX,
    },
    ATTR_API_CONDITION: {SENSOR_NAME: "Condition"},
    ATTR_API_WEATHER_CODE: {SENSOR_NAME: "Weather Code"},
}
FORECAST_SENSOR_TYPES = {
    ATTR_FORECAST_CONDITION: {SENSOR_NAME: "Condition"},
    ATTR_FORECAST_PRECIPITATION: {
        SENSOR_NAME: "Precipitation",
        SENSOR_UNIT: UnitOfLength.MILLIMETERS,
    },
    ATTR_FORECAST_PRECIPITATION_PROBABILITY: {
        SENSOR_NAME: "Precipitation probability",
        SENSOR_UNIT: PERCENTAGE,
    },
    # ATTR_FORECAST_PRESSURE: {
    #     SENSOR_NAME: "Pressure",
    #     SENSOR_UNIT: PRESSURE_HPA,
    #     SENSOR_DEVICE_CLASS: SensorDeviceClass.PRESSURE,
    # },
    ATTR_FORECAST_TEMP: {
        SENSOR_NAME: "Temperature",
        SENSOR_UNIT: UnitOfTemperature.CELSIUS,
        SENSOR_DEVICE_CLASS: SensorDeviceClass.TEMPERATURE,
    },
    ATTR_FORECAST_TEMP_LOW: {
        SENSOR_NAME: "Temperature Low",
        SENSOR_UNIT: UnitOfTemperature.CELSIUS,
        SENSOR_DEVICE_CLASS: SensorDeviceClass.TEMPERATURE,
    },
    ATTR_FORECAST_TIME: {
        SENSOR_NAME: "Time",
        SENSOR_DEVICE_CLASS: SensorDeviceClass.TIMESTAMP,
    },
    ATTR_API_WIND_BEARING: {SENSOR_NAME: "Wind bearing", SENSOR_UNIT: DEGREE},
    ATTR_API_WIND_SPEED: {
        SENSOR_NAME: "Wind speed",
        SENSOR_UNIT: UnitOfSpeed.METERS_PER_SECOND,
    },
}
