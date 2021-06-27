from django.contrib import admin
from .models import Category, Marca,Product, Variation
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name','slug')
    def has_view_permission(self, request,obj=None):
            if request.user.groups.filter(name='Bodeguero').exists():
                return True
            return False
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','marca','price','stock','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}

    def has_view_permission(self, request,obj=None):
            if request.user.groups.filter(name='Bodeguero').exists():
                return True
            return False
class VariationAdmin(admin.ModelAdmin):
    
    list_display = ('product','variation_category','variation_value','is_active','created_date')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category','variation_value')

    def has_view_permission(self, request,obj=None):
            if request.user.groups.filter(name='Bodeguero').exists():
                return True
            return False

class MarcaAdmin(admin.ModelAdmin):
    def has_view_permission(self, request,obj=None):
        if request.user.groups.filter(name='Bodeguero').exists():
            return True
        return False

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Variation,VariationAdmin)
admin.site.register(Marca,MarcaAdmin)