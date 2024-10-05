from django.urls import path
from .views import InsertDataView

urlpatterns = [
    path('insert-data/', InsertDataView.as_view(), name='insert_data'),
]