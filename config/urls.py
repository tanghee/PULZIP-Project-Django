from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('board/', include('board.urls', namespace='board')),
    path('notice/', include('notice.urls', namespace='notice')),
    path('', include('main.urls', namespace='main')),
]
