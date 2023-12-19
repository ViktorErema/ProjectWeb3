from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import *

urlpatterns = [
    path('', document_list, name='document_list'),
    path('zapros/', zapros2, name='zapros2'),
    path('document_new/', document_new, name='document_new'),
    path('document_detail/<int:document_pk>', document_detail, name='document_list'),
    path('list_detail/<uid>', list_detail, name='list_detail'),
    path('list_detail_car/<uid>', list_detail_car, name='list_detail_car'),
    path('list_objects/', list_objects, name='list_objects'),
    path('person_update/<uid>', person_update, name='person_update'),
    path('person_new/',person_new, name='person_new'),
    path('car_new/',car_new, name='car_new'),
    path('list_objects/<uid>', person_delete, name='person_delete'),
    path('list_objects_c/<uid>', car_delete, name='car_delete'),

    # path('search/', search, name='search'),
]
