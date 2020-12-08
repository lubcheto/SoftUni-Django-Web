from django import template

register = template.Library()



@register.filter(is_safe=True)
def label_with_classes(value, arg):
    a=5
    # return value.label_tag(attrs={'class': arg})
    # return value.label_tag(attrs={'class': arg})
    return value.label_tag(attrs={'class': arg})