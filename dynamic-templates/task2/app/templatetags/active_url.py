from django import template

register = template.Library()


@register.simple_tag()
def active_url(request, name):
    if request:
        if request.resolver_match.url_name == name:
            return "active"
        return ""
