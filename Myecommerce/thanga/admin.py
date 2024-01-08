from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import catagory, product

class CatagoryResource(resources.ModelResource):
    class Meta:
        model = catagory

class ProductResource(resources.ModelResource):
    class Meta:
        model = product
        exclude = ('productid', 'productimage','created_at')
        fields = ('catagoryname', 'productname', 'vendorname', 'pdescription', 'quantity', 'originalprice', 'sellingprice', 'status', 'Treanding' )
        skip_unchanged = True
        report_skipped = False

class CatagoryAdmin(ImportExportModelAdmin):
    list_display = ('catagoryid', 'catagoryname', 'status', 'created_at')
    resource_class = CatagoryResource

class ProductAdmin(ImportExportModelAdmin):
    list_display = ('productid', 'productname', 'vendorname', 'quantity', 'status', 'created_at')
    resource_class = ProductResource


admin.site.register(catagory, CatagoryAdmin)
admin.site.register(product, ProductAdmin)
