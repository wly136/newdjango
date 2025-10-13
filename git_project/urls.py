from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def home_view(request):
    return HttpResponse('Hello, Django from git_project!')


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
]