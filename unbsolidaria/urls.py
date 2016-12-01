from django.conf.urls import url
from . import views

urlpatterns = [
    # Urls para usuarios nao logados
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^noticias/$', views.noticias, name="noticias"),
    url(r'^contato/$', views.contato, name="contato"),
    url(r'^faq/$', views.faq, name="faq"),
    url(r'^orgposlogin/', views.organizacoes, name="organizacao"),
    url(r'^orgposlogin/', views.organizacao, name="organizacao"),
    url(r'^create/', views.anda_create, name="organizacao"),
    url(r'^(?P<id>\d+)/update/', views.anda_update, name="organizacao"),
    url(r'^(?P<id>\d+)/delete/', views.anda_delete, name="organizacao"),
    # url(r'^login/$', views.login, name="login"),
    # url(r'^signup/$', views.signup, name="signup"),
]
