from django.urls import path, include, re_path
from api.views import home

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]

urlpatterns += [
    re_path(r"^.*$", home),
]
