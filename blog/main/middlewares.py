import datetime
from time import time

from .logger_service import get_client_ip
from .models import Logger


class LogMiddlware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # before

        st = time()

        _created = str(datetime.datetime.now())
        _path = request.path
        _utm = str(request.GET.get('utm', ''))
        _i_p = get_client_ip(request)
        _time_exec = str(time() - st)
        logger = Logger(created=_created, time_execution=_time_exec, path=_path, utm=_utm, i_p=_i_p)
        logger.save()

        response = self.get_response(request)

        return response
