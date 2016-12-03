from __future__ import unicode_literals

from django.db import models

# Create your models here.


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


class Trabalho(models.Model):
    titulo = models.CharField(max_length=45)
    descricao = models.CharField(max_length=240)
    data_inicio = models.DateField(auto_now=False, auto_now_add=False)
    data_fim = models.DateField(auto_now=False, auto_now_add=False)
    vagas = models.IntegerField(default=0)

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo


class Endereco(models.Model):
    descricao = models.CharField(max_length=120)
    cep = models.CharField(max_length=11)

    def __unicode__(self):
        return self.cep

    def __str__(self):
        return self.cep


class Dias(models.Model):
    descricao = models.CharField(max_length=20)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao


class Tags(models.Model):
    descricao = models.CharField(max_length=45)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao
