from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from notice import views

app_name = 'notice'

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('feed/<pk>/', views.notice_detail, name='notice_detail'),
    path('feed/<pk>/update/', views.notice_update, name='notice_update'),
    path('feed/<pk>/delete/', views.notice_delete, name='notice_delete'),

    path('create/', views.notice_create, name='notice_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
