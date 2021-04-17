from django.db.models import (
    Model,
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
    winner = BooleanField(default=False)

    def __str__(self):
        return f"{self.player} {self.player_cards}"


class Game(Model):
    is_started = BooleanField(default=False)
    is_ended = BooleanField(default=False)
    last_card = JSONField(null=True)
    players = ManyToManyField(CustomUser, through=Rooms)
    started_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.is_started} ? {self.is_ended} ? {self.started_at}"
