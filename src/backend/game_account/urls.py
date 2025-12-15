from rest_framework.urls import path
from . import views

urlpatterns = [
    path('', views.GameAccountView.as_view(), name='game-account'),
]