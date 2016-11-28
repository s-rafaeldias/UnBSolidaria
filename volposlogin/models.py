from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Sugeridos(models.Model):
        organizacao = models.CharField(max_length=100)
	trabalho = models.CharField(max_length=100)
        descricao = models.TextField('descricao', max_length=4000)
	image = models.CharField(max_length=400)

        def __unicode__(self):
                return self.solicitacao

class Andamento(models.Model):
        organizacao = models.CharField(max_length=100)
	trabalho = models.CharField(max_length=100)
        descricao = models.TextField('descricao', max_length=4000)
	image = models.CharField(max_length=400)

        def __unicode__(self):
                return self.andamento


class Realizados(models.Model):
        organizacao = models.CharField(max_length=100)
	trabalho = models.CharField(max_length=100)
        descricao = models.TextField('descricao', max_length=4000)
	image = models.CharField(max_length=400)
	
        def __unicode__(self):
                return self.realizados

class Comentarios(models.Model):
        tipo = models.CharField(max_length=100)
	nome = models.CharField(max_length=100)
        comentario = models.TextField('comentario', max_length=4000)
	image = models.CharField(max_length=400)
	realizados = models.IntegerField()

        def __unicode__(self):
                return self.realizados

