
from web.models import coders,clients
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
# Create your views here.


# noinspection PyInterpreter
@require_http_methods(["GET"])
def get_coders(request):
    try:
        coderObj = coders.objects.all()
        coderList = []
        for coder in coderObj:
            coderList.append({
                "name":coder.username,
                "phone":coder.phone,
            })
        data = {
            "coder": coderList,
            "msg":"success",
            "errorNum":0,
        }
    except  Exception as e:
        data = {
            "msg":str(e),
            "coder":[],
            "errorNum":1
        }
    return HttpResponse(json.dumps(data), content_type="application/json")