from django.contrib import admin
from .models import WebAccount

admin.site.register(WebAccount)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')