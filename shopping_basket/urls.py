from .views import BasketViewByPk , BasketView
from django.urls import path

urlpatterns = [
    path('basket/' , BasketView.as_view() , name = "basket-customer"),
    path("basket/<int:pk>/" , BasketViewByPk.as_view() , name="basket-handling")
]