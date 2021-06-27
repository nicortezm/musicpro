from django.contrib import admin
from .models import Payment,Order,OrderProduct
# Register your models here.


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0
    def has_view_permission(self, request,obj=None):
        if request.user.groups.filter(name='Vendedor').exists():
            return True
        return False

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'first_name','last_name', 'email', 'region', 'comuna', 'order_total', 'descuento', 'status', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]

    def has_view_permission(self, request,obj=None):
        if request.user.groups.filter(name='Vendedor').exists():
            return True
        return False

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','payment_id','payment_method','amount_paid','status','created_at']

class OrderProductAdmin(admin.ModelAdmin):
    def has_view_permission(self, request,obj=None):
        if request.user.groups.filter(name='Vendedor').exists():
            return True
        return False
   
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)