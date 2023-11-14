from django.contrib import admin

from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text',)
    list_display_links = ('id', 'title',)


# admin.site.register(Document)
