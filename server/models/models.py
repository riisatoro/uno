from django.db.models import (
    Model,
    IntegerField,
    EmailField,
    DateTimeField,
    BooleanField,
    JSONField,
    ManyToManyField,
    ForeignKey,
    CASCADE
)
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = EmailField(blank=False, null=False, unique=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Rooms(Model):
    player = ForeignKey(CustomUser, on_delete=CASCADE)
    game = ForeignKey("Game", on_delete=CASCADE)
    player_cards = JSONField()
    has_left = BooleanField(default=False)
    winner = BooleanField(default=False)

    def __str__(self):
        return f"Player = {self.player} Cards = {self.player_cards} Left = {self.has_left} Win = {winner}"


class Game(Model):
    is_started = BooleanField(default=False)
    is_ended = BooleanField(default=False)
    last_card = JSONField(null=True)
    players = ManyToManyField(CustomUser, through=Rooms)
    player_amount = IntegerField(null=False, default=2)
    started_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"Started = {self.is_started} Ended = {self.is_ended} Players = {self.player_amount}"
