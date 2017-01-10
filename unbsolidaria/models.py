from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# Tabela de extend do User
class User(AbstractUser):
    descricao = models.CharField(max_length=45, blank=True, null=True)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.IntegerField( default=2 )

class Organizacao(models.Model):
    cnpj = models.CharField(max_length=45, blank=True, null=True)
    organizacao_fk = models.IntegerField( default=-1 )

class Voluntario(models.Model):
    GENRE_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )

    cpf = models.CharField(max_length=45, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True, choices=GENRE_CHOICES)
    voluntario_fk = models.IntegerField( default=-1 )

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


class Dia(models.Model):
    descricao = models.CharField(max_length=20)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao


class Trabalho(models.Model):
    titulo = models.CharField(max_length=45)
    descricao = models.TextField(max_length=140)
    autor = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True)
    data_inicio = models.DateField(auto_now=False, auto_now_add=False)
    data_fim = models.DateField(auto_now=False, auto_now_add=False)
    vagas = models.PositiveIntegerField(default=0)
    dias = models.ManyToManyField(Dia)
    organizacao = models.ForeignKey(User, related_name="dono")
    voluntarios = models.ManyToManyField(User, through='UsuarioTrabalho', through_fields=('trabalho', 'voluntario'))

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo


class Endereco(models.Model):
    endereco = models.CharField(max_length=120)
    cep = models.CharField(max_length=11)
    usuario_fk = models.IntegerField( default=-1 )

    def __unicode__(self):
        return self.cep

    def __str__(self):
        return self.cep


class Tag(models.Model):
    descricao = models.CharField(max_length=45)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

class UsuarioTrabalho(models.Model):
    organizacao = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizacao')
    voluntario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='voluntario')
    trabalho = models.ForeignKey(Trabalho, on_delete=models.CASCADE)
