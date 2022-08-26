from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts.helpers import response_dict
from accounts.models import User, UserProfile

from accounts.serializers import CustomTokenObtainPairSerializer, LoginSerializer, UserAccountProfileSerializer

# Create your views here.


class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    token_serializer_class = CustomTokenObtainPairSerializer
    throttle_scope = "login"

    # @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        request_data = request.data.copy()
        serializer = self.get_serializer(
            data=request_data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        # Add contact_number in request data. It's required for auth backend
        request_data["username"] = serializer.validated_data["user"].username
        _token_serializer = self.token_serializer_class(
            data=request_data)  # Generate JWT token
        _token_serializer.is_valid(raise_exception=True)
        response_data = _token_serializer.validated_data
        return Response(response_data, status=status.HTTP_200_OK)


class UserAccountAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            user_id = request.user.id
            user_obj = UserProfile.objects.filter(user_id=user_id).last()
            if not user_obj:
                if User.objects.filter(id=user_id).exists():
                    obj = UserProfile.objects.none()
                    serializer_data = UserAccountProfileSerializer(
                        obj, context={"user_id": user_id}).data
                else:
                    response = response_dict(
                        data=None, error=True, message="User Not Found")
                    return Response(response, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer_data = UserAccountProfileSerializer(user_obj).data
            response = dict()
            response["user"] = serializer_data
            # response["completed_screens"] = profile_progress_status(user_id) \
            #     if (user_id and profile_progress_status(user_id)) else []
            response = response_dict(
                data=response, error=False, message="User Account Detail")
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = response_dict(
                data=None, error=True, message=str(e.__str__()))
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
