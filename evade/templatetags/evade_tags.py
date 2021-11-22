from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from ..evade import evade

register = template.Library()


@register.filter(name="evade", is_safe=True)
@stringfilter
def evade_filter(value):
    """
    Escape string value to a pseudo-random HTML character reference, into one
    of named, decimal, or hexadecimal forms

    Example:
    {% load evade_tags %}
    {{ "me@example.com"|evade }}
    """
    return mark_safe(evade(value))
