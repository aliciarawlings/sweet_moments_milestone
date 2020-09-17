from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<selected_item_id>/', views.update_cart, name='add_to_cart'),
    path('update_cart/<selected_item_id>/', views.update_cart, name='update_cart')
]