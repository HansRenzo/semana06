from django.urls import path
from .views import PruebaView, CategoriaView, UnaCategoriaView, ProductosView

urlpatterns = [
    path('prueba', PruebaView.as_view()),
    path('categoria', CategoriaView.as_view()),
    path('categoria/<int:id>', UnaCategoriaView.as_view()),
    path('productos', ProductosView.as_view()),
]