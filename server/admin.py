from django.contrib import admin
from .models import Server, Code
# Register your models here.


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ("server_id", "secret_key")

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ['id', "server_id", "title", 'code_id']