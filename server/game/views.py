from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from models.models import Rooms
from serializers.serializers import ResultSerializer


class Results(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        data = ResultSerializer(
            Rooms.objects.filter(game__is_ended=True),
            many=True).data
        return Response(
            data, status=HTTP_200_OK
        )
