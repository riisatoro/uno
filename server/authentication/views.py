from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from .forms import UserCreationForm

class Registration(APIView):
    def post(self, request):
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return Response({}, status=HTTP_200_OK)
        return Response(user.errors.as_data(), status=HTTP_400_BAD_REQUEST)
