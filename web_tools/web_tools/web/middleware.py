# the middlewares have to be in a file named middleware in the app directory
from django.shortcuts import redirect
from django.utils import timezone


# get response gets the response from the 'next' middleware/view down the chain
def measure_time_middleware(get_response):
    def middleware(request, *args, **kwargs):
        start_time = timezone.now()

        # response has a status code (200 if all is alright), sessionId,
        # content with the page custom content, such as clicks
        response = get_response(request, *args, **kwargs)
        end_time = timezone.now()
        print(f'Executed in {end_time - start_time}')
        print(response.content)
        print(response.headers)
        return response

    # has to return a callable
    return middleware


class MeasureTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        start_time = timezone.now()
        response = self.get_response(request, *args, **kwargs)
        end_time = timezone.now()
        print(f'Executed in {end_time - start_time} from Class Middleware')
        return response


def redirect_on_error_middleware(get_response):

    def middleware(*args, **kwargs):
        response = get_response(*args, **kwargs)

        if response.status_code == 500:
            return redirect('index')

        return response

    return middleware


