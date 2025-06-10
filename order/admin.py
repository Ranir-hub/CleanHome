from django.contrib import admin
from order.models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Order, OrderAdmin)