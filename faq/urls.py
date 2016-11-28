from django.conf.urls import url

from faq.views import (faq)

urlpatterns = [
    url(r'^faq/', faq, name="faq"),
]
