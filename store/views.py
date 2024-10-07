from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


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


@login_required
def add_to_cart(request):
    index = request.POST.get('index')
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))
    product = Product.objects.get(id=product_id)
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False,
    )
    if created:
        order_item.quantity = quantity
        order_item.save()
        messages.success(request, "Added to cart")

        order, created = Order.objects.get_or_create(
            user=request.user,
            ordered = False
        )
        if created:
            order.items.add(order_item)
            order.status = 'Pending'
            order.save()
        else:
            order.items.add(order_item)
            order.save()
    else:
        order_item.quantity += quantity
        order_item.save()
        messages.success(request, "Increment Quantity")
    if index:
        return redirect('home')
    else:
        return redirect('product_details', id=product_id)

@login_required
def remove_to_cart(request, id):
    OrderItem.objects.get(id=id).delete()
    messages.success(request, "Removed Successfully")
    return redirect('carts')

@login_required
def carts(request):
    order_items = OrderItem.objects.filter(user=request.user, ordered=False)
    order = Order.objects.filter(user=request.user, ordered=False).last()
    products = Product.objects.filter(is_show=True)
    return render(request, 'store/cart.html',{'order':order,'order_items':order_items,'products':products})

@login_required
def cart_quantity_increment(request):
    order_item_id = request.POST.get('order_item_id')
    order_item = OrderItem.objects.get(id=order_item_id)
    if order_item.quantity <= order_item.product.stock:
        order_item.quantity += 1
        order_item.save()
        messages.success(request, 'Order quantity Increase')
    else:
        messages.error(request, 'Out of stock')
    return redirect('carts')

@login_required
def cart_quantity_decrement(request):
    order_item_id = request.POST.get('order_item_id')
    order_item = OrderItem.objects.get(id=order_item_id)
    if order_item.quantity > 1:
        order_item.quantity -= 1
        order_item.save()
        messages.success(request, 'Order quantity Decrease')
    else:
        messages.error(request, 'Quantity should be more than 1')
    return redirect('carts')


@login_required
def wishlist(request):
    wish_list = Wishlist.objects.filter(user=request.user)
    return render(request, 'store/wishlist.html',{'wish_list':wish_list})




@login_required
def add_to_wishlist(request):
    product_id = request.GET.get('product_id')
    home = request.GET.get('home', None)
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(product=product, user=request.user)
    if created:
        messages.success(request, 'Product added to wishlist')
    else:
        messages.warning(request, 'Product already in wishlist')
    if home:
        return redirect('home')
    else:
        return redirect('product_details', id=product.id)


@login_required
def remove_to_wishlist(request, id):
    Wishlist.objects.get(id=id).delete()
    messages.success(request, "Removed Successfully")
    return redirect('wishlist')

def blog_full_width(request):
    blogs = blog.objects.all()
    
    context = {
        'blogs':blogs
    }
    return render(request, 'store/blog-full-width.html', context)



def blog_details(request, id):
    blogs = blog.objects.get(id=id)
    comments = BlogComment.objects.filter(blog=blogs)
    comments_count = BlogComment.objects.filter(blog=blogs).count()
    user_form = BlogCommentForm() 
    if request.method == 'POST':
        user_form = BlogCommentForm(request.POST)
        if user_form.is_valid():
            obj = user_form.save(commit=False)
            obj.blog = blogs
            obj.save()
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Somthing went Wrong!')

    context = {
        'blogs': blogs,
        'user_form': user_form,
        'comments': comments,
        'comments_count': comments_count,
    }
    return render(request, 'store/blog-detail-full-width.html', context)



def contact(request):
    user_form = ContactUsForm() 

    if request.method == 'POST':
        user_form = ContactUsForm(request.POST)
        if user_form.is_valid():
            user_form.save() 
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Somthing went Wrong!')

    context = {
        'user_form': user_form,
    }
    return render(request, 'store/contact-us.html', context)



def about(request):
    abouts = AboutUs.objects.all()
    services = SupportSection.objects.all().last()

    context = {
        'abouts':abouts,
        'services':services,
    }
    return render(request, 'store/about_us.html', context)



def faqs(request):
    faqs = faq.objects.all()
    
    context = {
        'faqs':faqs
    }
    return render(request, 'store/faq.html', context)



def terms_condition(request):
    TermsConditions = TermsCondition.objects.all()
    
    context = {
        'TermsConditions':TermsConditions
    }
    return render(request, 'store/terms-condition.html', context)



def privacy_policy(request):
    PrivacyPolicys = PrivacyPolicy.objects.all()
    
    context = {
        'PrivacyPolicys':PrivacyPolicys
    }
    return render(request, 'store/privacy-policy.html', context)

































def compare(request):
    return render(request, 'store/compare.html')











def track_order(request):
    return render(request, 'store/track-order.html')


















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




def load_districts(request):
    division_id = request.GET.get('division_id')
    objs = District.objects.filter(division__id=division_id).order_by('name')
    return render(request, 'store/load_data/dropdown_list.html', {'objs': objs})


def load_sub_districts(request):
    district_id = request.GET.get('district_id')
    objs = SubDistrict.objects.filter(district__id=district_id).order_by('name')
    return render(request, 'store/load_data/dropdown_list.html', {'objs': objs})