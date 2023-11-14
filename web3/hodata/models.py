from django.db import models

# Create your models here.
class Document (models.Model):

    title = models.CharField(max_length=150, verbose_name='Имя документа')
    text = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'