from django.urls import path
from .import views

app_name='cloths'

urlpatterns = [
    path('', views.home, name='home'),
    path('cloths/<int:cloths_id>/', views.detail, name='detail'),
]