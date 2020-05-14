from django.contrib import admin
from .models import Vendor,Cart,Orders,Payment,ConfirmOrder,ShippingAddress
# Register your models here.


admin.site.register(Vendor)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Payment)
admin.site.register(ConfirmOrder)
admin.site.register(ShippingAddress)