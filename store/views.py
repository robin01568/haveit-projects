from django.shortcuts import render, HttpResponse
from .models import *


# Create your views here.
def home(request):
    products = Product.objects.filter(is_show=True)
    categories = ProductCategory.objects.all()
    banners = Banner.objects.all()
    offer_banners = OfferBanner.objects.all().order_by('-id')[:4]
    supports = SupportSection.objects.all().last()
    blogs = blog.objects.all()

    context = {
        'products':products,
        'categories':categories,
        'banners':banners,
        'offer_banners':offer_banners,
        'supports':supports,
        'blogs':blogs,
    }
    return render(request, 'store/index.html',context)



def product_page(request):
    products = Product.objects.filter(is_show=True)
    categories = ProductCategory.objects.all()
    sizes = Size.objects.all()
    colors = Color.objects.all()
    context = {
        'products':products,
        'categories':categories,
        'sizes':sizes,
        'colors':colors,
    }
    return render(request, 'store/product-page.html',context)


def product_category_page(request, id):
    category = ProductCategory.objects.get(id=id)
    size_id = request.GET.get('size_id')
    color_id = request.GET.get('color_id')
    color = None
    size = None
    if color_id:
        color = Color.objects.get(id=color_id)
    if size_id:
        size = Size.objects.get(id=size_id)

    if size:
        products = Product.objects.filter(is_show=True, category=category, size__name__icontains=size)
    if color:
        products = Product.objects.filter(is_show=True, category=category, color__name__icontains=color)
    if size and color:
        products = Product.objects.filter(is_show=True, category=category, size__name__icontains= size, color__name__icontains=color)
    else:
        products = Product.objects.filter(is_show=True, category=category)

    categories = ProductCategory.objects.all()
    sizes = Size.objects.all()
    colors = Color.objects.all()
    context = {
        'category':category,
        'size':size,
        'color':color,
        'products':products,
        'categories':categories,
        'sizes':sizes,
        'colors':colors,
    }
    return render(request, 'store/product-page.html',context)




def product_details(request, id):
    product = Product.objects.get(id=id)

    context = {
        'product':product
    }
    return render(request, 'store/product-accordion-full-width.html', context)









def blog_full_width(request):
    blogs = blog.objects.all()
    
    context = {
        'blogs':blogs
    }
    return render(request, 'store/blog-full-width.html', context)



def blog_details(request, id):
    blogs = blog.objects.get(id=id)

    context = {
        'blogs':blogs
    }
    return render(request, 'store/blog-detail-full-width.html', context)




def faqs(request):
    faqs = faq.objects.all()
    
    context = {
        'faqs':faqs
    }
    
    return render(request, 'store/faq.html', context)








def about(request):
    return render(request, 'store/about_us.html')


def contact(request):
    return render(request, 'store/contact-us.html')


def carts(request):
    return render(request, 'store/cart.html')




def checkout(request):
    return render(request, 'store/checkout.html')




def compare(request):
    return render(request, 'store/compare.html')











def track_order(request):
    return render(request, 'store/track-order.html')





def terms_condition(request):
    return render(request, 'store/terms-condition.html')





def privacy_policy(request):
    return render(request, 'store/privacy-policy.html')




def wishlist(request):
    return render(request, 'store/wishlist.html')




def blog_left_sidebar(request):
    return render(request, 'store/blog-left-sidebar.html')



def blog_right_sidebar(request):
    return render(request, 'store/blog-right-sidebar.html')






def blog_detail_left_sidebar(request):
    return render(request, 'store/blog-detail-left-sidebar.html')



def blog_detail_right_sidebar(request):
    return render(request, 'store/blog-detail-right-sidebar.html')



def shop_banner_left_sidebar_col_3(request):
    return render(request, 'store/shop-banner-left-sidebar-col-3.html')




def product_left_sidebar(request):
    return render(request, 'store/product-left-sidebar.html')




def product_right_sidebar(request):
    return render(request, 'store/product-right-sidebar.html')




def product_accordion_left_sidebar(request):
    return render(request, 'store/product-accordion-left-sidebar.html')




def product_accordion_right_sidebar(request):
    return render(request, 'store/product-accordion-right-sidebar.html')




def product_full_width(request):
    return render(request, 'store/product-full-width.html')




def product_accordion_full_width(request):
    return render(request, 'store/product-accordion-full-width.html')




def shop_full_width(request):
    return render(request, 'store/shop-full-width.html')




def shop_banner_left_sidebar_col_4(request):
    return render(request, 'store/shop-banner-left-sidebar-col-4.html')




def shop_full_width_col_6(request):
    return render(request, 'store/shop-full-width-col-6.html')




def shop_list_right_sidebar(request):
    return render(request, 'store/shop-list-right-sidebar.html')