from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('charts', views.charts, name='charts'),
    path('details/<int:pk>', views.details, name='details'),
    path('getpersons', views.getpersons, name='getpersons')
]