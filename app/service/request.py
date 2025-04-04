import time
from typing import Optional, Dict

import curlify
import requests


class Response:
    def __init__(self,
                 status_code: int = 200,
                 headers: Optional[Dict[str, str]] = None,
                 body: str = None):
        self.status_code = status_code
        self.headers = headers if isinstance(headers, dict) else {}
        self.body = body

    @classmethod
    def from_response(cls, resp: requests.Response):
        status_code = resp.status_code
        headers = dict(resp.headers)
        body = resp.text
        return cls(status_code, headers, body)


class RequestMethod:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'


def _default_request_headers():
    return {
        'Content-Type': 'application/json',
    }


_MIN_TIMEOUT = 1000
_DEFAULT_TIMEOUT = 5000
_MAX_TIMEOUT = 120000


def _fixed_timeout(timeout: int) -> int:
    if not isinstance(timeout, int):
        return _DEFAULT_TIMEOUT
    if timeout < _MIN_TIMEOUT:
        timeout = _MIN_TIMEOUT
    if timeout > _MAX_TIMEOUT:
        timeout = _MAX_TIMEOUT
    return timeout


class RequestSettings:
    def __init__(self, connect_timeout: int = _DEFAULT_TIMEOUT, read_timeout: int = _DEFAULT_TIMEOUT):
        self.connect_timeout = _fixed_timeout(connect_timeout)
        self.read_timeout = _fixed_timeout(read_timeout)

    def __str__(self):
        return str(self.__dict__)

    def connect_timeout_seconds(self):
        return _fixed_timeout(self.connect_timeout) / 1000

    def read_timeout_seconds(self):
        return _fixed_timeout(self.read_timeout) / 1000


class Request:
    def __init__(self,
                 url: str = '',
                 method: str = RequestMethod.GET,
                 headers: Optional[Dict[str, str]] = None,
                 body: str = '',
                 settings: Optional[RequestSettings] = None):
        self.url = url
        self.method = method
        self.headers = headers if isinstance(headers, dict) else _default_request_headers()
        self.body = body
        self.settings = settings if isinstance(settings, RequestSettings) else RequestSettings()

    def validate(self):
        if not self.url:
            return ValueError('url is required')
        if not self.method:
            return ValueError('method is required')
        return None

    def args(self):
        return {
            'method': self.method,
            'url': self.url,
            'headers': self.headers,
            'data': self.body.strip(),
            'timeout': (
                self.settings.connect_timeout_seconds(),
                self.settings.read_timeout_seconds()
            )
        }

    def invoke(self) -> (Response, Exception):
        try:
            resp = requests.request(**self.args())
            return Response.from_response(resp), None
        except Exception as e:
            return None, e

    def to_curl(self) -> (str, Exception):
        try:
            prepared_request = requests.PreparedRequest()
            prepared_request.prepare_method(self.method)
            prepared_request.prepare_url(self.url, None)
            prepared_request.prepare_headers(self.headers)
            prepared_request.prepare_body(self.body.strip(), None)
            return curlify.to_curl(prepared_request), None
        except Exception as e:
            return '', e


def _debug():
    req = Request(
        url='https://utmhikari.top/sitemap.xml',
        method=RequestMethod.GET,
        body='1234567'
    )
    print(req.to_curl())
    print(f'request args: {req.args()}')
    resp, err = req.invoke()
    if err:
        print(f'request error: {err}')
    else:
        print(f'response status code: {resp.status_code}, headers: {resp.headers}, body: {resp.body}')



if __name__ == '__main__':
    _debug()
