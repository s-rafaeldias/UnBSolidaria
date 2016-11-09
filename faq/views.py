from django.shortcuts import render_to_response
from faq.models import FAQ
from django.template import RequestContext

from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.

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
