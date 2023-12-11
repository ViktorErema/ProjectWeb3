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
    # path('', views.person_list, name='person_list'),
    # path('movie_list', views.movie_list, name='movie_list'),
    # path('person_list', views.person_list, name='person_list'),
    # path('persons', views.persons),
    # path('person_edit/<uid>', views.person_update, name='person_edit'),
]
