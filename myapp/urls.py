from django.urls import path
from . import views

urlpatterns = [
    path('mostrar_datos/', views.mostrar_datos, name='mostrar_datos'),
]
