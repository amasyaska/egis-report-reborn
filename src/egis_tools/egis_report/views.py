import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    if (request.method == "GET"):
        basepath = os.path.dirname(__file__)                            # get absolute path to this file
        filepath = os.path.abspath(os.path.join(basepath, "templates", "index.html"))
        with open(filepath, 'r') as f:
            return HttpResponse(f.read())
    elif (request.method == "POST"):
        response = HttpResponse(status=200)
        response["Location"] = "report/"
        return response

def report(request):
    if (request.method == "GET"):
        basepath = os.path.dirname(__file__)                            # get absolute path to this file
        filepath = os.path.abspath(os.path.join(basepath, "templates", "report.html"))
        with open(filepath, 'r') as f:
            return HttpResponse(f.read())       
