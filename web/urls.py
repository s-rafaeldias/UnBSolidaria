"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
1. Add an import:  from other_app.views import Home
2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
1. Add an import:  from blog import urls as blog_urls
2. Import the include() function: from django.conf.urls import url, include
3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from unbsolidaria import views
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'trabalhos', views.TrabalhoViewSet)
router.register(r'news', views.NoticiaViewSet)

urlpatterns = [
    url(r'', include("unbsolidaria.urls")),
    url(r'^admin/', admin.site.urls),

    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^', include(router.urls)),
	url(r'^rest-auth/', include('rest_auth.urls')),
	url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
