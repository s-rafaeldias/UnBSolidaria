from django.conf.urls import url

from .views import (index)

urlpatterns = [
    # Urls para usuários não logados
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^/noticias/$', index, name="noticias"),
    url(r'^/contato/$', index, name="contato"),
    url(r'^/faq/$', index, name="faq"),
    url(r'^/login/$', index, name="login"),
    url(r'^/signup/$', index, name="signup"),
]