# -*- coding: utf-8 -*-
from django import forms
from orgposlogin.models import Andamento

class AndamentoForm(forms.ModelForm):
    class Meta:
	model = Andamento
	fields = [
		"trabalho",
		"subtitulo",
		"descricao",
		"image"
		]
