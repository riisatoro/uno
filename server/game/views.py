from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from game.forms import GameCreateForm, RoomCreateForm
from game.queries import (
    is_player_in_room,
    get_available_games,
    get_game_by_id,
    get_room_by_game_player,
    count_players_in_game,
    join_player_game,
    player_allowed_to_join_game,
)
from gamecore.main import get_random_card
from serializers.serializers import AvailableGamesSerializer


class GameView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        """Receive available games to join"""
        games = get_available_games()
        data = AvailableGamesSerializer(games, many=True).data
        return Response(data, status=HTTP_200_OK)

    def put(self, request):
        """Join existed game"""
        if is_player_in_room([request.user]):
            return Response(
                {"details": "You are allowed to play only in one room"},
                status=HTTP_400_BAD_REQUEST,
            )
        if not player_allowed_to_join_game(request.user, request.POST.get("game_id")):
            return Response({"details": "You are not allowed to join this game"})

        game = get_game_by_id(request.POST.get("game_id"))
        cards = get_random_card()
        join_player_game(request.user, game, cards)
        if game.players.count() == game.player_amount:
            game.is_started=True
            game.save()
        return Response({}, status=HTTP_200_OK)

    def post(self, request):
        """Create own game"""
        if is_player_in_room([request.user]):
            return Response(
                {"details": "You are allowed to play only in one room"},
                status=HTTP_400_BAD_REQUEST,
            )

        new_game = GameCreateForm(request.POST)
        if not new_game.is_valid():
            return Response(new_game.errors.as_data(), status=HTTP_400_BAD_REQUEST)

        new_game = new_game.save()
        new_room = RoomCreateForm(
            {
                "player": request.user,
                "game": new_game,
                "player_cards": get_random_card(),
            }
        )
        new_room.save()
        return Response({}, status=HTTP_201_CREATED)

    def delete(self, request):
        game = get_game_by_id(request.POST.get("game_id"))
        room = get_room_by_game_player(game, request.user)
        if not game or not room:
            return Response({"details": "This game or room does not exist"})

        room.has_left = True
        room.save()
        if count_players_in_game(game) < 2:
            game.is_ended = True
            game.save()
        return Response({}, status=HTTP_200_OK)


class ResultsView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        data = ResultSerializer(
            Rooms.objects.filter(game__is_ended=True), many=True
        ).data
        return Response(data, status=HTTP_200_OK)
