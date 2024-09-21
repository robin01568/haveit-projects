from django.db import models
from userAccount.models import CustomUser


# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255)
    image = models.ImageField(upload_to='prodect/prodect-image')
    hover_image = models.ImageField(upload_to='prodect/prodect-image')
    img1 = models.ImageField(upload_to='prodect/prodect-extra-image', blank=True, null=True)
    img2 = models.ImageField(upload_to='prodect/prodect-extra-image', blank=True, null=True)
    img3 = models.ImageField(upload_to='prodect/prodect-extra-image', blank=True, null=True)
    img4 = models.ImageField(upload_to='prodect/prodect-extra-image', blank=True, null=True)
    img5 = models.ImageField(upload_to='prodect/prodect-extra-image', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    short_description = models.TextField()
    detail_description = models.TextField()
    specific_description = models.TextField(blank=True, null=True)
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    stock = models.IntegerField(default=0)
    is_show = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def discount_percentage(self):
        if self.discount_price and self.price:
            discount_amount = self.price - self.discount_price
            discount_percentage = (discount_amount / self.price) * 100
            return discount_percentage
        else:
            return 0


