from django.contrib import admin
from models.models import Game, Rooms


class GameAdmin(admin.ModelAdmin):
    list_display = [
        'is_started', 'is_ended', 'last_card', 'player_amount', 'started_at'
    ]


class RoomsAdmin(admin.ModelAdmin):
    list_display = [
        'player', 'game', 'player_cards', 'has_left', 'winner'
    ]


admin.site.register(Game, GameAdmin)
admin.site.register(Rooms, RoomsAdmin)
