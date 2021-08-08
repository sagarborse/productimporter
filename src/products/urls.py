from django.urls import re_path
from .views import index, upload

urlpatterns = [
    re_path(r'index/$', index, name='index'),
    re_path(r'^upload/$', upload, name='index'),
]