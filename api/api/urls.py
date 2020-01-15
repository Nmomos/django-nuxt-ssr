from django.contrib import admin
from django.urls import path, include  # 追加
from django.conf import settings  # 追加
from django.conf.urls.static import static  # 追加

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),  # 追加
]

# 追加
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
