import pytz
from django.db import models
from datetime import datetime
from django_neomodel import DjangoNode
from neomodel import StructuredNode, StringProperty, DateTimeProperty, UniqueIdProperty, DateProperty, Relationship, \
    RelationshipTo, RelationshipFrom, One, StructuredRel, IntegerProperty, OneOrMore, ZeroOrMore
from .models import *


class title_life(StructuredRel):
    title = StringProperty(unique_index=True,
                          required=True)

class title_owns(StructuredRel):
    title = StringProperty(unique_index=True,
                          required=True)

class Person(DjangoNode):
    uid = UniqueIdProperty()
    name  = StringProperty()
    age = IntegerProperty(index=True,
                          default=0)
    persons = Relationship('Person', "Frends")
    cars = RelationshipTo('Car', 'owns')


    class Meta:
         app_label = 'hodata'


class Car(DjangoNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    number = StringProperty()
    cars = Relationship('Car', None)
    persons = RelationshipFrom('Person', 'owns')
    class Meta:
         app_label = 'hodata'


