"""This module contains util classes related to web http."""

__author__ = "Srikrishnan Suresh"
__copyright__ = "Copyright 2015, MyCraze"
__version__ = "1.0.1"

from django.http import HttpResponse
from django.utils import simplejson


class JsonResponse(HttpResponse):
    """JSON response class, used to render an HTML response in json format.
    """
    def __init__(self, content, mimetype='application/json', status=None, content_type=None):
        super(JsonResponse, self).__init__(
            content=simplejson.dumps(content),
            mimetype=mimetype,
            status=status,
            content_type=content_type,
        )
