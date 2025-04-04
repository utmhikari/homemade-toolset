import random
import time
from datetime import datetime
from threading import Thread
from typing import Optional
from concurrent.futures import ProcessPoolExecutor

from PySide6.QtCore import QObject, Signal, QThread

from app.service.logger import LOGGER
from app.service.request import Request, RequestMethod, Response
from app.util import time as timeutil


_REQUEST_POOL = ProcessPoolExecutor(max_workers=3)


def _executor():
    return _REQUEST_POOL


class RequestStartEvent:
    def __init__(self):
        pass

class RequestProgressEvent:
    def __init__(self, seconds: float):
        self.seconds = seconds

class RequestFinishEvent:
    def __init__(self,
                 req: Optional[Request],
                 resp: Optional[Response],
                 err: Optional[Exception],
                 seconds: float):
        self.req = req
        self.resp = resp
        self.err = err
        self.seconds = seconds


class RequestSignals(QObject):
    start = Signal(RequestStartEvent)
    progress = Signal(RequestProgressEvent)
    finish = Signal(RequestFinishEvent)


class RequestWorkerThread(QThread):
    """refer to https://www.cnblogs.com/dnxrzl/p/17096668.html"""
    def __init__(self, req: Request, parent=None):
        QThread.__init__(self, parent)
        self.req = req
        self.signals = RequestSignals()

    def run(self):
        LOGGER.info(f'do request at thread: {str(QThread.currentThread())}')
        req = self.req
        if not isinstance(req, Request):
            evt = RequestFinishEvent(
                req=None,
                resp=None,
                err=ValueError('req must be Request instance'),
                seconds=0
            )
            self.signals.finish.emit(evt)
            return
        validate_err = req.validate()
        if validate_err:
            evt = RequestFinishEvent(
                req=req,
                resp=None,
                err=validate_err,
                seconds=0
            )
            self.signals.finish.emit(evt)
            return
        self.signals.start.emit(RequestStartEvent())

        executor = _executor()
        start_time = timeutil.now()
        future = executor.submit(req.invoke)
        while not future.done():
            cur_time = timeutil.now()
            seconds = (cur_time - start_time).total_seconds()
            evt = RequestProgressEvent(
                seconds=seconds
            )
            self.signals.progress.emit(evt)
            sleep_ms = random.randint(50, 150)
            QThread.msleep(sleep_ms)
        resp, err = future.result()
        end_time = timeutil.now()
        seconds = (end_time - start_time).total_seconds()
        evt = RequestFinishEvent(
            req=req,
            resp=resp,
            err=err,
            seconds=seconds
        )
        self.signals.finish.emit(evt)
