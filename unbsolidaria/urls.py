from django.conf.urls import url
from . import views

urlpatterns = [
    # Urls para usuarios nao logados
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^noticias/$', views.noticias, name="noticias"),
    url(r'^contato/$', views.contato, name="contato"),
    url(r'^faq/$', views.faq, name="faq"),

    # Urls para usuarios logados como Organizacao
    url(r'^listaTrabalhos/$', views.TrabalhosView.as_view(), name="lista-trabalhos"),
    url(r'^criarTrabalho/$', views.TrabalhoCreate.as_view(), name="criar-trabalho"),
    url(r'^editarTrabalho/(?P<pk>\d+)/$', views.TrabalhoUpdate.as_view(), name="editar-trabalho"),
    url(r'^deletarTrabalho/(?P<pk>\d+)/$', views.TrabalhoDelete.as_view(), name="deletar-trabalho"),
    url(r'^visualizarTrabalho/(?P<pk>\d+)/$', views.TrabalhoDetailView.as_view(), name='visualizar-trabalho'),
    # Urls para usuarios logados como Voluntarios
   
]


