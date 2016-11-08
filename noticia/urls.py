from django.conf.urls import url

from noticia.views import (noticias, noticia)

urlpatterns = [
    url(r'^noticias/', noticias, name="noticias"),
    url(r'^noticias/noticia/(?P<pk>\d+)$', noticia, name="noticia"),
]
