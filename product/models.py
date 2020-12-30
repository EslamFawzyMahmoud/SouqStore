from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Product(models.Model):
    PRDname=models.CharField(max_length=100,verbose_name=_("Product name"))
    #category=models
    PRDdesc=models.TextField(verbose_name=_("Product Description"))
    PRDprice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("Product Price"))
    PRDcost=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("Product Cost"))
    PRDcreated=models.DateTimeField(verbose_name=_("Product Created At"))

    def __str__(self):
        return self.PRDname



class ProductImage(models.Model):
    PRDIProduct=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_("Product"))
    PRDIImage=models.ImageField(upload_to='product/',verbose_name=_("Image"))

    def __str__(self):
        return str(self.PRDIProduct)


# category
# image
# Alternatives
# Accessories






