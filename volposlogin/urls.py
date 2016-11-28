from django.conf.urls import url

from volposlogin.views import voluntarios,voluntario

urlpatterns = [
    url(r'^volposlogin/', voluntarios, name="voluntario"),
    url(r'^volposlogin/', voluntario, name="voluntario"),
]

