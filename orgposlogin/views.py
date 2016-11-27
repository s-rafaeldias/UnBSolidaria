from django.shortcuts import render_to_response, render, redirect
from orgposlogin.models import Andamento, Realizados
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from orgposlogin.forms import AndamentoForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib import messages

# Create your views here.


def organizacoes(request):

    andamento_list = Andamento.objects.all()
    realizados_list = Realizados.objects.all()
    paginator1 = Paginator(andamento_list, 3)
    paginator2 = Paginator(realizados_list, 3)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        andamento = paginator1.page(page)
    except (EmptyPage, InvalidPage):
        andamento = paginator1.page(paginator1.num_pages)

    try:
        realizados = paginator2.page(page)
    except (EmptyPage, InvalidPage):
        realizados = paginator2.page(paginator2.num_pages)


    return render_to_response('orgposlogin/orgposlogin.html',{'andamento':andamento, 'realizados':realizados},context_instance=RequestContext(request))

def organizacao(request):
    try:
        anda_id = int(request.GET.get('anda', '1'))
    except ValueError:
        anda_id = 0

    try:
        realiza_id = int(request.GET.get('realiza', '1'))
    except ValueError:
        realiza_id = 0

    anda = get_object_or_404(Andamento, pk=anda_id)
    realiza = get_object_or_404(Realizados, pk=realiza_id)

    return render_to_response('orgposlogin/orgposlogin.html',{'anda':anda, 'realiza':realiza},context_instance=RequestContext(request))


def anda_create(request):
	form = AndamentoForm(request.POST or None, request.FILES or None)
	if request.method == "POST":
		trabalho = request.POST.get("trabalho")
		subtitulo = request.POST.get("subtitulo")
		descricao = request.POST.get("descricao")
		image = request.POST.get("image")
		Andamento.objects.create(trabalho=trabalho, subtitulo=subtitulo, descricao=descricao,image=image)
	context = {
		"form": form,
	}	
	return render(request, "orgposlogin/anda_create.html", context)

def anda_update(request, id=None):
	instance = get_object_or_404(Andamento, id=id)
	form = AndamentoForm(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()

	context = {
		"trabalho": instance.trabalho,
		"subtitulo": instance.subtitulo,
		"descricao": instance.descricao,
		"image": instance.image,
		"instance": instance,
		"form": form,
	}
	messages.success(request, "Trabalho atualizado com sucesso")
	return render(request, "orgposlogin/anda_update.html", context)


def anda_delete(request, id=None):
	instance1 = get_object_or_404(Andamento, id=id)
	instance1.delete()
	messages.success(request, 'Trabalho deletado com sucesso')
	return redirect("/orgposlogin")







