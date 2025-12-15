from django.contrib import admin
from .models import GameAccount

admin.site.register(GameAccount)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id','uid', 'oauth_code')
    search_fields = ('uid')
    readonly_fields = ('id')
    fieldsets = (
        (None, {'fields': ('id','uid', 'oauth_code')}),
    )