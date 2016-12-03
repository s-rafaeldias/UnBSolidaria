from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# Tabela de extend do User
class User(AbstractUser):
    cpf = models.CharField(max_length=45, blank=True, null=True)
    cnpj = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    telephone = models.CharField(max_length=45, blank=True, null=True)


# Tabela de Noticias
class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=400, default='')
    texto = models.TextField('texto', max_length=4000)
    dataCadastro = models.DateTimeField('criado em', auto_now_add=True)
    dataNoticia = models.DateTimeField('data da noticia', auto_now_add=False)

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo


# Tabela de FAQ
class FAQ(models.Model):
    pergunta = models.CharField(max_length=400)
    resposta = models.TextField('resposta', max_length=4000)
    dataCadastro = models.DateTimeField('criado em', auto_now_add=True)
    dataPergunta = models.DateTimeField('data da faq', auto_now_add=False)

    def __unicode__(self):
        return self.pergunta

    def __str__(self):
        return self.pergunta
