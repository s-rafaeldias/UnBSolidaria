from django.conf.urls import url

from trabespecifico.views import (trabespecifico)

urlpatterns = [
    url(r'^trabespecifico/', trabespecifico, name="trabespecifico"),
]
