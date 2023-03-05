from django.shortcuts import render
from rest_framework import views as rest_views, response
import bcrypt

from custom_users.models import CustomUser


# Create your views here.

class GetCreateUsers(rest_views.APIView):
    def get(self, request):

        return response.Response(
            {
                "message": "Okay",
            }
        )

    def post(self, request):
        user = CustomUser(**request.data)
        # hash the password
        # password = bcrypt.hashpw(request.data['password'], "123456")
        user.save()


class GetUpdateDeleteUser(rest_views.APIView):

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
