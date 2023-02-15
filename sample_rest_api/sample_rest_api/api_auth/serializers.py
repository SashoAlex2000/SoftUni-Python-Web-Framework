from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation as pass_validators
from django.core import exceptions
from django.shortcuts import render

# Create your views here.
from rest_framework import generics as rest_views, serializers
from rest_framework.authtoken import views as auth_token_views
from rest_framework.authtoken import models as auth_token_models
from rest_framework.response import Response

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    # hashes password
    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user

    # we actually bypass Django's refault password checks, so we have to custom validation
    def validate(self, data):

        user = UserModel(**data)

        password = data.get("password")
        errors = {

        }

        try:
            pass_validators.validate_password(password, user)
        except exceptions.ValidationError as e:
            errors['password'] = [e for e in e.messages]
        if errors:
            raise serializers.ValidationError(errors)

        return super().validate(data)

    # Modify the response sent to the client
    def to_representation(self, instance):
        user_repr = super().to_representation(instance)

        print(user_repr)  # < -- OrderedDict([('username', 'saso'), ('password', '1122')])
        user_repr.pop('password')
        print(user_repr)

        return user_repr
