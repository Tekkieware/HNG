from django.urls import path
from .views import user_data

urlpatterns = [
    path('', user_data, name="user")
    

]