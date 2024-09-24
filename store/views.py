from django.shortcuts import render, HttpResponse
from .models import *


# Create your views here.
def home(request):
    products = Product.objects.filter(is_show=True)
    categories = ProductCategory.objects.all()
    banners = Banner.objects.all()
    offer_banners = OfferBanner.objects.all().order_by('-id')[:4]
    supports = SupportSection.objects.all().last()

    context = {
        'products':products,
        'categories':categories,
        'banners':banners,
        'offer_banners':offer_banners,
        'supports':supports,
    }
    return render(request, 'store/index.html',context)



def product_details(request, id):
    product = Product.objects.get(id=id)

    context = {
        'product':product
    }
    return render(request, 'store/product-accordion-full-width.html', context)

from django.db.models import Sum

def about(request):
    # supports = Banner.objects.all() # multitple
    # supports = Banner.objects.first() # one
    # supports = Banner.objects.last() # one
    # supports = Banner.objects.get(id=1) # one
    # supports = Banner.objects.filter(title__icontains='dgdF explore') # multiple
    # supports = Banner.objects.filter(title__iexact='dgdF explore') # multiple
    # supports = Banner.objects.aggregate(amount_sum=Sum('amount')) # multiple
    # print('supports',supports)
    # supports = Banner.objects.all().order_by('-amount') # multiple
    # supports = Banner.objects.values('title', 'amount) # multiple
    # supports = Banner.objects.filter(id=1).values_list('amount') # multiple
    # print('supports ',supports)



    return render(request, 'store/about_us.html')


def contact(request):
    return render(request, 'store/contact-us.html')


def carts(request):
    return render(request, 'store/cart.html')




def checkout(request):
    return render(request, 'store/checkout.html')




def compare(request):
    return render(request, 'store/compare.html')




def faq(request):
    return render(request, 'store/faq.html')






def track_order(request):
    return render(request, 'store/track-order.html')





def terms_condition(request):
    return render(request, 'store/terms-condition.html')





def privacy_policy(request):
    return render(request, 'store/privacy-policy.html')




def wishlist(request):
    return render(request, 'store/wishlist.html')




def blog_detail_full_width(request):
    return render(request, 'store/blog-detail-full-width.html')



def blog_left_sidebar(request):
    return render(request, 'store/blog-left-sidebar.html')



def blog_right_sidebar(request):
    return render(request, 'store/blog-right-sidebar.html')



def blog_full_width(request):
    return render(request, 'store/blog-full-width.html')



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