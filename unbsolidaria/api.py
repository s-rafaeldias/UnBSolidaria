from tastypie.resources import ModelResource
from tastypie import fields
from .models import Trabalho, Organizacao

class OrganizacaoResource(ModelResource):
    class Meta:
        queryset = Organizacao.objects.all()
        resource_name = 'organizacao'

class TrabalhoResource(ModelResource):
	organizacao = fields.ForeignKey(OrganizacaoResource, 'organizacao')
    
	class Meta:
		queryset = Trabalho.objects.all()
		resource_name = 'trabalhos'