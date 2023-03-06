from datetime import datetime
from uuid import UUID

# 0x01b21dd213814000 is the number of 100-ns intervals between the
# UUID epoch 1582-10-15 00:00:00 and the Unix epoch 1970-01-01 00:00:00.
_EPOCH_OFFSET = 0x01b21dd213814000


def _get_uuid_time_ns(urn: UUID):
    '''
    Returns the time used to generate a version 1 UUID in nanoseconds
    '''
    return (urn.time - 0x01b21dd213814000) * 100

def _get_time_low(urn: UUID):
    timestamp = _get_uuid_time_ns(urn) // 100 + _EPOCH_OFFSET
    return timestamp & 0xffffffff


def _get_time_mid(urn: UUID):
    timestamp = _get_uuid_time_ns(urn) // 100 + _EPOCH_OFFSET
    return (timestamp >> 32) & 0xffff


def _get_time_hi_version(urn: UUID):
    timestamp = _get_uuid_time_ns(urn) // 100 + _EPOCH_OFFSET
    return (timestamp >> 48) & 0x0fff


def _get_uuid_datetime(urn: UUID):
    timestamp = _get_uuid_time_ns(urn) / 1e9
    return datetime.fromtimestamp(timestamp)


def get_datetime_dict(urn: UUID):
    urn_date = _get_uuid_datetime(urn).isoformat()
    urn_date_time_low = _get_time_low(urn)
    urn_date_time_mid = _get_time_mid(urn)
    urn_date_time_hi_version = _get_time_hi_version(urn)

    return {
        "date": urn_date,
        "time_low": urn_date_time_low,
        "time_mid": urn_date_time_mid,
        "time_hi_version": urn_date_time_hi_version
    }
