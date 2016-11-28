from django.conf.urls import url

from cadastro.views import (cadastro)

urlpatterns = [
    url(r'^cadastro/', cadastro, name="cadastro"),
]
