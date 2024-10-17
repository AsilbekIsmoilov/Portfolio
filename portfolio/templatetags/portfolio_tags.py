from django import template

from portfolio.models import Category, About, Experience, Projects

register = template.Library()
@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.simple_tag()
def get_about():
    return About.objects.all()

@register.simple_tag()
def get_experience():
    return Experience.objects.all()

@register.simple_tag()
def get_projects():
    return Projects.objects.all()