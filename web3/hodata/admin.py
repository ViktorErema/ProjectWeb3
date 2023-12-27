from django.contrib import admin
from .models import *
from django_neomodel import admin as neo_admin


class PersonAdmin(admin.ModelAdmin):
    list_display = ("uid", "name")
neo_admin.register(Person, PersonAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ("uid", "name")
neo_admin.register(Car, CarAdmin)

