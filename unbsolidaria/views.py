from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from .forms import UserForm
from django.views.generic import View
from noticia.models import Noticia

# Create your views here.


class IndexView(generic.ListView):
    template_name = '../templates/index.html'
    context_object_name = 'all_noticias'

    def get_queryset(self):
        return Noticia.objects.all()

class UserFromView(View):
    form_class = UserForm
    template_name = '../templates/registration_form.html'

    #mostrar um form em branco
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #processar informacoes
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)#cria um objeto, porem n coloca no banco ainda

            #normaliza
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returna objeto se esta tudo certo com as credenciais
            user = authenticate(username = username, password = password)

            if user is not None:

                if user.is_active:# analisa se o usuario esta ativo, ou seja, n esta banido nem nada
                    login(request, user)
                    return redirect('../')

        return render(request, self.template_name, {'form': form})#se o usuario nao for valido, returna ele pro formulario de novo