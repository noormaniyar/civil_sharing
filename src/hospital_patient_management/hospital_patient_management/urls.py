from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('patients.urls', namespace="patient")),
    path('', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),

]
