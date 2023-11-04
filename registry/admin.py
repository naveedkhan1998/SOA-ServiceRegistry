from typing import Any
from django.contrib import admin
from .models import Server, Url, ServiceEndpoint

from .helper import ping_websocket

# Register your models here.


class ServerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj: Server, form, change):
        if "is_active" in form.changed_data:
            qs_url = Url.objects.filter(server=obj)
            qs_endpoints = ServiceEndpoint.objects.filter(server=obj)

            if not obj.is_active:
                qs_url.update(is_active=False)
                qs_endpoints.update(is_active=False)
            else:
                qs_url.update(is_active=True)
                qs_endpoints.update(is_active=True)
            ping_websocket()

        obj.save()


class UrlAdmin(admin.ModelAdmin):
    def save_model(self, request: Any, obj: Url, form: Any, change: Any) -> None:
        if "is_active" in form.changed_data:
            ping_websocket()
        obj.save()


class ServiceEndpointAdmin(admin.ModelAdmin):
    def save_model(self, request: Any, obj: Url, form: Any, change: Any) -> None:
        if "is_active" in form.changed_data:
            ping_websocket()
        obj.save()


admin.site.register(Server, ServerAdmin)
admin.site.register(Url, UrlAdmin)
admin.site.register(ServiceEndpoint, ServiceEndpointAdmin)
