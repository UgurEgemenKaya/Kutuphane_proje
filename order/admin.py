from django.contrib import admin

# Register your models here.
from order.models import Shopcart, Order, OrderProduct


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'amount']
    list_filter = ['user']

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user','product','quantity')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'code', 'city', 'total', 'status','phone']
    list_filter = ['status']
    readonly_fields = ('user','address','city','country','phone','first_name','ip','last_name','total','teslim_tarih','code')
    can_delete = False
    inlines = [OrderProductline]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity','teslim_tarih']
    list_filter = ['user']

admin.site.register(Shopcart,ShopCartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)

