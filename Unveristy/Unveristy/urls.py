from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Unveristy import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
