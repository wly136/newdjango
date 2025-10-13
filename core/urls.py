from django.urls import path
from .views import index, contact


urlpatterns = [
    path('', index, name='core-index'),
    path('contact/', contact, name='contact'),
]