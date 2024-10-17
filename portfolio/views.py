from django.shortcuts import render
from django.views.generic import ListView

from portfolio.models import Info, Category


# Create your views here.


class InfoList(ListView):
    model = Info
    context_object_name = 'categories'
    template_name = 'portfolio/index.html'
    extra_context = {
        "title":"My Portfolio"
    }

    def get_queryset(self):
        categories = Category.objects.all()
        data = []
        for category in categories:
            infos = category.infos.all()

            data.append({
                "title":category.title,
                "infos":infos
            })
        return data

class InfoListByCategory(ListView):
    model = Info
    context_object_name = "infos"
    template_name = 'portfolio/index.html'
    extra_context = {
        "title":"Portfolio Page"
    }