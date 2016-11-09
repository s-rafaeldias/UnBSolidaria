from django.shortcuts import render_to_response
from noticia.models import Noticia
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.

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

def noticia(request):
    try:
        noticia_id = int(request.GET.get('noticia', '1'))
    except ValueError:
        noticia_id = 0

    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render_to_response('noticia/noticia.html',{'noticia':noticia}, context_instance=RequestContext(request))
