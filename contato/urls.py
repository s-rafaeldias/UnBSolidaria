from django.conf.urls import url

from contato.views import (contato)

urlpatterns = [
    url(r'^contato/', contato, name="contato"),
]
