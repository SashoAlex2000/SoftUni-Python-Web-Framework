from django.http import JsonResponse


def page_not_found(request, exception):
    return JsonResponse({
        "error": "Custom error",
        "status": 404,
    })

