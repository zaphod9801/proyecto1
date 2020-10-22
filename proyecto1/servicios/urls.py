from django.urls import path
from .views import Servicios
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Servicios,name = "Servicios"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)