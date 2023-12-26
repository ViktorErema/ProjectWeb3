from django.contrib import admin
from .models import *
from django_neomodel import admin as neo_admin

# @admin.register(Document)
# class DocumentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'text',)
#     list_display_links = ('id', 'title',)
#
#
# admin.site.register(Subject)
# admin.site.register(Predicat)
# admin.site.register(Object)
# admin.site.register(Graff)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("uid", "name")
neo_admin.register(Person, PersonAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ("uid", "name")
neo_admin.register(Car, CarAdmin)

