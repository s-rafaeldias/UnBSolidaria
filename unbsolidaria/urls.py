from django.conf.urls import url

from . import views

urlpatterns = [
    # Urls para usuarios nao logados
    url(r'^$', views.IndexView.as_view(), name="index"),
    # url(r'^/noticias/$', noticias, name="noticias"),
    # url(r'^/contato/$', contato, name="contato"),
    # url(r'^/faq/$', faq, name="faq"),
    # url(r'^/login/$', login, name="login"),
    # url(r'^/signup/$', signup, name="signup"),
]