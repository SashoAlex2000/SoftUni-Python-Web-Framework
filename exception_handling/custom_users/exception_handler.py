from django.http import JsonResponse


def page_not_found(request, exception):  # < -- displayed when URL cannot be resolved
    return JsonResponse({
        "error": "Custom error",
        "status": 404,
    })
