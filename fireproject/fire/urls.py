from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.FireAPIView.as_view(), name='fire'),
]