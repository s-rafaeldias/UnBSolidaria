from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FAQ(models.Model):
	pergunta = models.CharField(max_length=400)
	resposta = models.TextField('resposta', max_length=4000)
	dataCadastro = models.DateTimeField('criado em', auto_now_add=True)
	dataPergunta = models.DateTimeField('data da faq', auto_now_add=False)

	def __unicode__(self):
		return self.pergunta
