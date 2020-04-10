from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='ugaach-home'),
    path('about/', views.about, name='ugaach-about'),
    path('feedback/', views.feedback, name='ugaach-feedback')
]