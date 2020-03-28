from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from cart.cart import Cart


def product_list(request, category_slug=None):
    cart = Cart(request)
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    phone = Product.objects.filter(available=True, category_id=2)[:1]
    phone_deals = Product.objects.filter(available=True, category_id=2)[:2]
    laptops = Product.objects.filter(available=True, category_id=1)[:2]
    return render(request, 'shop/list.html', locals())


def product_detail(request, id, slug):
    cart = Cart(request)
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail.html', locals())