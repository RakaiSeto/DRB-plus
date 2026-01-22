from django.urls import path
from .views import health as health_views

urlpatterns = [
    # Health Check
    path("ping", health_views.index, name="health"), 
]
