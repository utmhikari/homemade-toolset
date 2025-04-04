import datetime


class Format:
    # default
    SECONDS = '%Y-%m-%d %H:%M:%S'
    MILLISECONDS = '%Y-%m-%d %H:%M:%S.%f'

    # RFC3339
    SECONDS_RFC3339 = '%Y-%m-%dT%H:%M:%SZ'
    MILLISECONDS_RFC3339 = '%Y-%m-%dT%H:%M:%S.%fZ'


class Precision:
    SECOND = 'second'
    MILLISECOND = 'millisecond'
    UNKNOWN = 'unknown'


def get_format(p: str, fmt_type: str = '') -> str:
    fmt_type_lower = fmt_type.lower().strip()
    if p == Precision.SECOND:
        if fmt_type == '' or fmt_type == 'default':
            return Format.SECONDS
        elif fmt_type_lower == 'rfc3339':
            return Format.SECONDS_RFC3339
    elif p == Precision.MILLISECOND:
        if fmt_type == '' or fmt_type == 'default':
            return Format.MILLISECONDS
        elif fmt_type_lower == 'rfc3339':
            return Format.MILLISECONDS_RFC3339
    else:
        return ''


def from_string(s: str, fmt: str = Format.SECONDS) -> (datetime.datetime, Exception):
    try:
        return datetime.datetime.strptime(s, fmt), None
    except Exception as e:
        return None, e


def from_seconds(secs: int) -> (datetime.datetime, Exception):
    try:
        return datetime.datetime.fromtimestamp(secs), None
    except Exception as e:
        return None, e


def from_milliseconds(msecs: int) -> (datetime.datetime, Exception):
    try:
        return datetime.datetime.fromtimestamp(msecs / 1e3), None
    except Exception as e:
        return None, e


def from_timestamp(ts: int, p: str) -> (datetime.datetime, Exception):
    if p == Precision.SECOND:
        return from_seconds(ts)
    elif p == Precision.MILLISECOND:
        return from_milliseconds(ts)
    else:
        return None, Exception('unknown precision')


def to_string(tm: datetime.datetime, fmt: str = Format.SECONDS) -> (str, Exception):
    try:
        return tm.strftime(fmt), None
    except Exception as e:
        return '', e


def to_seconds(tm: datetime.datetime) -> int:
    return int(tm.timestamp())


def to_milliseconds(tm: datetime.datetime) -> int:
    return int(tm.timestamp() * 1e3)


def to_timestamp(tm: datetime.datetime, p: str) -> (int, Exception):
    if p == Precision.SECOND:
        return to_seconds(tm), None
    elif p == Precision.MILLISECOND:
        return to_milliseconds(tm), None
    else:
        return None, Exception('unknown precision')

def now() -> datetime.datetime:
    return datetime.datetime.now()


def _debug():
    s = '2024-08-28 11:22:33.444'
    tm, e = from_string(s, Format.MILLISECONDS)
    print(tm, e)
    tm_to_s, e = to_string(tm, Format.MILLISECONDS)
    print(tm_to_s, e)
    sec = to_seconds(tm)
    print(sec)
    sec_to_tm, _ = from_seconds(sec)
    print(sec_to_tm)
    msec = to_milliseconds(tm)
    print(msec)
    msec_to_tm, _ = from_milliseconds(msec)
    print(msec_to_tm)


if __name__ == '__main__':
    _debug()
