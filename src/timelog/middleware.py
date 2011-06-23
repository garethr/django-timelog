import time
import logging
from django.utils.encoding import smart_str

logger = logging.getLogger(__name__)


class TimeLogMiddleware(object):

    def process_request(self, request):
        request._start = time.time()

    def process_response(self, request, response):
        # if an exception is occured in a middleware listed
        # before TimeLogMiddleware then request won't have '_start' attribute
        # and the original traceback will be lost (original exception will be
        # replaced with AttributeError)
        if hasattr(request, '_start'):
            d = {'method': request.method,
                 'time': time.time() - request._start,
                 'code': response.status_code,
                 'url': smart_str(request.path_info)}
            msg = '%(method)s "%(url)s" (%(code)s) %(time).2f' % d
            logger.info(msg)
        return response
