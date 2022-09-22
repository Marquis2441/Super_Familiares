from django.urls import path
from Family.views import listar_family

urlpatterns = [
    path('', listar_family),
]