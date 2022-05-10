from django import template

register = template.Library()

@register.filter(name='filter')
def filt(value, arg):
    return value.filter(category=arg)