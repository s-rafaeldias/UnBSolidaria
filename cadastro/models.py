from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Inscricao(models.Model):
        nome = models.CharField(max_length=100)
        cpf = models.CharField('CPF', max_length=11, unique=True)
        idade = models.IntegerField()
        email = models.EmailField(unique=True)
        telefone = models.CharField(max_length=20, blank=True)
        criado_em = models.DateTimeField('criado em', auto_now_add=True)

        class Meta:
                ordering = ['criado_em']
                verbose_name = (u'nome')
                verbose_name_plural = (u'nomes')

        def __unicode__(self):
                return self.nome

