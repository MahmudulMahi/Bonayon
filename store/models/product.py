from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.name




class Product_Details(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE)
    details = models.TextField(null=True,default="empty")
    details_show=models.BooleanField(default=False)
    uses = models.TextField(null=True,default="empty")
    show = models.BooleanField(default=False)
    diseases=models.TextField(null=True,default="empty")
    diseases_show=models.BooleanField(default=False)
    care_growing=models.TextField(null=True,default="empty")
    care_growing1_show= models.BooleanField(default=False)
    fartilizer=models.TextField(null=True,default="empty")
    fartilizer_show=models.BooleanField(default=False)