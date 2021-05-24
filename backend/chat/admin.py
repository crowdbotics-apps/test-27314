from django.contrib import admin
from .models import (
    Message,
    Thread,
    ForwardedMessage,
    ThreadAction,
    MessageAction,
    ThreadMember,
)

admin.site.register(Thread)
admin.site.register(ForwardedMessage)
admin.site.register(MessageAction)
admin.site.register(Message)
admin.site.register(ThreadMember)
admin.site.register(ThreadAction)

# Register your models here.
