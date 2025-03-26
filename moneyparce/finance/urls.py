from django.urls import path
from .views import dashboard

app_name = 'finance'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]
