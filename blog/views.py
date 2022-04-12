from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home(request):
    context = {
        "articles": [
            {
                "title": "لیگ قهرمانان اروپا",
                "description": "چرت و پرت می نویسم همانا رستگار شوم:)",
                "image": "https://hamsan-cdn-a.yektanet.com/media/CACHE/images/items/image_ebb59fb4-cef8-4d6f-b697-188949b392e2__1daEtXrrjk/90/375x250.jpeg"
            },
            {
                "title": "لیگ قهرمانان آسیا",
                "description": "What does the fox say?",
                "image": "https://www.thespruce.com/thmb/JObhDcNNBALGVyF9S7bFoQwoXsI=/941x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/plants-with-big-flowers-4138211-hero-b10becb169064cc4b3c7967adc1b22e1.jpg"
            }
        ]

    }
    return render(request, "blog/home.html", context)

# Create your views here.
