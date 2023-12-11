import pytz
from django.db import models
from datetime import datetime
from django_neomodel import DjangoNode
from neomodel import StructuredNode, StringProperty, DateTimeProperty, UniqueIdProperty, DateProperty, Relationship, \
    RelationshipTo, RelationshipFrom, One, StructuredRel, IntegerProperty, OneOrMore
from .models import *


# Create your models here.
class Document (models.Model):

    title = models.CharField(max_length=150, verbose_name='Имя документа')
    text = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'


class Subject (models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'

class Predicat (models.Model):

    name = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.name}'

class Object (models.Model):

    name = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.name}'

class Graff (models.Model):

    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    predicat = models.ForeignKey(Predicat, on_delete = models.CASCADE)
    object = models.ForeignKey(Object, on_delete = models.CASCADE)
    connected = models.ForeignKey('self', on_delete = models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return f'{self.subject} {self.predicat} {self.object}'



class SupplierRel(StructuredRel):
    since = DateTimeProperty(default=datetime.now)


class Supplier(DjangoNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    delivery_cost = IntegerProperty()
    coffees = RelationshipTo('Coffee', 'SUPPLIES')
    class Meta:
        app_label = 'hodata'

class Coffee(DjangoNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    nameSupplier = StringProperty(unique_index=True)
    price = IntegerProperty()
    suppliers = RelationshipFrom(Supplier, 'SUPPLIES', model=SupplierRel)

    class Meta:
        app_label = 'hodata'




class Address(StructuredNode):
    sourceID       = StringProperty()
    country_codes  = StringProperty()
    valid_until    = StringProperty()
    address        = StringProperty()
    countries      = StringProperty()
    node_id        = StringProperty(index = True)


class Entity(StructuredNode):
    sourceID                           = StringProperty()
    address                            = StringProperty()
    jurisdiction                       = StringProperty()
    service_provider                   = StringProperty()
    countries                          = StringProperty()
    jurisdiction_description           = StringProperty()
    valid_until                        = StringProperty()
    ibcRUC                             = StringProperty()
    name                               = StringProperty()
    country_codes                      = StringProperty()
    incorporation_date                 = StringProperty()
    node_id                            = StringProperty(index = True)
    status                             = StringProperty()
    officers = RelationshipFrom('.officer.Officer', 'OFFICER_OF')
    intermediaries = RelationshipFrom('.intermediary.Intermediary', 'INTERMEDIARY_OF')
    addresses = RelationshipTo('.address.Address', 'REGISTERED_ADDRESS')
    others = RelationshipFrom('.other.Other', 'CONNECTED_TO')
    entities = Relationship('.entity.Entity', None)
class Intermediary(StructuredNode):
    sourceID      = StringProperty()
    valid_until   = StringProperty()
    name          = StringProperty()
    country_codes = StringProperty()
    countries     = StringProperty()
    node_id       = StringProperty(index = True)
    status        = StringProperty()
    entities      = RelationshipTo('Entity', 'INTERMEDIARY_OF')
    addresses     = RelationshipTo('Address', 'REGISTERED_ADDRESS')
    officers      = Relationship('Officer', None)


class Officer(StructuredNode):
    sourceID      = StringProperty()
    name          = StringProperty()
    country_codes = StringProperty()
    valid_until   = StringProperty()
    countries     = StringProperty()
    node_id       = StringProperty(index = True)
    addresses     = RelationshipTo('Address', 'REGISTERED_ADDRESS')
    entities      = RelationshipTo('Entity', 'OFFICER_OF')
    officers      = Relationship('Officer', None)

class Other(StructuredNode):
    sourceID    = StringProperty()
    name        = StringProperty()
    valid_until = StringProperty()
    node_id     = StringProperty(index = True)
    countries   = StringProperty()
    addresses   = RelationshipTo('Address', 'REGISTERED_ADDRESS')
    officers    = Relationship('Officer', None)
    entities    = Relationship('Entity', None)


class PersonLivesInCity(StructuredRel):
    some_num = IntegerProperty(index=True,
                               default=12)

class CountryOfOrigin(StructuredNode):
    code = StringProperty(unique_index=True,
                          required=True)

class CityOfResidence(StructuredNode):
    name = StringProperty(required=True)
    country = RelationshipTo(CountryOfOrigin,
                             'FROM_COUNTRY')

class PersonOfInterest(DjangoNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True,
                          default=0)

    country = RelationshipTo(CountryOfOrigin,
                             'IS_FROM')
    city = RelationshipTo(CityOfResidence,
                          'Живет',
                          model=PersonLivesInCity)

    class Meta:
        app_label = 'hodata'