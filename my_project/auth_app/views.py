from django.shortcuts import render
from django.views.generic import CreateView
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.models import UserModel
from auth_app.serializers import UserSerializer


# Create your views here.


class CreateUserAPIView(APIView):
    @extend_schema(
        summary='Create new user',
        description=(
            "Creates a new user account with the provided information.\n\n"
            "Behavior:\n"
            "- Password will be hashed automatically.\n"
            "- Default phone number is '000-000-0000' if not provided.\n"
            "- Other optional fields like city can also be set."
        ),
        request=UserSerializer,
        responses={
            201: OpenApiResponse(UserSerializer, description='User created successfully.'),
            400: OpenApiResponse(OpenApiTypes.OBJECT, description='Validation error')
        }
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

