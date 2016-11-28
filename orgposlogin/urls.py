from django.conf.urls import url

from orgposlogin.views import organizacoes, organizacao

urlpatterns = [
    url(r'^orgposlogin/', organizacoes, name="organizacao"),
    url(r'^orgposlogin/', organizacao, name="organizacao"),
]

