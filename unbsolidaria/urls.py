from django.conf.urls import url
from . import views

<<<<<<< HEAD

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFromView.as_view(), name='register'),
]

=======
from . import views

urlpatterns = [
    # Urls para usuarios nao logados
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^noticias/$', views.noticias, name="noticias"),
    url(r'^contato/$', views.contato, name="contato"),
    url(r'^faq/$', views.faq, name="faq"),
    # url(r'^login/$', views.login, name="login"),
    # url(r'^signup/$', views.signup, name="signup"),
]
>>>>>>> 9094f0b0dd74f572e4cf0fff7705c2e393cae616
