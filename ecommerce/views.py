from django.shortcuts import render
from django.shortcuts import render_to_response

from ecommerce.models import *

def index(request):
    products = Product.objects.all()
    variables = {'products': products}
    return render(request, 'home/index.html', variables)

def show(request, product_id=None):
    product = Product.objects.filter(id=product_id)
    variables = {'product': product}
    return render(request, 'home/show.html', variables)

def show_category(request, catid=None):
    """
    category list page view for the website
    """
    products = []
    try:
        if catid:
            category = Category.objects.get(id=catid)
            products = Product.objects.filter(category=category)
    except:
        pass
    c = {'categories': Category.objects.all(), 'products': products}
    return render_to_response('index.html', c, context_instance=RequestContext(request))
