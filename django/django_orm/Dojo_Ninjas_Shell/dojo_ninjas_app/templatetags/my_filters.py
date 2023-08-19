from django import template
register = template.Library()

@register.filter(name='filter_ninjas')
def filter_by_dojo_id(ninjas_list, id):
    return [ninja for ninja in ninjas_list if ninja.dojo_id== id]