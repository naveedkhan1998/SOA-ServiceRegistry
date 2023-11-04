from django.urls import path
from . import views


urlpatterns = [
    path("update/", views.update_clients, name="update"),
    path("endpoints/", views.get_endpoints, name="endpoints"),
]
