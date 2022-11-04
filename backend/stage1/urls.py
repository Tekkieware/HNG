from django.urls import path
from .views import user_data, calculate

urlpatterns = [
    path('', user_data, name="user"),
    path('api/calculate', calculate, name="calculate")
]