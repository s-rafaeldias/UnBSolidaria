# -*- coding: utf-8 -*-
from models import User, Trabalho
from django import forms

class ContactForm(forms.Form):
    INPUT_CLASS = 'form-control input-lg'

    from_email = forms.EmailField(required=True,
                                  widget=forms.EmailInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Email*'}))
    subject = forms.CharField(required=True,
                              widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Assunto*'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':INPUT_CLASS,'placeholder': 'Mensagem*'}))



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'cpf', 'cnpj', 'telephone', 'type',
                  'gender', 'description']