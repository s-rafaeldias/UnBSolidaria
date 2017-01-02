from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from .models import Noticia, FAQ, Trabalho, User, Organizacao, Voluntario
from django.core.mail import send_mail
from django.http import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from .models import Noticia, FAQ,  UsuarioTrabalho
from django.template import RequestContext
from django.views import generic
from .forms import ContactForm, UserForm, OrganizacaoForm, VoluntarioForm
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core.urlresolvers import reverse_lazy
import django_filters

# Create your views here.


class IndexView(generic.ListView):
    template_name = '../templates/index.html'
    context_object_name = {}

    def get_queryset(self):
        return Noticia.objects.all()


class OrganizacaoFormView(View):
    form_class = UserForm
    org_form_class = OrganizacaoForm
    template_name = '../templates/cadastro/organizacao_form.html'    

    # mostrar um form em branco
    def get(self, request):
        form = self.form_class(None)
        form_org = self.org_form_class(None)

        return render(request, self.template_name, {'form': form, 'form_org': form_org})

    # processar informacoes
    def post(self, request):
        form = self.form_class(request.POST)
        org_form = self.org_form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # cria um objeto, porem n coloca no banco ainda

            # normaliza
            user.type = 1
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            if org_form.is_valid():
                org_user = org_form.save(commit=False)  # cria um objeto, porem n coloca no banco ainda
                org_user.organizacao_fk = user.id
                org_user.save()

            # returna objeto se esta tudo certo com as credenciais
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:  # analisa se o usuario esta ativo, ou seja, n esta banido nem nada
                    login(request, user)
                    return redirect('../../')

        return render(request, self.template_name, {'form': form, 'org_form': org_form})  # se o usuario nao for valido, returna ele pro formulario de novo

class VoluntarioFormView(View):
    form_class = UserForm
    vol_form_class = VoluntarioForm
    template_name = '../templates/cadastro/voluntario_form.html'

    # mostrar um form em branco
    def get(self, request):
        form = self.form_class(None)
        form_vol = self.vol_form_class(None)

        return render(request, self.template_name, {'form': form, 'form_vol': form_vol})

     # processar informacoes
    def post(self, request):
        form = self.form_class(request.POST)
        vol_form = self.vol_form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False )  # cria um objeto, porem n coloca no banco ainda
            # normaliza
            user.type = 0
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if vol_form.is_valid():
                vol_user = vol_form.save(commit=False)  # cria um objeto, porem n coloca no banco ainda
                vol_user.voluntario_fk = user.id
                vol_user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:  # analisa se o usuario esta ativo, ou seja, n esta banido nem nada
                    login(request, user)
                    return redirect('../../')

        return render(request, self.template_name, {'form': form, 'vol_form': vol_form})  # se o usuario nao for valido, returna ele pro formulario de novo


class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'cpf', 'cnpj', 'telephone', 'type',
              'gender', 'description']

    def get_object(self, queryset=None):
        return self.request.user


class UserDelete(LoginRequiredMixin, generic.DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = '../templates/trabalhos/deletarTrabalho.html'
    model = User
    success_url = reverse_lazy('../')

    def get_object(self, queryset=None):
        return self.request.user


def contato(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          ['rafaeltbt@gmail.com'])
                form = ContactForm()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return render_to_response("contato/contato.html", {'form': form,
                                                           'mensagem': 'Email enviado com sucesso!'},
                                  context_instance=RequestContext(request))
    return render(request, "contato/contato.html", {'form': form})


def faq(request):
    faq_list = FAQ.objects.all()
    paginator = Paginator(faq_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        perguntas = paginator.page(page)
    except (EmptyPage, InvalidPage):
        perguntas = paginator.page(paginator.num_pages)

    return render_to_response('faq/lista.html', {'perguntas': perguntas}, context_instance=RequestContext(request))


class DetailsNoticia(generic.DeleteView):
    model = Noticia
    template_name = 'noticia/noticia.html'


def noticias(request):
    noticias_list = Noticia.objects.all()
    paginator = Paginator(noticias_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        noticias = paginator.page(page)
    except (EmptyPage, InvalidPage):
        noticias = paginator.page(paginator.num_pages)

    return render_to_response('noticia/lista.html', {'noticias': noticias}, context_instance=RequestContext(request))


#######################################################################################
class TrabalhosView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = '../templates/trabalhos/listaTrabalhos.html'
    context_object_name = 'lista_trabalhos'
    paginate_by = 5	

    def get_queryset(self):
        return Trabalho.objects.all()


class MeusTrabalhosView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = '../templates/trabalhos/meusTrabalhos.html'
    context_object_name = 'lista_trabalhos'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if self.request.user.type == 1:
            return super(MeusTrabalhosView, self).get(request, *args, **kwargs)
        else:
            return redirect('/listaTrabalhos')

    def get_queryset(self):
        return Trabalho.objects.all()



def ContribuicaoTrabalhosView(request):
        return render_to_response('trabalhos/contribuicaoTrabalhos.html', {'contribuicao_trabalhos': UsuarioTrabalho.objects.all(), 'lista_trabalhos': Trabalho.objects.all() }, context_instance=RequestContext(request))


class TrabalhoCreate(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = '../templates/trabalhos/criarTrabalho.html'
    model = Trabalho
    fields = ['titulo', 'descricao', 'vagas', 'data_inicio', 'data_fim', 'organizacao']
    success_url = '/listaTrabalhos'

    def get(self, request, *args, **kwargs):
        if self.request.user.type == 1:
            return super(TrabalhoCreate, self).get(request, *args, **kwargs)
        else:
            return redirect('/listaTrabalhos')


class TrabalhoUpdate(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = '../templates/trabalhos/editarTrabalho.html'
    model = Trabalho
    fields = ['titulo', 'descricao', 'vagas', 'data_inicio', 'data_fim']
    success_url = '/listaTrabalhos'

    def get(self, request, *args, **kwargs):
        if self.request.user.type == 1:
            return super(TrabalhoUpdate, self).get(request, *args, **kwargs)
        else:
            return redirect('/listaTrabalhos')


class TrabalhoDelete(LoginRequiredMixin, generic.DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = '../templates/trabalhos/deletarTrabalho.html'
    model = Trabalho
    success_url = reverse_lazy('lista-trabalhos')

    def get(self, request, *args, **kwargs):
        if self.request.user.type == 1:
            return super(TrabalhoDelete, self).get(request, *args, **kwargs)
        else:
            return redirect('/listaTrabalhos')


class TrabalhoDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = '../templates/trabalhos/visualizarTrabalho.html'
    model = Trabalho

    def get_context_data(self, **kwargs):
        context = super(TrabalhoDetailView, self).get_context_data(**kwargs)
        return context


#######################################################################################
class TrabalhoUsuarioCreate(generic.CreateView):
    template_name = '../templates/trabalhoUsuario/new.html'
    model = UsuarioTrabalho
    fields = ['organizacao', 'trabalho', 'voluntario']
    success_url = reverse_lazy('lista-trabalhos')

    def get_context_data(self, **kwargs):
        context = super(TrabalhoUsuarioCreate, self).get_context_data(**kwargs)
        teste = self.kwargs['pk']
        context['trabalho'] = Trabalho.objects.get(pk=teste)
        return context


class TrabalhoUsuarioUpdate(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = '../templates/trabalhoUsuario/update.html'
    model = UsuarioTrabalho
    fields = ['organizacao', 'trabalho', 'voluntario']
    success_url='/listaTrabalhos'


class TrabalhoUsuarioDelete(LoginRequiredMixin, generic.DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = '../templates/trabalhoUsuario/delete.html'
    model = UsuarioTrabalho
    success_url = reverse_lazy('lista-trabalhos')


class TrabalhoUsuarioView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = '../templates/trabalhoUsuario/list.html'
    context_object_name = 'lista_voluntarios'
    paginate_by = 5

    def get_queryset(self):
        teste = self.kwargs['pk']
        print teste
        return UsuarioTrabalho.objects.all().filter(trabalho_id=teste)

######################################################################################################

# class UserFilter(django_filters.FilterSet):
#     class Meta:
#         model = User
#         fields = {
#             'gender': ['exact'],
#             'type': ['exact'],
#             'last_login': ['gt'],
#             'date_joined': ['gt'],                        
#         }

# class TrabalhoFilter(django_filters.FilterSet):
#     class Meta:
#         model = Trabalho
#         fields = {
#             'vagas': ['exact'],
#             'organizacao': ['exact'],
#             'data_inicio': ['exact'],
#             'data_fim': ['exact'],
#         }

# class UsuarioTrabalhoFilter(django_filters.FilterSet):
#     class Meta:
#         model = UsuarioTrabalho
#         fields = {
#             'organizacao': ['exact'],
#             'trabalho': ['exact'],
#             'voluntario': ['exact'],
#         }

# def filters(request):
#     # f = UserFilter(request.GET, queryset=User.objects.all())
#     return render(request, 'filtros/filter.html')

# def user_filters(request):
#     f = UserFilter(request.GET, queryset=User.objects.all())
#     # f = UserFilter(request.GET, queryset=User.objects.all())
#     return render(request, 'filtros/user.html', {'filter': f})

# def trab_user_filters(request):
#     f = UsuarioTrabalhoFilter(request.GET, queryset=UsuarioTrabalho.objects.all())
#     # f = UserFilter(request.GET, queryset=User.objects.all())
#     return render(request, 'filtros/trab_user.html', {'filter': f})

# def trabalho_filters(request):
#     g = TrabalhoFilter(request.GET, queryset=Trabalho.objects.all())
#     # f = UserFilter(request.GET, queryset=User.objects.all())
#     return render(request, 'filtros/trab.html', {'filter': g})

from rest_framework import viewsets
from unbsolidaria.serializers import UserSerializer, TrabalhoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class TrabalhoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Trabalho.objects.all().order_by('-date_joined')
    serializer_class = TrabalhoSerializer