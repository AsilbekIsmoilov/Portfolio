from django.urls import path

from portfolio.views import InfoList, InfoListByCategory

urlpatterns = [
    path('', InfoList.as_view(),name='index'),
    path('category/<slug:slug>', InfoListByCategory.as_view() ,name='category'),
]