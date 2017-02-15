from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('title','name')
    search_fields = ('title','name')

@admin.register(UserPermission)
class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'permission')
    search_fields = ('title', 'permission')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'permission')
    search_fields = ('title', 'permission')


