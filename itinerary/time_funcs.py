from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp


DATE_FMT = ""
TIME_FMT = "%H:%M:%S"

from google.protobuf.timestamp_pb2 import Timestamp
from datetime import timedelta, datetime, date


def get_date_string_from_timestamp(pb_timestamp):
    """
    Converts a timestamp object to datetime.date object
    """
    return str(pb_timestamp.ToDatetime().date())


def get_time_str_from_timestamp(timestamp_object):
    """
    Converts timestamp object to datetime.timedelta object
    """
    datetime_obj = timestamp_object.ToDatetime()
    time_str = datetime_obj.strftime("%H:%M:%S")
    return time_str


def get_timestamp_from_time(timedelta_obj):
    """
    Converts a timedelta_obj to protobuf Timestamp
    """
    epoch = datetime.utcfromtimestamp(0)
    target_datetime = epoch + timedelta_obj
    timestamp_obj = Timestamp()
    timestamp_obj.FromDatetime(target_datetime)
    return timestamp_obj


def get_pb_timestamp_from_date(date_object):
    """
    Converts a datetime.date object to a protobuf Timestamp object.
    """
    dt_object = datetime.combine(date_object, datetime.min.time())
    timestamp = Timestamp()
    timestamp.FromDatetime(dt_object)

    return timestamp
