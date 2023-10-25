from django.urls import path
from .views import  SubCategoryView , SubCategoryViewByPk

urlpatterns = [
    path('subcategory/' , SubCategoryView.as_view() , name='category-list'),
    path('subcategory/<int:pk>/' , SubCategoryViewByPk.as_view() , name = 'category-detail')
]