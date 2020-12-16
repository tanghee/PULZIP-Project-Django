from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from board import views

app_name = 'board'

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('feed/<pk>/', views.board_detail, name='board_detail'),
    path('feed/<pk>/update/', views.board_update, name='board_update'),
    path('feed/<pk>/delete/', views.board_delete, name='board_delete'),

    path('create/', views.board_create, name='board_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
