from django.db import models

METHODS = [
    ("GET", "GET"),
    ("POST", "POST"),
    ("DELETE", "DELETE"),
    ("PUT", "PUT"),
]


class Server(models.Model):
    title = models.CharField(max_length=255, default="FastAPI")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Server Name: {self.title} | Is Active: {self.is_active}"


class Url(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    url = models.URLField(
        default="https://www.google.com/", unique=True, max_length=200
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Server: {self.server.title} | URL_ID: {self.id} | URL: {self.url} | Is Active: {self.is_active}"


class ServiceEndpoint(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    method = models.CharField(choices=METHODS, default="GET", max_length=10)
    endpoint = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Server: {self.server.title} | Method: {self.method} | Endpoint: {self.endpoint} | Is Active: {self.is_active}"
