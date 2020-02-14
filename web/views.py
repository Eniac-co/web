
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



@require_http_methods(["POST"])
def register_coders(request):
    print("i'm in")
    try:
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        skype = request.POST.get('skype')
        coders.objects.create(username=username,phone=phone,email=mail,password=skype)
        data = {
            "username": username,
            "phone":phone,
            "mail":mail,
            "skype":skype,
            "msg":"success",
            "errorNum":0,
        }
        print(data)
    except  Exception as e:
        data = {
            "msg":str(e),
            "coder":[],
            "errorNum":1
        }
        print(data)
    return HttpResponse(json.dumps(data), content_type="application/json")