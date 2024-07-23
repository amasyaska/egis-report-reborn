import os
import sys

from django.http import HttpResponse
from django.shortcuts import render

basepath = os.path.dirname(__file__)                            # get absolute path to this file
filepath = os.path.abspath(os.path.join(basepath, "..", ".."))
sys.path.append(filepath)     # to be able to import top-level packages

from . import functions
from XlsxManager import XlsxManager
from TimesheetParser import TimesheetParser

# Create your views here.

def index(request):
    if (request.method == "GET"):
        basepath = os.path.dirname(__file__)                            # get absolute path to this file
        filepath = os.path.abspath(os.path.join(basepath, "templates", "index.html"))
        with open(filepath, 'r') as f:
            return HttpResponse(f.read())
    elif (request.method == "POST"):
        xlsx_files_amount = int(request.POST['xlsx_files_amount'])
        url_list = list()
        for i in range(xlsx_files_amount):
            url_list.append(request.POST[f'xlsx_file_{i}'])
        xlsx_manager = XlsxManager()
        xlsx_filenames_list = list()
        for url in url_list:
            filename = XlsxManager.get_xlsx_file_from_url_google_docs(url)
            basepath = os.path.dirname(__file__)                            # get absolute path to this file
            filepath = os.path.abspath(os.path.join(basepath, "..", "..", "..", "resources", filename))
            xlsx_filenames_list.append(filepath)
        print(f"getting report for {request.POST['project_name']}\nfor: {url_list} and {xlsx_filenames_list}")
        timesheet_parser = TimesheetParser(xlsx_filenames_list)
        timesheet_parser.write_report_to_xlsx_file(timesheet_parser.get_report_by_project_name(request.POST['project_name']), "test_web")


        

def report(request):
    if (request.method == "GET"):
        basepath = os.path.dirname(__file__)                            # get absolute path to this file
        filepath = os.path.abspath(os.path.join(basepath, "templates", "report.html"))
        with open(filepath, 'r') as f:
            return HttpResponse(f.read()) 
