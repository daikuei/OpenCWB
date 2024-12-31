""" Opendata CWB convertor """
import time
from datetime import datetime, timedelta


class OpendataCWB:

    @staticmethod
    def _get_weather(the_dict, index, wx_index, last_pop, mode):
        value = {}
        start_time = None
        value["dt"] = int(time.time())
        TIME_STR = "time"
        ELEMENTNAME = "elementName"
        ELEMENTVALUE = "elementValue"
        STARTTIME = "startTime"
        VALUE_STR = "value"
        if "Time" in the_dict[0]:
            TIME_STR = "Time"
            ELEMENTNAME = "ElementName"
            ELEMENTVALUE = "ElementValue"
            STARTTIME = "StartTime"
            VALUE_STR = "ElementValue"
            DATATIME = "DataTime"

        if index < len(the_dict[wx_index - 1][TIME_STR]):
            start_time = the_dict[wx_index - 1][TIME_STR][index][STARTTIME]
        if start_time:
            try:
                if "T" in start_time:
                    value["dt"] = int(time.mktime(datetime.strptime(
                        start_time.strip(), "%Y-%m-%dT%H:%M:%S+08:00").timetuple()))
                else:
                    value["dt"] = int(time.mktime(datetime.strptime(
                        start_time.strip(), "%Y-%m-%d %H:%M:%S").timetuple()))
            except ValueError:
                pass
        value["weather"] = [{}]
        value["main"] = {}
        value["calc"] = {}
        value["feels_like"] = {}
        value["pop"] = last_pop
        pop_mode = "PoP12h"
        if mode == "hourly":
            # PoP6h or PoP3h
            pop_mode = "PoP"

        for i in the_dict:
            element_value = None
            if index < len(i[TIME_STR]):
                element_value = i[TIME_STR][index].get(ELEMENTVALUE, None)
            if element_value is None:
                continue
            if i[ELEMENTNAME] in ["WeatherDescription", "天氣預報綜合描述"]:
                # 32
                if VALUE_STR in element_value[0]:
                    value["weather"][0]["description"] = element_value[0]["WeatherDescription"]
                    value["weather"][0]["icon"] = ""
                else:
                    value["weather"][0]["description"] = list(element_value[0].values())[0]
                    value["weather"][0]["icon"] = ""
            elif i[ELEMENTNAME] in ["Wx", "天氣現象"]:
                # 32
                if VALUE_STR in element_value[0]:
                    value["weather"][0]["main"] = element_value[0][VALUE_STR]
                    value["weather"][0]["id"] = int(element_value[1][VALUE_STR])
                else:
                    value["weather"][0]["main"] = list(element_value[0].values())[0]
                    value["weather"][0]["id"] = int(list(element_value[0].values())[1])
            elif pop_mode in i[ELEMENTNAME] or "降雨機率" in i[ELEMENTNAME]:
                # 32
                for j in i[TIME_STR]:
                    if start_time == j[STARTTIME]:
                        if VALUE_STR in element_value[0]:
                            pop = element_value[0][VALUE_STR]
                        else:
                            pop = list(element_value[0].values())[0]
                        if pop == " " or pop == "-":
                            pop = "0"
                        value["pop"] = float(int(pop)/100)
                        break
            elif i[ELEMENTNAME] in ["AT", "體感溫度"]:
                # 56
                if VALUE_STR in element_value[0]:
                    value["main"]["feels_like"] = int(element_value[0][VALUE_STR])
                else:
                    value["main"]["feels_like"] = int(list(element_value[0].values())[0])
            elif i[ELEMENTNAME] in ["MaxAT", "最高體感溫度"]:
                if VALUE_STR in element_value[0]:
                    value["main"]["feels_like"] = int(element_value[0][VALUE_STR])
                    value["feels_like"]["max"] = int(element_value[0][VALUE_STR])
                else:
                    value["main"]["feels_like"] = int(list(element_value[0].values())[0])
                    value["feels_like"]["max"] = int(list(element_value[0].values())[0])
            elif i[ELEMENTNAME] in ["MinAT", "最低體感溫度"]:
                if VALUE_STR in element_value[0]:
                    value["feels_like"]["min"] = int(element_value[0][VALUE_STR])
                else:
                    value["feels_like"]["min"] = int(list(element_value[0].values())[0])
            elif i[ELEMENTNAME] in ["UVI", "紫外線指數"]:
                value["uvi"] = 0
                for j in i[TIME_STR]:
                    if start_time == j[STARTTIME]:
                        if VALUE_STR in element_value[0]:
                            value["uvi"] = int(j[ELEMENTVALUE][0][VALUE_STR])
                        else:
                            value["uvi"] = int(list(j[ELEMENTVALUE][0].values())[0])
                        break
            elif i[ELEMENTNAME] in ["T", "溫度", "平均溫度"]:
                # 56
                if VALUE_STR in element_value[0]:
                    value["main"]["temp"] = int(element_value[0][VALUE_STR])
                else:
                    value["main"]["temp"] = int(list(element_value[0].values())[0])
            elif i[ELEMENTNAME] in ["MaxT", "最高溫度"]:
                if VALUE_STR in element_value[0]:
                    value["main"]["temp_max"] = int(element_value[0][VALUE_STR])
                else:
                    value["main"]["temp_max"] = int(list(element_value[0].values())[0])
            elif i[ELEMENTNAME] in ["MinT", "最低溫度"]:
                if VALUE_STR in element_value[0]:
                    value["main"]["temp_min"] = int(element_value[0][VALUE_STR])
                else:
                    value["main"]["temp_min"] = int(list(element_value[0].values())[0])
            elif i[ELEMENTNAME] in ["Td", "露點溫度", "平均露點溫度"]:
                # 56
                if VALUE_STR in element_value[0]:
                    value["calc"]["dewpoint"] = int(element_value[0][VALUE_STR]) * 100
                else:
                    value["calc"]["dewpoint"] = int(list(element_value[0].values())[0]) * 100
            elif i[ELEMENTNAME] in ["RH", "相對濕度", "平均相對濕度"]:
                # 56
                if VALUE_STR in element_value[0]:
                    value["humidity"] = int(element_value[0][VALUE_STR])
                else:
                    value["humidity"] = int(list(element_value[0].values())[0])
            elif i[ELEMENTNAME] in ["MinCI", "舒適度指數"]:
                # 56
                if VALUE_STR in element_value[0]:
                    value["calc"]["humidex"] = int(element_value[0][VALUE_STR])
                else:
                    value["calc"]["humidex"] = int(list(element_value[0].values())[0])
            elif i[ELEMENTNAME] in ["MaxCI", "舒適度指數"]:
                # 56
                if VALUE_STR in element_value[0]:
                    value["calc"]["heatindex"] = int(element_value[0][VALUE_STR])
                else:
                    value["calc"]["heatindex"] = int(list(element_value[0].values())[0])
            elif i[ELEMENTNAME] in ["WS", "風速"]:
                # 32
                if VALUE_STR in element_value[0]:
                    value["wind_speed"] = int(''.join(
                        k for k in element_value[0][VALUE_STR] if k.isdigit()))
                    value["wind_gust"] = int(''.join(
                        c for c in element_value[1][VALUE_STR] if c.isdigit()))
                else:
                    value["wind_speed"] = int(''.join(
                        k for k in list(element_value[0].values())[0] if k.isdigit()))
                    value["wind_gust"] = int(''.join(
                        c for c in list(element_value[0].values())[1] if c.isdigit()))
            elif i[ELEMENTNAME] in ["WD", "風向"]:
                # 32
                if VALUE_STR in element_value[0]:
                    value["wind_deg"] = element_value[0][VALUE_STR]
                else:
                    value["wind_deg"] = list(element_value[0].values())[0]
            else:
                if VALUE_STR in element_value[0]:
                    value[i[ELEMENTNAME]] = element_value[0][VALUE_STR]
                else:
                    value[i[ELEMENTNAME]] = list(element_value[0].values())[0]
        return value

    @staticmethod
    def _get_weather2(the_dict, index, wx_index, last_pop, mode):
        result = {}
        TIME_STR = "Time"
        ELEMENTNAME = "ElementName"
        ELEMENTVALUE = "ElementValue"
        STARTTIME = "StartTime"
        ENDTIME = "EndTime"
        DATATIME = "DataTime"

        for i in the_dict:
            if i[ELEMENTNAME] in ["T", "溫度", "平均溫度"]:
                # prepare time slots.
                for time_data_idx in range(1, len(i[TIME_STR])):
                    process_time_str = i[TIME_STR][time_data_idx][DATATIME]
                    temp = int(i[TIME_STR][time_data_idx][ELEMENTVALUE][0]["Temperature"])
                    if process_time_str in result:
                        if result[process_time_str].get('main'):
                            result[process_time_str]['main']['temp'] = temp
                        else:
                            result[process_time_str]['main'] = {"temp": temp}
                    else:
                        result[process_time_str] = {
                            "dt": int(time.mktime(datetime.strptime(process_time_str.strip(), "%Y-%m-%dT%H:%M:%S+08:00").timetuple())),
                            "main": {
                                "temp": temp,
                            }
                        }
            elif i[ELEMENTNAME] in ["Td", "露點溫度", "平均露點溫度"]:
                for time_data_idx in range(1, len(i[TIME_STR])):
                    process_time_str = i[TIME_STR][time_data_idx][DATATIME]
                    dewpoint = int(i[TIME_STR][time_data_idx][ELEMENTVALUE][0]["DewPoint"]) * 100
                    if process_time_str in result:
                        if result[process_time_str].get('calc'):
                            result[process_time_str]['calc']['dewpoint'] = dewpoint
                        else:
                            result[process_time_str]['calc'] = {"dewpoint": dewpoint}
                    else:
                        result[process_time_str] = {
                            "dt": int(time.mktime(datetime.strptime(process_time_str.strip(), "%Y-%m-%dT%H:%M:%S+08:00").timetuple())),
                            "calc": {
                                "dewpoint": dewpoint,
                            }
                        }
            elif i[ELEMENTNAME] in ["RH", "相對濕度", "平均相對濕度"]:
                for time_data_idx in range(1, len(i[TIME_STR])):
                    process_time_str = i[TIME_STR][time_data_idx][DATATIME]
                    humidity = int(i[TIME_STR][time_data_idx][ELEMENTVALUE][0]["RelativeHumidity"])
                    if process_time_str in result:
                        result[process_time_str]['humidity'] = humidity
                    else:
                        result[process_time_str] = {'humidity': humidity}
            elif i[ELEMENTNAME] in ["AT", "體感溫度"]:
                for time_data_idx in range(1, len(i[TIME_STR])):
                    process_time_str = i[TIME_STR][time_data_idx][DATATIME]
                    feels_like = i[TIME_STR][time_data_idx][ELEMENTVALUE][0]["ApparentTemperature"]
                    feels_like_int = int(feels_like) if feels_like.isdigit() else feels_like
                    if process_time_str in result:
                        if result[process_time_str].get('main'):
                            result[process_time_str]['main']['feels_like'] = feels_like_int
                        else:
                            result[process_time_str]['main'] = {"feels_like": feels_like_int}
                    else:
                        result[process_time_str] = {
                            "dt": int(time.mktime(datetime.strptime(process_time_str.strip(), "%Y-%m-%dT%H:%M:%S+08:00").timetuple())),
                            "main": {
                                "feels_like": feels_like_int,
                            }
                        }
            elif i[ELEMENTNAME] in ["MaxCI", "舒適度指數"]:
                for time_data_idx in range(1, len(i[TIME_STR])):
                    process_time_str = i[TIME_STR][time_data_idx][DATATIME]
                    humidex = i[TIME_STR][time_data_idx][ELEMENTVALUE][0]["ComfortIndex"]
                    humidex_int = int(humidex) if humidex.isdigit() else humidex
                    if process_time_str in result:
                        if result[process_time_str]['calc']:
                            result[process_time_str]['calc']['humidex'] = humidex_int
                        else:
                            result[process_time_str]['calc'] = {"humidex": humidex_int}
                    else:
                        result[process_time_str] = {
                            "dt": int(time.mktime(datetime.strptime(process_time_str.strip(), "%Y-%m-%dT%H:%M:%S+08:00").timetuple())),
                            "calc": {
                                "humidex": humidex_int,
                            }
                        }
            elif i[ELEMENTNAME] in ["WS", "風速"]:
                for time_data_idx in range(1, len(i[TIME_STR])):
                    process_time_str = i[TIME_STR][time_data_idx][DATATIME]
                    wind_speed = int(i[TIME_STR][time_data_idx][ELEMENTVALUE][0]["WindSpeed"])
                    beau_fort_scale_str = i[TIME_STR][time_data_idx][ELEMENTVALUE][0]["BeaufortScale"]
                    if process_time_str in result:
                        result[process_time_str]['wind_speed'] = wind_speed
                        result[process_time_str]['wind_gust'] = int(beau_fort_scale_str) if beau_fort_scale_str.isdigit() else int(
                            beau_fort_scale_str.replace(">=", "").replace("<=", "").replace(">", "").replace("<", ""))
            elif i[ELEMENTNAME] in ["WD", "風向"]:
                for time_data_idx in range(1, len(i[TIME_STR])):
                    process_time_str = i[TIME_STR][time_data_idx][DATATIME]
                    wind_deg = i[TIME_STR][time_data_idx][ELEMENTVALUE][0]["WindDirection"]
                    if process_time_str in result:
                        result[process_time_str]['wind_deg'] = wind_deg
                    else:
                        result[process_time_str] = {
                            "dt": int(time.mktime(datetime.strptime(process_time_str.strip(), "%Y-%m-%dT%H:%M:%S+08:00").timetuple())),
                            "wind_deg": wind_deg,
                        }
            elif "降雨機率" in i[ELEMENTNAME]:
                for time_data_idx in range(0, len(i[TIME_STR])):
                    start_time_str = i[TIME_STR][time_data_idx][STARTTIME]
                    end_time_str = i[TIME_STR][time_data_idx][ENDTIME]
                    start_time = datetime.strptime(start_time_str.strip(), "%Y-%m-%dT%H:%M:%S+08:00")
                    end_time = datetime.strptime(end_time_str.strip(), "%Y-%m-%dT%H:%M:%S+08:00")
                    if mode == "hourly":
                        time_delta = timedelta(hours=1)
                    else:
                        time_delta = timedelta(hours=12)

                    while start_time <= end_time:
                        process_time_str = start_time.isoformat()+"+08:00"
                        pop = i[TIME_STR][time_data_idx][ELEMENTVALUE][0]["ProbabilityOfPrecipitation"]
                        if process_time_str in result:
                            result[process_time_str]['pop'] = float(int(pop)/100)
                        # else:
                        #     result[process_time_str] = {
                        #         "dt": int(time.mktime(start_time.timetuple())),
                        #         "pop": float(int(pop)/100),
                        #     }
                        start_time = start_time + time_delta

            elif i[ELEMENTNAME] in ["Wx", "天氣現象"]:
                for time_data_idx in range(0, len(i[TIME_STR])):
                    start_time_str = i[TIME_STR][time_data_idx][STARTTIME]
                    end_time_str = i[TIME_STR][time_data_idx][ENDTIME]
                    start_time = datetime.strptime(start_time_str.strip(), "%Y-%m-%dT%H:%M:%S+08:00")
                    end_time = datetime.strptime(end_time_str.strip(), "%Y-%m-%dT%H:%M:%S+08:00")
                    if mode == "hourly":
                        time_delta = timedelta(hours=1)
                    else:
                        time_delta = timedelta(hours=12)
                    while start_time <= end_time:
                        process_time_str = start_time.isoformat()+"+08:00"
                        weather_main= i[TIME_STR][time_data_idx][ELEMENTVALUE][0]["Weather"]
                        weather_code= i[TIME_STR][time_data_idx][ELEMENTVALUE][0]["WeatherCode"]
                        if process_time_str in result:
                            if result[process_time_str].get("weather"):
                                result[process_time_str]['weather'][0] =  {"main": weather_main,
                                                                         "id": int(weather_code),
                                                                         "icon": ""}
                            else:
                                result[process_time_str]['weather'] = [{"main": weather_main,
                                                                         "id": int(weather_code),
                                                                         "icon": ""}]
                        # else:
                        #     result[process_time_str] = {
                        #         "dt": int(time.mktime(start_time.timetuple())),
                        #         "weather": [{"main": weather_main,
                        #                      "id": int(weather_code),
                        #                      "icon": ""}]
                        #     }
                        start_time = start_time + time_delta

            elif i[ELEMENTNAME] in ["WeatherDescription", "天氣預報綜合描述"]:
                for time_data_idx in range(0, len(i[TIME_STR])):
                    start_time_str = i[TIME_STR][time_data_idx][STARTTIME]
                    end_time_str = i[TIME_STR][time_data_idx][ENDTIME]
                    start_time = datetime.strptime(start_time_str.strip(), "%Y-%m-%dT%H:%M:%S+08:00")
                    end_time = datetime.strptime(end_time_str.strip(), "%Y-%m-%dT%H:%M:%S+08:00")
                    if mode == "hourly":
                        time_delta = timedelta(hours=1)
                    else:
                        time_delta = timedelta(hours=12)
                    while start_time <= end_time:
                        process_time_str = start_time.isoformat()+"+08:00"
                        description= i[TIME_STR][time_data_idx][ELEMENTVALUE][0]["WeatherDescription"]
                        if process_time_str in result:
                            if result[process_time_str].get("weather"):
                                if result[process_time_str]['weather'][0]:
                                    result[process_time_str]['weather'][0]["description"] = description
                                else:
                                    result[process_time_str]['weather'][0] = {"description": description}
                            # else:
                            #     result[process_time_str]['weather'] = [{"description": description}]
                        # else:
                        #     result[process_time_str] = {
                        #         "dt": int(time.mktime(start_time.timetuple())),
                        #         "weather": [{"description": description}]
                        #     }
                        start_time = start_time + time_delta
        return list(result.values())

    @classmethod
    def to_dict(cls, the_dict):
        value = {}
        TIME_STR = "time"
        LOCATIONS = "locations"
        LOCATION = "location"
        LATITUDE = "lat"
        LONGITUDE = "lon"
        WEATHERELEMENT = "weatherElement"
        DATASETDESCRIPTION = "datasetDescription"
        ELEMENTNAME = "elementName"
        if "Locations" in the_dict["records"]:
            TIME_STR = "Time"
            LOCATIONS = "Locations"
            LOCATION = "Location"
            LATITUDE = "Latitude"
            LONGITUDE = "Longitude"
            WEATHERELEMENT = "WeatherElement"
            DATASETDESCRIPTION = "DatasetDescription"
            ELEMENTNAME = "ElementName"

        record = None
        for i in the_dict["records"][LOCATIONS]:
            if len(i[LOCATION]) >= 1:
                record = i
                break

        if record is None:
            return value

        value["lon"] = float(record[LOCATION][0][LONGITUDE])
        value["lat"] = float(record[LOCATION][0][LATITUDE])
        value["timezone"] = 8

        mode = ""
        dataset_desc = record[DATASETDESCRIPTION]
        # 臺灣各縣市鄉鎮未來1週逐12小時天氣預報
        if dataset_desc == "臺灣各縣市鄉鎮未來1週逐12小時天氣預報":
            mode = "daily"
        if dataset_desc == "臺灣各縣市鄉鎮未來1週天氣預報":
            mode = "daily"
        if dataset_desc == "臺灣各縣市鄉鎮未來3天(72小時)逐3小時天氣預報":
            mode = "hourly"
        if dataset_desc == "臺灣各縣市鄉鎮未來3天天氣預報":
            mode = "hourly"

        wx_index = 0
        length = 0
        last_pop = 0

        for i in record[LOCATION][0][WEATHERELEMENT]:
            if i['ElementName'] == "Wx" or "天氣現象" == i[ELEMENTNAME]:
                length = len(i[TIME_STR])
                break
            wx_index = wx_index + 1

        value["current"] = OpendataCWB._get_weather(
            record[LOCATION][0][WEATHERELEMENT], 0, wx_index, last_pop, mode)
        last_pop = value["current"]["pop"]

        value[mode] = []
        wx_index = len(record[LOCATION][0][WEATHERELEMENT])
        value[mode] = OpendataCWB._get_weather2(record[LOCATION][0][WEATHERELEMENT], i, wx_index, last_pop, mode)
        last_pop = value["current"]["pop"]

        issue_data = value[mode][0]
        if not issue_data.get("pop"):
            issue_data["pop"] = value["current"]["pop"]
            issue_data["weather"] = value["current"]["weather"]
        return value
