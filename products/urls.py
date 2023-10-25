
from django.urls import path
from .views import ProductView , ProductViewByPk

urlpatterns = [
    path('product/<int:pk>/' , ProductViewByPk.as_view() , name='product-detail'),
    path('product/', ProductView.as_view() , name='product-list'),
]