from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from main import views


app_name = 'main'

urlpatterns = [
    path('', views.main_link, name='main_link'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
