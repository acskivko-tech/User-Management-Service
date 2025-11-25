from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.models import UserModel
from auth_app.serializers import UserSerializer


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserAPIListView(APIView):
    @extend_schema(
        summary='List users',
        description=(
                "Returns a list of all registered users with their full information.\n\n"
                "Behavior:\n"
                "- Shows only existing users.\n"
                "- Each user is serialized using the standard UserSerializer."
        ),
        responses={
            200: OpenApiResponse(UserSerializer(many=True), description='List of users returned successfully.')
        }
    )
    def get(self,request):
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetCurrentUserAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        summary='Get current user',
        description=(
                "Retrieves information about the currently authenticated user.\n\n"
                "Behavior:\n"
                "- Returns full user profile.\n"
                "- Requires the user to be authenticated."
        ),
        responses={
            200: OpenApiResponse(UserSerializer, description='Current user retrieved successfully.'),
            401: OpenApiResponse(OpenApiTypes.OBJECT, description='User not authenticated'),
        }
    )
    def get(self,request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetIDUserAPIView(APIView):
    permission_classes = (IsAdminUser,)

    @extend_schema(
        summary='Get user by ID',
        description=(
                "Retrieves information of a specific user by their ID.\n\n"
                "Behavior:\n"
                "- Only admin users can access this endpoint.\n"
                "- Returns full user profile for the requested user ID.\n"
                "- If user with provided ID does not exist, returns 404."
        ),
        responses={
            200: OpenApiResponse(UserSerializer, description='User retrieved successfully.'),
            401: OpenApiResponse(OpenApiTypes.OBJECT, description='User not authenticated'),
            403: OpenApiResponse(OpenApiTypes.OBJECT, description='User does not have permission'),
            404: OpenApiResponse(OpenApiTypes.OBJECT, description='User not found'),
        }
    )
    def get(self,request,pk):
        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CurrentUserUpdateAPIView(APIView):
    @extend_schema(
        summary='Update current user',
        description=(
            "Updates the profile information of the currently authenticated user.\n\n"
            "Behavior:\n"
            "- Only the fields provided in the request will be updated.\n"
            "- Fields not included in the request remain unchanged.\n"
            "- Password is not updated here (only profile fields).\n"
        ),
        request=UserSerializer,
        responses={
            200: OpenApiResponse(UserSerializer, description='User updated successfully.'),
            400: OpenApiResponse(OpenApiTypes.OBJECT, description='Validation error'),
            401: OpenApiResponse(OpenApiTypes.OBJECT, description='User not authenticated'),
        }
    )

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IDUserAPIUpdateView(APIView):
    permission_classes = (IsAdminUser,)
    @extend_schema(
        summary='Update user by ID (admin only)',
        description=(
            "Allows an administrator to update any user's profile using their ID.\n\n"
            "Behavior:\n"
            "- Only the fields provided will be updated.\n"
            "- If the user does not exist, a 404 error is returned.\n"
            "- Password is not updated here (profile fields only)."
        ),
        request=UserSerializer,
        responses={
            200: OpenApiResponse(UserSerializer, description='User updated successfully.'),
            400: OpenApiResponse(OpenApiTypes.OBJECT, description='Validation error'),
            401: OpenApiResponse(OpenApiTypes.OBJECT, description='Authentication required'),
            403: OpenApiResponse(OpenApiTypes.OBJECT, description='Admin privileges required'),
            404: OpenApiResponse(OpenApiTypes.OBJECT, description='User not found'),
        }
    )
    def put(self,request,pk):
        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
             return Response({'detail':"User was not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)