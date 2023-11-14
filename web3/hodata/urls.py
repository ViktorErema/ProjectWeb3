from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import document_list, document_new

urlpatterns = [
    path('', document_list, name='document_list'),
    path('document_list/document_new/', document_new, name='document_new'),
]
