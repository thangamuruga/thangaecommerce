from django.db import models
import datetime
import os


def getfilename(request,filename):
	now_time=datetime.datetime.now().strftime("%Y%m%D%H:%M:%S")
	new_filename = "%s%s"%(now_time,filename)
	return os.path.join('uploads/',new_filename)

class catagory(models.Model):
    catagoryid=models.AutoField(primary_key=True)
    catagoryname=models.CharField(max_length=150, null=False, blank=False)
    image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    description=models.CharField(max_length=500,null=True,blank=False)
    status=models.BooleanField(default=True,help_text="1=show,0=hidden")
    created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
	return self.categoryname


class product(models.Model):
    catagoryname=models.ForeignKey(catagory,on_delete=models.CASCADE)
    productid=models.AutoField(primary_key=True)
    productname=models.CharField(max_length=150,null=False,blank=False)
    vendorname=models.CharField(max_length=150,null=False,blank=False)
    productimage=models.ImageField(upload_to=getfilename,null=True,blank=True)
    pdescription=models.CharField(max_length=500,null=True,blank=False)
    quantity=models.PositiveIntegerField(null=False,blank=False)
    originalprice=models.FloatField(null=False,blank=False)
    sellingprice=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=True,help_text="1=show,0=hidden")
    Treanding=models.BooleanField(default=False,help_text="0=default,1=threanding")
    created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
	return self.productname
