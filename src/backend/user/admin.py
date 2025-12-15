from django.contrib import admin
from .models import User

@admin.register(User)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    readonly_fields = ('id',)
    fieldsets = (
        (None, {'fields': ('id', 'username', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )