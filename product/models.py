from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Product(models.Model):
    PRDname=models.CharField(max_length=100,verbose_name=_("Product name"))
    PRDCategory=models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True)
    PRDBrand=models.ForeignKey('settings.Brand',on_delete=models.CASCADE,blank=True,null=True)
    PRDdesc=models.TextField(verbose_name=_("Product Description"))
    PRDprice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("Product Price"))
    PRDcost=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("Product Cost"))
    PRDcreated=models.DateTimeField(verbose_name=_("Product Created At"))

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
    def __str__(self):
        return self.PRDname

class ProductImage(models.Model):
    PRDIProduct=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_("Product"))
    PRDIImage=models.ImageField(upload_to='product/',verbose_name=_("Image"),)

    def __str__(self):
        return str(self.PRDIProduct)

class Category(models.Model):
    CATName=models.CharField(max_length=50,verbose_name=_("Name"))
    # __isnull to filter the main category
    CATParent=models.ForeignKey('self',limit_choices_to={'CATParent__isnull':True},verbose_name=_("Main Category"),on_delete=models.CASCADE,blank=True,null=True)
    CATDesc=models.TextField(verbose_name=_("Description"))
    CATImg=models.ImageField(upload_to='category/',verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return str(self.CATName)

class Product_Alternatives(models.Model):
    PALNProduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='main_Product',verbose_name=_("Product"))
    PALNAlternative=models.ManyToManyField(Product,related_name='Alternatives_Product',verbose_name=_("Alternative"))
    class Meta:
        verbose_name=_("Product Alternative")
        verbose_name_plural=_("Product Alternatives")

    def __str__(self):
        return str(self.PALNProduct)

class Product_Accessories(models.Model):
    PACProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mainAccessories_Product',verbose_name=_("Product"))
    PACAccessories = models.ManyToManyField(Product, related_name='Accessories_Product',verbose_name=_("Accessories"))
    class Meta:
        verbose_name=_("ProductAccessory")
        verbose_name_plural=_("Product Accessories")

    def __str__(self):
        return str(self.PACProduct)