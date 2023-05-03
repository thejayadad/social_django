from django.urls import path
from .views import dashboard

app_name = "post"

urlpatterns = [
    path("", dashboard, name='dashboard')
]