from django.db import models
from UserAccount.models import CustomUser
from phone_field import PhoneField

# Create your models here.
class WebsiteInfo(models.Model):
    logo = models.ImageField(upload_to='web-logo')
    contact1 = PhoneField(blank=True, null=True, help_text='Contact phone number')
    contact2 = PhoneField(blank=True, null=True, help_text='Contact phone number')
    email1 = models.EmailField(blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    locations = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'Website Info Id:{self.id}'

# https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d456.4274610640328!2d90.42616504843001!3d23.76806489560369!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3755bf537d1f2e09%3A0x8fe7a3faf331a140!2z4KaH4KaJ4Kao4Ka_4Kat4Ka-4Kaw4KeN4Ka4IOCmh-CmnyDgpofgpqjgprjgp43gpp_gpr_gpp_gpr_gpongpp8!5e0!3m2!1sbn!2sbd!4v1727514123372!5m2!1sbn!2sbd


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
        
        
class Categorys(models.Model):
    name = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='category/category-icon-image', blank=True, null=True)
    total_items = models.BigIntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Banner(models.Model):
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='banner')

    def __str__(self):
        return self.title


class OfferBanner(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='banner')

    def __str__(self):
        return self.title

class SupportSection(models.Model):
    shipping = models.CharField(max_length=255)
    support = models.CharField(max_length=255)
    returns = models.CharField(max_length=255)
    payment = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.shipping
    
    
class blog(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    short_description1 = models.TextField(blank=True, null=True)
    short_description2 = models.TextField(blank=True, null=True)
    short_description3 = models.TextField(blank=True, null=True)
    detail_description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    date = models.DateField()
    image = models.ImageField(upload_to='Blog-image')
    img1 = models.ImageField(upload_to='Blog-image')
    img2 = models.ImageField(upload_to='Blog-image')
    
    def __str__(self):
        return self.title
    

class BlogComment(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    


class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    massage = models.TextField(max_length=255)
    date = models.DateField(auto_created=True, auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
    
    
class AboutUs(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    description1 = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)
    description4 = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='About_us-image')
    img1 = models.ImageField(upload_to='About_us-image', blank=True, null=True)
    img2 = models.ImageField(upload_to='About_us-image', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
    
    
class faq(models.Model):
    questions = models.CharField(max_length=255)
    answer = models.TextField()
    
    def __str__(self):
        return self.questions
    
    
    
    
class TermsCondition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    
    
    
class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title