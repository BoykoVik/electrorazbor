from django import template

register = template.Library()

@register.filter(name='mul')
def mul(value, arg):
    """Умножает value на arg"""
    return float(value) * float(arg)

