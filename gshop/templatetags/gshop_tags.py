from django import template

from gshop.models import Category

register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(slug=filter)


@register.inclusion_tag('gshop/list_categories.html')
def show_categories(selected=None):
    cats = Category.objects.all()
    return {"categories": cats, "cat_selected": selected}
