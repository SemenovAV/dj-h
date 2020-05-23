from django.db import models


class Player(models.Model):
    pass


class Game(models.Model):
    is_active = models.BooleanField(default=True, editable=True)
    number = models.PositiveSmallIntegerField(blank=True)
    author = models.ForeignKey(Player, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='attempts')
    attempt = models.PositiveSmallIntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='players')
    is_true = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
