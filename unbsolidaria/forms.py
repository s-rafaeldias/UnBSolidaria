# -*- coding: utf-8 -*-
from models import User, Organizacao, Voluntario, Trabalho, Endereco
from django import forms
from localflavor.br.forms import BRCPFField, BRCNPJField, BRPhoneNumberField

class ContactForm(forms.Form):
    INPUT_CLASS = 'form-control input-lg'

    from_email = forms.EmailField(required=True,
                                  widget=forms.EmailInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Email*'}))
    subject = forms.CharField(required=True,
                              widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Assunto*'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':INPUT_CLASS,'placeholder': 'Mensagem*'}))



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    telefone = BRPhoneNumberField(required=True,widget=None)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'telefone', 'descricao']


class OrganizacaoForm(forms.ModelForm):

    class Meta:
        model = Organizacao
        fields = ['cnpj']


class VoluntarioForm(forms.ModelForm):
    cpf = BRCPFField(required=True)

    class Meta:
        model = Voluntario
        fields = ['cpf', 'sexo']


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['endereco', 'cep']


class TrabalhoForm(forms.ModelForm):
    class Meta:
        model = Trabalho
 	fields = ['titulo', 'descricao', 'autor', 'email', 'vagas', 'data_inicio', 'data_fim']

