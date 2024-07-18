from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("report", views.report)
]
