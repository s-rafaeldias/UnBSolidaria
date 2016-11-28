from django.shortcuts import render_to_response
from orgposlogin.models import Solicitacao
from orgposlogin.models import Andamento
from orgposlogin.models import Realizados
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.


def organizacoes(request):
    solicitacao_list = Solicitacao.objects.all()
    andamento_list = Andamento.objects.all()
    realizados_list = Realizados.objects.all()

    paginator = Paginator(solicitacao_list, 3)
    paginator1 = Paginator(andamento_list, 3)
    paginator2 = Paginator(realizados_list, 3)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        solicitacao = paginator.page(page)
    except (EmptyPage, InvalidPage):
        solicitacao = paginator.page(paginator.num_pages)

    try:
        andamento = paginator1.page(page)
    except (EmptyPage, InvalidPage):
        andamento = paginator1.page(paginator1.num_pages)

    try:
        realizados = paginator2.page(page)
    except (EmptyPage, InvalidPage):
        realizados = paginator2.page(paginator2.num_pages)


    return render_to_response('orgposlogin/orgposlogin.html',{'solicitacao':
    solicitacao, 'andamento':andamento, 'realizados':realizados},context_instance=RequestContext(request))

def organizacao(request):
    try:
        solicita_id = int(request.GET.get('solicita', '1'))
    except ValueError:
        solicita_id = 0

    try:
        anda_id = int(request.GET.get('anda', '1'))
    except ValueError:
        anda_id = 0

    try:
        realiza_id = int(request.GET.get('realiza', '1'))
    except ValueError:
        realiza_id = 0

    solicita = get_object_or_404(Solicitacao, pk=solicita_id)
    anda = get_object_or_404(Andamento, pk=anda_id)
    realiza = get_object_or_404(Realizados, pk=realiza_id)

    return render_to_response('orgposlogin/orgposlogin.html',{'solicita':solicita, 'anda':anda, 'realiza':realiza},context_instance=RequestContext(request))



