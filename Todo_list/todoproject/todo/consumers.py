import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("task_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("task_updates", self.channel_name)

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            "task_updates",
            {
                'type': 'task_update',
                'message': text_data
            }
        )

    async def task_update(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
