from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Employee not found"}, status=404)
