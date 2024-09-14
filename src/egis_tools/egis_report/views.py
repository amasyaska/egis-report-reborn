import os
import sys

from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views import View

basepath = os.path.dirname(__file__)                            # get absolute path to this file

filepath = os.path.abspath(os.path.join(basepath, "..", ".."))
sys.path.append(filepath)     # to be able to import top-level packages

from . import functions
from XlsxManager import XlsxManager
from TimesheetParser import TimesheetParser

# VIEWS

class Index(View):

    def get(self, request):
        filepath = os.path.abspath(os.path.join(basepath, "templates", "index.html"))
        with open(filepath, 'r') as f:
            return HttpResponse(f.read())

    def post(self, request):
        xlsx_files_amount = int(request.POST['xlsx_files_amount'])
        return redirect(f'/report/?amount={xlsx_files_amount}')


class Report(View):

    def get(self, request):
        amount = request.GET.get("amount", None)
        if (amount.isnumeric() and int(amount) >= 1):    # makes sure that amount parameter is integer and in correct range
            filepath = os.path.abspath(os.path.join(basepath, "templates", "report.html"))
            with open(filepath, 'r') as f:
                return HttpResponse(f.read())
        
        response = HttpResponse()
        response.status_code = 400
        return response



def index(request):
    if (request.method == "GET"):
        basepath = os.path.dirname(__file__)                            # get absolute path to this file
        filepath = os.path.abspath(os.path.join(basepath, "templates", "index.html"))
        with open(filepath, 'r') as f:
            return HttpResponse(f.read())
    elif (request.method == "POST"):
        xlsx_files_amount = int(request.POST['xlsx_files_amount'])
        url_list = list()
        print(f"request.POST: {request.POST}")
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
        filename = "report"
        timesheet_parser.write_report_to_xlsx_file(timesheet_parser.get_report_by_project_name(request.POST['project_name']), filename)
        basepath = os.path.dirname(__file__)                            # get absolute path to this file
        filepath = os.path.abspath(os.path.join(basepath, "..", "..", "..", "resources", "output", f"{filename}.xlsx"))
        # file download
        with open(filepath, "rb") as f:
            response = HttpResponse(f.read(), content_type="application/vnd.ms-excel")
            response["Content-Disposition"] = f"attachment; filename={filename}"
            return response


        

def report(request):
    if (request.method == "GET"):
        basepath = os.path.dirname(__file__)                            # get absolute path to this file
        filepath = os.path.abspath(os.path.join(basepath, "templates", "report.html"))
        with open(filepath, 'r') as f:
            return HttpResponse(f.read()) 
