from django.shortcuts import render
import requests
from django.http import *
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .countries import countries


def index(request):
    return render(request, 'hello_world.html')


def getOrigin(request, address):
    geoCodingUrl = 'http://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': address}

    response = requests.get(geoCodingUrl, params=params)
    res = response.json()["results"][0]
    res["status_code"] = 200
    #return HttpResponse(json.dumps(res), content_type='application/json')
    return render(request, 'client.html', {"res": res})


@api_view(['GET', 'POST'])
def getCountryName(request):
    """
    API endpoint that allows users to be viewed or edited.
    """
    print(request)
    print(request.body)
    print(request.GET)
    print(request.META)
    if request.method == "GET":
        if "code" in request.GET:
            code = request.GET["code"]
            for k in countries:
                if k["code"] == code:
                    return HttpResponse(json.dumps(k), content_type='application/json')
        else:
            return HttpResponse(json.dumps({"error":"Send me a code"}), content_type='application/json')
    elif request.method == "POST":
        return HttpResponse(json.dumps({}), content_type='application/json')

            


