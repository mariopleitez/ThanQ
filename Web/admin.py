from django.contrib import admin

# Register your models here.
from Web.models import *

admin.site.register(Tag)
admin.site.register(Customer)
admin.site.register(Message)
admin.site.register(MessageLog)