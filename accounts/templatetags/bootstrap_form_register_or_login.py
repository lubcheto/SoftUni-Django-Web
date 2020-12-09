from django import template

register = template.Library()


@register.inclusion_tag('tags/bootstrap_form_register_or_login.html')
def bootstrap_form_register_or_login(form, action, method):
    for (_,field) in form.fields.items():
        if 'class' not in field.widget.attrs:
            field.widget.attrs['class']= ' '
        field.widget.attrs['class'] +=' form-control'

    return {
        'form':form,
        'action':action,
        'method':method,
        }


