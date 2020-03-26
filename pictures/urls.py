from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

from .views import PageList

app_name = 'pictures'

# Apps views
apps_urls = [
    path('', PageList.as_view(), name='page-list'),
    # path('<slug:project_dir>/edit/', PageDetailView.as_view(), name='page-detail-view'),
]

# Views index
urlpatterns = [
    path('', include(apps_urls)),
] + static(settings.MEDIA_URL)