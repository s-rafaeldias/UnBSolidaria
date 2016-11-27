from django.conf.urls import url
from orgposlogin.views import organizacoes, organizacao, anda_create, anda_update,anda_delete



urlpatterns = [

    url(r'^orgposlogin/', organizacoes, name="organizacao"),
    url(r'^orgposlogin/', organizacao, name="organizacao"),
    url(r'^create/', anda_create, name="organizacao"),
    url(r'^(?P<id>\d+)/update/', anda_update, name="organizacao"),
    url(r'^(?P<id>\d+)/delete/', anda_delete, name="organizacao"),
]

