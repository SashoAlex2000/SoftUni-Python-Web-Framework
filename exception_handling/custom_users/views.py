from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework import views as rest_views, response, status
import bcrypt

from custom_users.models import CustomUser


# Create your views here.

# all these handlers are 'global' - always raised
def handler500(request):

    context = {
        'err_message': 'my handler',
    }

    curr_response = render(request, 'test_500.html', context)

    # what the status code we return is :?
    curr_response.status_code = 500

    # return HttpResponse(template.render(request))
    return curr_response


def second_handler_500(request, *args, **kwargs):
    template = loader.get_template('test_500.html')
    response.status_code = 400

    return HttpResponse(template.render({'err_message': 'ines handler error!'}, request))


def custom_error_view(request, exception=None):
    return render(request, "test_500.html", {
        'err_message': 'StackOverflow error message',
    })


class GetCreateUsers(rest_views.APIView):
    def get(self, request):

        CustomUser.objects.get(pk=999)  # <-- to throw error

        return response.Response(
            {
                "message": "Okay",
            }
        )

    def post(self, request):
        user = CustomUser(**request.data)
        # hash the password
        # password = bcrypt.hashpw(request.data['password'], "123456")

        # unique constraint failed, but the exception is IntegrityError
        # try:
        #     user.save()
        #     template = loader.get_template('index.html')
        # except IntegrityError as ex:
        #     # we also have to return the appropriate status
        #     return response.Response(
        #         {
        #             "message": "A user with this email already exists"
        #         },
        #         status=status.HTTP_400_BAD_REQUEST
        #     )
        #
        # return response.Response(
        #     {"message": "hmm"},
        # )

        try:
            user.save()
            template = loader.get_template('index.html')
            context = {
                "name": user.name,
            }
        except IntegrityError as ex:
            template = loader.get_template('test_500.html')
            context = {
                "err_message": f"{user.email} is already taken!"
            }

        return HttpResponse(template.render(context, request))


class GetUpdateDeleteUser(rest_views.APIView):

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
