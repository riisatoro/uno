from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from models.models import Rooms
from serializers.serializers import ResultSerializer

from .forms import GameCreateForm


class RoomsView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        data = ResultSerializer(
            Rooms.objects.filter(
                game__is_ended=False, game__is_started=False), many=True
            ).data
        return Response(data, status=HTTP_200_OK)

    def post(self, request):
        new_room = GameCreateForm(request.POST)
        if new_room.is_valid():
            new_room.save()
            return Response({}, status=HTTP_201_CREATED)
        return Response(new_room.errors.as_data(), status=HTTP_400_BAD_REQUEST)


class PlayerLeaveView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        current_room = Rooms.objects.filter(
            player=request.user,
            has_left=False,
        )
        if current_room:
            current_room.update(has_left=True)
            return Response({}, HTTP_200_OK)
        return Response({'details': 'User is not in game.'}, HTTP_400_BAD_REQUEST)


class ResultsView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        data = ResultSerializer(
            Rooms.objects.filter(game__is_ended=True),
            many=True).data
        return Response(
            data, status=HTTP_200_OK
        )
