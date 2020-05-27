from django.conf import settings
from django.db.models import Avg
from django.shortcuts import render
from django.views import View

from .models import Route


class MapView(View):

    def get(self, request, *args, **kwargs):
        routes = Route.objects.all().prefetch_related('stations').order_by('name')
        stations_names = [route['name'] for route in routes.values()]
        active_route_name = request.GET.get('route') or stations_names[0]
        stations = routes.get(name=active_route_name).stations.values()
        center = {
            'y': routes.get(name=active_route_name).stations.aggregate(Avg('latitude'))['latitude__avg'],
            'x': routes.get(name=active_route_name).stations.aggregate(Avg('longitude'))['longitude__avg']
        }
        context = {
            'center': center,
            'routes': stations_names,
            'api_key': getattr(settings, "MAP_API_KEY", None)
        }

        if active_route_name:
            context['stations'] = stations
            context['this_route'] = active_route_name

        return render(request, 'stations.html', context)
