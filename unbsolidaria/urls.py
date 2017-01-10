from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Urls para usuarios nao logados 
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^noticias/$', views.noticias, name="noticias"),
    url(r'^noticias/(?P<pk>\d+)$', views.DetailsNoticia.as_view(), name='leiamais'),
    url(r'^contato/$', views.contato, name="contato"),
    url(r'^faq/$', views.faq, name="faq"),
    url(r'^get_user/$', views.get_user, name="get_user"),
    url(r'^set_user/$', views.set_user, name="set_user"),

    url(r'^listaTrabalhos/$', views.TrabalhosView.as_view(), name="lista-trabalhos"),
    url(r'^meusTrabalhos/$', views.MeusTrabalhosView.as_view(), name="meus-trabalhos"),
    url(r'^criarTrabalho/$', views.TrabalhoCreate.as_view(success_url='../../'), name="criar-trabalho"),
    url(r'^editarTrabalho/(?P<pk>\d+)/$', views.TrabalhoUpdate.as_view(), name="editar-trabalho"),
    url(r'^deletarTrabalho/(?P<pk>\d+)/$', views.TrabalhoDelete.as_view(), name="deletar-trabalho"),
    url(r'^visualizarTrabalho/(?P<pk>\d+)/$', views.TrabalhoDetailView.as_view(), name='visualizar-trabalho'),

    url(r'^entrarTrabalho/(?P<pk>\d+)/$', views.TrabalhoUsuarioCreate.as_view(), name='entrar-trabalho'),
    url(r'^listaVoluntarios/(?P<pk>\d+)/$', views.TrabalhoUsuarioView.as_view(), name='lista-voluntarios'),
    url(r'^contribuicaoTrabalhos/$', views.ContribuicaoTrabalhosView, name="contribuicao-trabalhos"),

    url(r'^perfil/(?P<pk>\d+)/$', views.PerfilUsuarioView.as_view(), name='perfil-usuario'),
    url(r'^registrar/Organizacao/$', views.OrganizacaoFormView.as_view(), name='registrar-organizacao'),
    url(r'^registrar/Voluntario/$', views.VoluntarioFormView.as_view(), name='registrar-voluntario'),
    url(r'^user/edit/$', views.UserUpdate.as_view(success_url='../../'), name='user-update'),
    url(r'^user/delete/$', views.UserDelete.as_view(success_url='../../'), name='user-delete'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '../'}, name='logout'),

    url(r'^filtros$', views.filters),
    url(r'^filtros/user$', views.user_filters),
    url(r'^filtros/trab$', views.trabalho_filters),
    url(r'^filtros/trab_user$', views.trab_user_filters),
]
