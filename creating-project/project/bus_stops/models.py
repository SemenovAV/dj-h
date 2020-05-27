from django.db import models


class Station(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    latitude = models.FloatField(
        null=False,
        blank=False,
    )
    longitude = models.FloatField(
        null=False,
        blank=False
    )
    route_numbers = models.ManyToManyField(
        'Route',
        related_name='stations',
        symmetrical=False,
        through='RouteStation'
    )
    name = models.CharField(max_length=100)


class Route(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False
    )


class RouteStation(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
