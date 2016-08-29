from __future__ import unicode_literals

import random

from django import template
from django.utils.encoding import force_text

register = template.Library()


@register.filter(is_safe=True)
def evade(value):
    """
    Escape string value as a numeric character reference,
    randomly either in decimal or hexadecimal form

    Example:
    {% load evade_tags %}
    {{ "me@example.com"|evade }}
    """
    string = ""
    for letter in value:
        integer = random.randint(0, 1)
        if integer == 0:
            entity = "&#%d;" % ord(letter)
        else:
            entity = "&#x%x;" % ord(letter)
        string += entity
    return force_text(string)
