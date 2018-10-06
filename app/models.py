from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.AutoField(primary_key=True,null=False,unique=True)
    category_name = models.CharField(max_length=40)

    def __str__(self):
        return str(self.category_name)


class Sub_Category(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=40)

    def __str__(self):
        return self.sub_category_name

class Product(models.Model):
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=45)

    def __str__(self):
        return self.product_name
