
from django.urls import path
from .views import ProductView , ProductViewByPk

urlpatterns = [
    path('product-detail/<int:pk>/' , ProductViewByPk.as_view() , name='product-detail'),
    path('product-create/', ProductView.as_view() , name='create-product'),
    path('product-list/', ProductView.as_view() , name='product-list'),
    path('product-update/<int:pk>/', ProductViewByPk.as_view() , name='product-update'),
    path('product-delete/<int:pk>/', ProductViewByPk.as_view() , name='product-delete')
]