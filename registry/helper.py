from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def ping_websocket():
    room_name = "test"
    message_data = {
        "type": "chat_message",
        "message": "PING",
        "user": "ADMIN",
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(f"ws_{room_name}", message_data)
