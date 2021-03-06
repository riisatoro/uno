from rest_framework.serializers import ModelSerializer

from models.models import Game, Rooms, CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']


class ResultSerializer(ModelSerializer):
    player = CustomUserSerializer()

    class Meta:
        model = Rooms
        fields = ['player', 'winner']
        depth = 1


class AvailableGamesSerializer(ModelSerializer):
    players = CustomUserSerializer(read_only=True, many=True)

    class Meta:
        model = Game
        fields = ['id', 'player_amount', 'players', 'is_started']
        depth = 1


