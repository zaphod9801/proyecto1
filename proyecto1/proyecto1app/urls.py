from django.urls import path
from proyecto1app.views import Home, Tienda, Blog, Contacto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Home, name = "Home"),
    path('tienda/',Tienda,name = "Tienda"),
    path('blog/',Blog,name = "Blog"),
    path('contacto/',Contacto,name = "Contacto"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)