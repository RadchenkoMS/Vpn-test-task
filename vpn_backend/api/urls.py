from django.urls import path
from .views import proxy_view

urlpatterns = [
    path('test/', proxy_view, name='proxy_view'),
]