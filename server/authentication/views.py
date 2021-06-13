from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from rest_framework.permissions import IsAuthenticated
from serializers.serializers import CustomUserSerializer

from .forms import UserCreationForm


class Registration(APIView):
    def post(self, request):
        user = UserCreationForm(request.data)
        if user.is_valid():
            user.save()
            return Response({}, status=HTTP_200_OK)
        return Response(user.errors.as_data(), status=HTTP_400_BAD_REQUEST)


class UserData(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        user = request.user
        data = CustomUserSerializer(user).data
        return Response(data, HTTP_200_OK)

