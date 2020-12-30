from django.db import models

# Create your models here.


class Product(models.Model):
    PRDname=models.CharField(max_length=100)
    #category=models
    PRDdesc=models.TextField()
    PRDprice=models.DecimalField(max_digits=5,decimal_places=2)
    PRDcost=models.DecimalField(max_digits=5,decimal_places=2)
    PRDcreated=models.DateTimeField()

    def __str__(self):
        return self.PRDname

# category
# image
# Alternatives
# Accessories






