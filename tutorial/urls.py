"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include 
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from rest_framework.renderers import CoreJSONRenderer, BrowsableAPIRenderer
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

schema_view = get_schema_view(
    title='Pastebin API',
    renderer_classes=[BrowsableAPIRenderer, CoreJSONRenderer, OpenAPIRenderer, SwaggerUIRenderer]
)

urlpatterns = [
	url(r'^', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^schema/$', schema_view),
]

urlpatterns += staticfiles_urlpatterns()

