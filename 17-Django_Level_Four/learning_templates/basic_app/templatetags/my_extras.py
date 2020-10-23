from django import template
register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

# one way of declaring filter
#register.filter('cut',cut)
