from Store.models import WebsiteInfo, Order, OrderItem, Wishlist

def dynamic_data(request):
    con_web_info = WebsiteInfo.objects.last()
    if request.user.is_authenticated:
        con_order_items_count = OrderItem.objects.filter(user=request.user, ordered=False).count()
        con_wish_count = Wishlist.objects.filter(user=request.user).count()

        con_order_items = OrderItem.objects.filter(user=request.user, ordered=False)
        con_order = Order.objects.filter(user=request.user, ordered=False).last()
    else:
        con_order_items_count = 0
        con_wish_count = 0

        con_order_items = ''
        con_order = ''
    return {
        'con_web_info':con_web_info,
        'con_order_items_count':con_order_items_count,
        'con_wish_count':con_wish_count,
        
        'con_order':con_order,
        'con_order_items':con_order_items,
    }