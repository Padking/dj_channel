from django import template

register = template.Library()

@register.filter
def to_empty(value):
    """
    Заменяет символ "@" на пустую строку"
    """

    return value.replace("@", "")
