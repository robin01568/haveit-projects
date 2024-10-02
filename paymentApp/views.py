from django.shortcuts import render
from Store.models import Order, OrderItem, Product
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def checkout(request):
    order_items = OrderItem.objects.filter(user=request.user, ordered=False)
    order = Order.objects.filter(user=request.user, ordered=False).last()
    products = Product.objects.filter(is_show=True)
    context = {
        'order':order,
        'order_items':order_items,
        'products':products
        }
    return render(request, 'paymentApp/checkout.html', context)

@login_required
def apply_coupon(request):
    pass