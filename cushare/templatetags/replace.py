from django import template

register = template.Library()

@register.filter
def replace(value):
    # code = """{}""".format(value).replace("ス", """ """)
    ## create a custom filter for django templates
    return value