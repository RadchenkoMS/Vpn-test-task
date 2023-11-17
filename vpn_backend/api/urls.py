from django.urls import path
from .views import proxy_view

urlpatterns = [
    path('<path:external_url>/', proxy_view, name='proxy_view'),
]