from django.urls import path
from .views import UsuarioDetalles, UsuarioAPIView

urlpatterns = [
    path('usuarios/', UsuarioAPIView.as_view()),
    path('detalle/<uuid:ID>/', UsuarioDetalles.as_view())
]
