from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.websocket_example, name="websocket_example"),
]
