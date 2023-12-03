from django.db import models
from datetime import datetime
from django_neomodel import DjangoNode
from neomodel import StructuredNode, StringProperty, DateTimeProperty, UniqueIdProperty

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


# class Book(DjangoNode):
#     uid = UniqueIdProperty()
#     title = StringProperty(unique_index=True)
#     status = StringProperty(choices=(
#             ('Available', 'A'),
#             ('On loan', 'L'),
#             ('Damaged', 'D'),
#         ), default='Available')
#     created = DateTimeProperty(default=datetime.utcnow)
#
#     class Meta:
#         app_label = 'library'
