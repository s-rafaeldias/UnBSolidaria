from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from .models import Noticia, FAQ, Trabalho
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.views import generic
from .forms import ContactForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core.urlresolvers import reverse


# Create your views here.

class IndexView(generic.ListView):
    template_name = '../templates/index.html'
    context_object_name = {}

    def get_queryset(self):
        return Noticia.objects.all()

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

    return render_to_response('faq/lista.html',{'perguntas':
        perguntas}, context_instance=RequestContext(request))

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

    return render_to_response('noticia/lista.html',{'noticias':
    noticias}, context_instance=RequestContext(request))


class TrabalhosView(generic.ListView):
    template_name = '../templates/trabalhos/listaTrabalhos.html'
    context_object_name = 'lista_trabalhos'
    paginate_by = 2

    def get_queryset(self):
        return Trabalho.objects.all()


class TrabalhoCreate(generic.CreateView):
    template_name = '../templates/trabalhos/criarTrabalho.html'
    model= Trabalho
    fields = ['titulo', 'descricao', 'data_inicio', 'data_fim']
    success_url='/listaTrabalhos'






#    sugeridos_list =selfugeridos.objects.all()
#     andamento_list = Andamento.objects.all()
#     realizados_list = Realizados.objects.all()
#     comentarios_list = Comentarios.objects.all()


#     paginator = Paginator(sugeridos_list, 10
# )
#     paginator1 = Paginator(andamento_list, 10)
#     paginator2 = Paginator(realizados_list, 10)
#     paginator3 = Paginator(comentarios_list, 10)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#     try:
#         sugeridos = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         sugeridos = paginator.page(paginator.num_pages)

#     try:
#         andamento = paginator1.page(page)
#     except (EmptyPage, InvalidPage):
#         andamento = paginator1.page(paginator1.num_pages)

#     try:
#         realizados = paginator2.page(page)
#     except (EmptyPage, InvalidPage):
#         realizados = paginator2.page(paginator2.num_pages)

#     try:
#         comentarios = paginator3.page(page)
#     except (EmptyPage, InvalidPage):
#         comentarios = paginator3.page(paginator3.num_pages)

#     return render_to_response('volposlogin/volposlogin.html',{'sugeridos':
#     sugeridos, 'andamento':andamento, 'realizados':realizados, 'comentarios':comentarios},context_instance=RequestContext(request))

# def voluntario(request):
#     try:
#         sugere_id = int(request.GET.get('sugere', '1'))
#     except ValueError:
#         sugere_id = 0

#     try:
#         anda_id = int(request.GET.get('anda', '1'))
#     except ValueError:
#         anda_id = 0

#     try:
#         realiza_id = int(request.GET.get('realiza', '1'))
#     except ValueError:
#         realiza_id = 0

#     try:
#         comenta_id = int(request.GET.get('comenta', '1'))
#     except ValueError:
#         comenta_id = 0

#     sugere = get_object_or_404(Sugeridos, pk=solicita_id)
#     anda = get_object_or_404(Andamento, pk=anda_id)
#     realiza = get_object_or_404(Realizados, pk=realiza_id)
#     comenta = get_object_or_404(Comentarios, pk=comenta_id)

#     return render_to_response('volposlogin/volposlogin.html',{'sugere':sugere, 'anda':anda, 'realiza':realiza, 'comenta':comenta },context_instance=RequestContext(request))



