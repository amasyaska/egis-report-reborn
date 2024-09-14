from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="main"),
    path("report/", views.Report.as_view(), name="report"),
]
