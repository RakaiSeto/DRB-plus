from django.urls import path, include, re_path
from api.views import home
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]

urlpatterns += static(
    "/assets/", document_root=os.path.join(settings.BASE_DIR, "frontend/dist")
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    # SPA fallback (React Router friendly)
    re_path(r"^.*$", home),
]
