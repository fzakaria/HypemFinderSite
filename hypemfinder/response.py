from django.core.serializers import json, serialize
from django.http import HttpResponse
from collections import Iterable


class JsonResponse(HttpResponse):
    """Very basic response object. Expects the object to be either a Iterable
    Set of Models, a QuerySet or a single Model Instance"""
    def __init__(self, object):
        if isinstance(object, Iterable):
            content = serialize('json',object, ensure_ascii=False,)
        else:
            content = serialize('json', [object,], ensure_ascii=False)
        super(JsonResponse, self).__init__(content, content_type="application/json")


