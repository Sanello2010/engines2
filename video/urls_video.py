from django.urls import re_path
from . import views

urlpatterns = [
    re_path('video/', views.index_vid, name='index_vid')
]