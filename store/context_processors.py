from Store.models import WebsiteInfo

def dynamic_data(request):
    con_web_info = WebsiteInfo.objects.last()

    return {
        'con_web_info':con_web_info
    }