from django.forms import (
    ModelForm, 
    IntegerField,
)

from models.models import Game, Rooms


class GameCreateForm(ModelForm):
    player_amount = IntegerField(min_value=2, max_value=4)
    class Meta:
        model = Game
        fields = ['player_amount']


class RoomCreateForm(ModelForm):

    class Meta:
        model = Rooms
        fields = '__all__'
