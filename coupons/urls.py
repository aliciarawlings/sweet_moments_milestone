from django.conf.urls import url
from .import views
urlpatterns = [
    url('apply/', views.apply_coupon, name='apply')
]