from django.contrib import admin
from django_neomodel import admin as neo_admin
from .models import *

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text',)
    list_display_links = ('id', 'title',)


admin.site.register(Subject)
admin.site.register(Predicat)
admin.site.register(Object)
admin.site.register(Graff)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ("title", "created")
# neo_admin.register(Book, BookAdmin)
