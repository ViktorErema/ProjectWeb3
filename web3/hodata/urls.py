from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static
from . views import *

urlpatterns = [

    path('list_detail/<uid>', list_detail, name='list_detail'),
    path('list_detail_car/<uid>', list_detail_car, name='list_detail_car'),
    path('', list_objects, name='list_objects'),
    path('person_update/<uid>', person_update, name='person_update'),
    path('car_update/<uid>', car_update, name='car_update'),
    path('person_new/',person_new, name='person_new'),
    path('car_new/',car_new, name='car_new'),
    path('list_objects/<uid>', person_delete, name='person_delete'),
    path('list_objects_c/<uid>', car_delete, name='car_delete'),
    re_path('', run, name="run"),
    # re_path("vivod/", zapros, name="vivod"),
    # re_path("vivod/", zapros3, name="vivod"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
