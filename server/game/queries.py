from models.models import Rooms, Game


def is_player_in_room(users: list):
    return Game.objects.filter(
        is_ended=False,
        players__in=users,
        rooms__has_left=False,
    ).exists()


def get_available_games():
    return Game.objects.filter(is_started=False, is_ended=False).all()


def get_game_by_id(id):
    return Game.objects.filter(id=id).first()


def get_room_by_game_player(game, player):
    return Rooms.objects.filter(game=game, player=player).first()


def count_players_in_game(game):
    game = Game.objects.filter(id=game.id, rooms__has_left=False).first()
    if not game:
        return 0
    return game.players.count()


def join_player_game(player, game, cards):
    return Rooms(player=player, game=game, player_cards=cards).save()


def player_allowed_to_join_game(player, game_id):
    return (
        Game.objects.filter(id=game_id, is_started=False, is_ended=False)
        .exclude(players__in=[player])
        .exists()
    )


def get_game_by_user(player):
    return Game.objects.filter(is_ended=False, players__in=[player]).first()