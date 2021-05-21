from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include('material.urls', namespace="materials")),
    path('cloths/', include('cloths.urls', namespace='cloths')),
    path('admin/', admin.site.urls),
]
