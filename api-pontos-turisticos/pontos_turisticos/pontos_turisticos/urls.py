"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls. static import static
from rest_framework.authtoken.views import obtain_auth_token
from core.api.viewsets import PontoTuristicoViewsets 
from atracoes.api.viewsets import AtracaoViewsets
from enderecos.api.viewsets import EnderecoViewsets
from comentario.api.viewsets import ComentarioViewset
from avaliacao.api.viewsets import AvaliacaoViewsets

router = routers.DefaultRouter()
router.register(r'pontoturistico',PontoTuristicoViewsets, basename='pontos_turisticos')
router.register(r'atracoes',AtracaoViewsets)
router.register(r'endereco',EnderecoViewsets)
router.register(r'comentario',ComentarioViewset)
router.register(r'avaliacoes',AvaliacaoViewsets)


urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path(r'api-token-auth/',obtain_auth_token),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
