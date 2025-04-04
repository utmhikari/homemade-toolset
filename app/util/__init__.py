import json
import yaml
from typing import Any, Optional


def json_dump(o: Any, indent: Optional[int] = 2, ensure_ascii: bool = False, **kwargs) -> (str, Exception):
    try:
        return json.dumps(o, indent=indent, ensure_ascii=ensure_ascii, **kwargs), None
    except Exception as e:
        return '', e


def json_load(s: str) -> (Any, Exception):
    try:
        return json.loads(s), None
    except Exception as e:
        return None, e


def json_pretty(s: str) -> str:
    o, e = json_load(s)
    if e is not None:
        return s
    p, e = json_dump(o)
    if e is not None:
        return s
    return p


def yaml_dump(o: Any, indent: Optional[int] = 2, allow_unicode: bool = True, **kwargs) -> (str, Exception):
    try:
        return yaml.safe_dump(o, indent=indent, allow_unicode=allow_unicode, **kwargs), None
    except Exception as e:
        return '', e


def yaml_load(s: str) -> (Any, Exception):
    try:
        return yaml.safe_load(s), None
    except Exception as e:
        return None, e
