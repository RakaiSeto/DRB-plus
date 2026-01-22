from django.http import HttpResponse
from django.conf import settings
import os

def home(request):
    index_path = os.path.join(
        settings.BASE_DIR,
        "frontend",
        "dist",
        "index.html"
    )
    with open(index_path, "r", encoding="utf-8") as f:
        return HttpResponse(f.read())
