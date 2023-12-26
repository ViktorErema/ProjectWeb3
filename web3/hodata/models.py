import pytz
from django.db import models
from datetime import datetime
from django_neomodel import DjangoNode
from neomodel import StructuredNode, StringProperty, DateTimeProperty, UniqueIdProperty, DateProperty, Relationship, \
    RelationshipTo, RelationshipFrom, One, StructuredRel, IntegerProperty, OneOrMore, ZeroOrMore
from .models import *
from py2neo import Graph, Node

# class Document (models.Model):
#
#     title = models.CharField(max_length=150, verbose_name='Имя документа')
#     text = models.TextField(verbose_name='Описание')
#
#
# class Subject (models.Model):
#
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return f'{self.name}'
#
# class Predicat (models.Model):
#
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return f'{self.name}'
#
# class Object (models.Model):
#
#     name = models.CharField(max_length=150)
#     def __str__(self):
#         return f'{self.name}'
#
# class Graff (models.Model):
#
#     subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
#     predicat = models.ForeignKey(Predicat, on_delete = models.CASCADE)
#     object = models.ForeignKey(Object, on_delete = models.CASCADE)
#     connected = models.ForeignKey('self', on_delete = models.SET_NULL, null = True, blank = True)
#
#     def __str__(self):
#         return f'{self.subject} {self.predicat} {self.object}'


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


