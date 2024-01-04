from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from . models import catagory
from . models import product

class catagoryadmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display=('catagoryid','catagoryname','status','created_at')

class productadmin(ImportExportModelAdmin,admin.ModelAdmin):
        list_display=('productid','productname','vendorname','quantity','status','created_at')


admin.site.register(catagory,catagoryadmin)
admin.site.register(product,productadmin)
