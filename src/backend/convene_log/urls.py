from rest_framework.urls import path
from . import views

urlpatterns=[
    path('add/',views.ConveneLogView.as_view(), name="add-convene-log")
]