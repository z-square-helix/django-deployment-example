from django import template

register = template.Library()

def cut(value, arg):
    # cuts out all values of arg from string
    return value.replace(arg, '')

register.filter('cutter', cut)
