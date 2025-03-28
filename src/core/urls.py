
from django.contrib import admin
from django.urls import path
from .views import home, healthz
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('healthz/', healthz),
]
