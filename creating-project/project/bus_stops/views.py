from django.conf import settings
from django.shortcuts import render
from django.views import View

from .models import Route


class MapView(View):

    def get(self, request, *args, **kwargs):
        routes = Route.objects.all().prefetch_related('stations').order_by('name')
        names = [route['name'] for route in routes.values()]
        context = {
            'center': {
                'y': 55.755814,
                'x': 37.617635
            },
            'routes': names,
            'api_key': getattr(settings, "MAP_API_KEY", None)
        }
        name = request.GET.get('route') or names[0]
        if name:
            context['stations'] = routes.get(name=name).stations.values()
            context['this_route'] = name

        return render(request, 'stations.html', context)
