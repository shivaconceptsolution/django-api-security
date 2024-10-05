from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('addition', views.addition, name='addition'),
    path('sicalc', views.sicalc, name='sicalc')
]