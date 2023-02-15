from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation as pass_validators
from django.core import exceptions
from django.shortcuts import render

# Create your views here.
from rest_framework import generics as rest_generic_views, serializers, views as rest_views
from rest_framework.authtoken import views as auth_token_views
from rest_framework.authtoken import models as auth_token_models
from rest_framework.response import Response

from sample_rest_api.api_auth.serializers import CreateUserSerializer

UserModel = get_user_model()


class RegisterApiView(rest_generic_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer


# copied from the documentation
class LoginApiView(auth_token_views.ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        # call the serializer class with the appropriate info from the request
        # it has its own serializer
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)

        # gets the user from the request
        user = serializer.validated_data['user']

        # creates a token for the user
        token, created = auth_token_models.Token.objects.get_or_create(user=user)

        # returns it as a response
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
        })


class LogoutApiView(rest_views.APIView):
    def get(self, request):
        return self.__perform_logout(request)

    def post(self, request):
        return self.__perform_logout(request)

    @staticmethod
    def __perform_logout(request):
        print(request.user)
        request.user.auth_token.delete()

        return Response({
            'message': 'You have been logged out!'
        })

