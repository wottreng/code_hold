import time
import datetime


def dateNow():
    date = datetime.date.today()
    dateFormat = date.strftime("%d-%b-%Y")
    return dateFormat


def dateTimeNow():
    date = datetime.datetime.now()
    dateFormat = date.strftime("%d-%b-%Y %H:%M:%S")
    return dateFormat


def epochTimeNow():
    return str(time.time()).split(".")[0]


def convertEpochTime(epochTime):
    date = datetime.datetime.fromtimestamp(epochTime)
    dateFormat = date.strftime("%d-%b-%Y %H:%M:%S")
    return dateFormat

# calculate time in seconds between two timestamps, format: "HH:MM:SS.mmm"
def calculate_elapsed_time_seconds(start_timestamp: str, end_timestamp: str):
    start_timestamp_value = datetime.datetime.strptime(start_timestamp, "%H:%M:%S.%f")
    end_timestamp_value = datetime.datetime.strptime(end_timestamp, "%H:%M:%S.%f")
    difference = end_timestamp_value - start_timestamp_value
    return difference.total_seconds()


if __name__ == "__main__":
    print(dateNow())  # 15-Feb-2022
    print(dateTimeNow())  # 15-Feb-2022 13:34:41
    print(epochTimeNow())  # 1644950081
    print(convertEpochTime(int(epochTimeNow())))  # 15-Feb-2022 13:35:50
    print(calculate_elapsed_time_seconds("00:03:02.124", "01:02:34.401"))  # 3572.277
