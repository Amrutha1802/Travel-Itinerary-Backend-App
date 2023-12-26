from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime


def create_timestamp_from_mysql_date(mysql_date):
    datetime_obj = datetime.combine(mysql_date, datetime.min.time())
    date_timestamp = Timestamp()
    date_timestamp.FromDatetime(datetime_obj)
    return date_timestamp


def create_mysql_date_from_timestamp(date):
    return date.ToDatetime().date()


def create_time_stamp_from_datetime(date):
    timestamp_obj = Timestamp()
    timestamp_obj.FromDatetime(date)
    return timestamp_obj


def create_mysql_time_from_timestamp(timestamp_object):
    datetime_obj = timestamp_object.ToDatetime()
    mysql_time_str = datetime_obj.strftime("%H:%M:%S")
    return mysql_time_str


def create_timestamp_from_mysql_time(timedelta_obj):
    epoch = datetime.utcfromtimestamp(0)
    target_datetime = epoch + timedelta_obj
    timestamp_obj = Timestamp()
    timestamp_obj.FromDatetime(target_datetime)
    return timestamp_obj
