from django import template

register = template.Library()


@register.filter(name='num_to_stars')
def num_to_stars(value):
    return '★' * int(value)
