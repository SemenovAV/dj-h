import csv

from django.core.management.base import BaseCommand

from bus_stops.models import Station, Route, RouteStation


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('moscow_bus_stations.csv', encoding="cp1251") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            next(reader)
            stations_query = set()
            routes_query = set()
            route_station = {}
            for station in reader:
                station_id = station.get('ID')
                longitude = station.get('Longitude_WGS84')
                latitude = station.get('Latitude_WGS84')
                station_name = station.get('Name')
                routes = station.get('RouteNumbers')

                if station_id and longitude and latitude and station_name and routes:

                    station_obj = Station(
                        id=station_id,
                        latitude=latitude,
                        longitude=longitude,
                        name=station_name
                    )

                    stations_query.add(station_obj)
                    routes = routes.split(';')
                    route_station[station_id] = routes
                    for elem in routes:
                        name = elem.strip()
                        routes_query.add(name)
            routes_query = {name: int(route_id) for route_id, name in enumerate(routes_query)}

            Station.objects.bulk_create(stations_query)
            Route.objects.bulk_create(
                [Route(id=route_id, name=name) for name, route_id in routes_query.items()]
            )

            station_dict = Station.objects.in_bulk()
            route_dict = Route.objects.in_bulk()

            route_station_query = set()
            for station, routes in route_station.items():
                for route in routes:
                    route_station_query.add(
                        RouteStation(
                            id=len(route_station_query),
                            station=station_dict[int(station)],
                            route=route_dict[routes_query[route.strip()]]
                        ))

            RouteStation.objects.bulk_create(route_station_query)
