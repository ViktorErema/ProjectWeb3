from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import document_list, document_new, zapros, document_detail

urlpatterns = [
    path('', document_list, name='document_list'),
    path('', zapros, name='zapros'),
    path('document_new/', document_new, name='document_new'),
    path('document_detail/<int:document_pk>', document_detail, name='document_list'),
]
