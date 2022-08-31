from django import template

register = template.Library()
@register.filter('continue')
def continue_(loop):
    raise StopLoopException(loop, True)