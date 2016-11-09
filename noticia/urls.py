from django.conf.urls import url

from noticia.views import (noticias, noticia)

urlpatterns = [
    url(r'^noticias/', noticias, name="noticia"),
    url(r'^noticia/', noticia, name="noticia"),
]
