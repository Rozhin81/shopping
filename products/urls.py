
from django.urls import path
from .views import ProductView , ProductViewByPk , ChartViewByPk

urlpatterns = [
    path('product/<int:pk>/' , ProductViewByPk.as_view() , name='product-detail'),
    path('product/', ProductView.as_view() , name='product-list'),
    path('chart/<int:pk>/' , ChartViewByPk.as_view() , name="chart_each_product")
]