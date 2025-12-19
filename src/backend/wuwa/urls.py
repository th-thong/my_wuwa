from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('game-account/',include('game_account.urls')),
    path('convene-log/',include('convene_log.urls')),
]