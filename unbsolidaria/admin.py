from django.contrib import admin
<<<<<<< HEAD
from faq.models import FAQ
from noticia.models import Noticia


admin.site.register(FAQ)
admin.site.register(Noticia)
=======
from django.db import models
from django import forms

# Register your models here.
##########################################################################
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    formfield_overrides = {
    models.TextField: {'widget': forms.Textarea(
                       attrs={'rows': 5,
                              'cols': 40})}
    }

admin.site.register(FAQ, FAQAdmin)
##########################################################################
from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin):
    formfield_overrides = {
    models.TextField: {'widget': forms.Textarea(
                       attrs={'rows': 5,
                              'cols': 40})}
    }

admin.site.register(Noticia, NoticiaAdmin)
##########################################################################
>>>>>>> 9094f0b0dd74f572e4cf0fff7705c2e393cae616
