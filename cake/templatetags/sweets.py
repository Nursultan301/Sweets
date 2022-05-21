from django import template

from cake.models import Sweets

register = template.Library()


@register.inclusion_tag('cake/tags/sweets.html')
def get_sweets(cnt=8):
    sweets = Sweets.objects.order_by("-create_at")[:cnt]
    return {"sweets": sweets}
