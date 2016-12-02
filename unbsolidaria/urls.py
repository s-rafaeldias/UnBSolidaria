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

    # Urls para usuarios logados como Voluntarios

]
