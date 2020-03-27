from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

from .views import PageList, PageDetail

app_name = 'pictures'

# Apps views
apps_urls = [
    path('', PageList.as_view(), name='page-list'),
    path('<int:pk>/', PageDetail.as_view(), name='page-detail'),
]

# Views index
urlpatterns = [
    path('', include(apps_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)