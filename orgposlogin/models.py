from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Andamento(models.Model):
        trabalho = models.CharField(max_length=100)
	subtitulo = models.CharField(max_length=100)
        descricao = models.TextField('descricao', max_length=4000)
	image = models.FileField()

        def __unicode__(self):
                return self.andamento


class Realizados(models.Model):
        trabalho = models.CharField(max_length=100)
	subtitulo = models.CharField(max_length=100)
        descricao = models.TextField('descricao', max_length=4000)
	image = models.FileField(null=True, blank=True)

        def __unicode__(self):
                return self.realizados

