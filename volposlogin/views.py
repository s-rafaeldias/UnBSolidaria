from django.shortcuts import render_to_response
from volposlogin.models import Sugeridos
from volposlogin.models import Andamento
from volposlogin.models import Realizados
from volposlogin.models import Comentarios
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.


def voluntarios(request):
    sugeridos_list = Sugeridos.objects.all()
    andamento_list = Andamento.objects.all()
    realizados_list = Realizados.objects.all()
    comentarios_list = Comentarios.objects.all()


    paginator = Paginator(sugeridos_list, 10
)
    paginator1 = Paginator(andamento_list, 10)
    paginator2 = Paginator(realizados_list, 10)
    paginator3 = Paginator(comentarios_list, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        sugeridos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        sugeridos = paginator.page(paginator.num_pages)

    try:
        andamento = paginator1.page(page)
    except (EmptyPage, InvalidPage):
        andamento = paginator1.page(paginator1.num_pages)

    try:
        realizados = paginator2.page(page)
    except (EmptyPage, InvalidPage):
        realizados = paginator2.page(paginator2.num_pages)

    try:
        comentarios = paginator3.page(page)
    except (EmptyPage, InvalidPage):
        comentarios = paginator3.page(paginator3.num_pages)

    return render_to_response('volposlogin/volposlogin.html',{'sugeridos':
    sugeridos, 'andamento':andamento, 'realizados':realizados, 'comentarios':comentarios},context_instance=RequestContext(request))

def voluntario(request):
    try:
        sugere_id = int(request.GET.get('sugere', '1'))
    except ValueError:
        sugere_id = 0

    try:
        anda_id = int(request.GET.get('anda', '1'))
    except ValueError:
        anda_id = 0

    try:
        realiza_id = int(request.GET.get('realiza', '1'))
    except ValueError:
        realiza_id = 0

    try:
        comenta_id = int(request.GET.get('comenta', '1'))
    except ValueError:
        comenta_id = 0

    sugere = get_object_or_404(Sugeridos, pk=solicita_id)
    anda = get_object_or_404(Andamento, pk=anda_id)
    realiza = get_object_or_404(Realizados, pk=realiza_id)
    comenta = get_object_or_404(Comentarios, pk=comenta_id)

    return render_to_response('volposlogin/volposlogin.html',{'sugere':sugere, 'anda':anda, 'realiza':realiza, 'comenta':comenta },context_instance=RequestContext(request))



