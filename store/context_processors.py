from Store.models import WebsiteInfo, Order, OrderItem

def dynamic_data(request):
    con_web_info = WebsiteInfo.objects.last()
    con_order_items_count = OrderItem.objects.filter(ordered=False).count()
    con_order_items = OrderItem.objects.filter(ordered=False)
    con_order = Order.objects.filter(user=request.user, ordered=False).last()
    return {
        'con_web_info':con_web_info,
        'con_order_items_count':con_order_items_count,
        'con_order':con_order,
        'con_order_items':con_order_items,
    }