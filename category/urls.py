from django.urls import path
from .views import CategoryView , CategoryViewByPk

urlpatterns = [
    path('category/' , CategoryView.as_view() , name='category-list'),
    path('category/<int:pk>/' , CategoryViewByPk.as_view() , name = 'category-detail')
]