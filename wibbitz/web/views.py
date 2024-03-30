import json

from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse

from web.models import Subscribe, Customers, Features, VideoBlog, Testimonial, MarketingFeatures, Product, Blog, Contact
from web.forms import ContactForm

def index(request):
    customers = Customers.objects.all()
    latest_customers = Customers.objects.all()[:4]
    features = Features.objects.all()
    videoblogs = VideoBlog.objects.all()
    testimonials = Testimonial.objects.all()
    marketingfeatures = MarketingFeatures.objects.all()
    products = Product.objects.all()
    blogs = Blog.objects.all()

    form = ContactForm()

    context = {
        "customers": customers,
        "features": features,
        "videoblogs": videoblogs,
        "testimonials": testimonials,
        "marketingfeatures": marketingfeatures,
        "products": products,
        "blogs": blogs,
        "form": form,
        "latest_customers": latest_customers
    }
    return render(request, "index.html", context=context)


def subscribe(request):
    email = request.POST.get('email')
    if not Subscribe.objects.filter(email=email).exists():

        Subscribe.objects.create(
            email=email
        )
        response_data = {
            "status" : "success",
            "title" : "Successfully Subscribed",
        }

    else:
        response_data = {
            "status" : "error",
            "title" : "You Have Already Subscribed",
        }
    return HttpResponse(json.dumps(response_data), content_type="application/javascript")
    

def contact(request):

    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        response_data = {
            "status" : "success",
            "title" : "Successfully Subscribed",
        }

    else:
        response_data = {
            "status" : "error",
            "title" : "You Have Already Subscribed",
        }
    return HttpResponse(json.dumps(response_data), content_type="application/javascript")


def product(request, pk):
    product = get_object_or_404(Product.objects.filter(pk=pk))
    context = {
        "product": product
    }
    return render(request, "product.html", context=context)