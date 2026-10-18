from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Product

def home(request):
    products = Product.objects.filter(is_available=True, is_featured=True)[:6]
    return render(request, "store/home.html", {"products": products})

def shop(request):
    products = Product.objects.filter(is_available=True)
    category = request.GET.get("category", "").strip()
    search = request.GET.get("q", "").strip()
    if category:
        products = products.filter(category__iexact=category)
    if search:
        products = products.filter(name__icontains=search)
    categories = Product.objects.filter(is_available=True).values_list("category", flat=True).distinct()
    return render(request, "store/shop.html", {
        "products": products, "categories": categories,
        "selected_category": category, "search_query": search,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, "store/product_detail.html", {"product": product})

@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_available=True)
    cart = request.session.get("cart", {})
    key = str(product.id)
    cart[key] = int(cart.get(key, 0)) + 1
    request.session["cart"] = cart
    messages.success(request, f"{product.name} was added to your cart.")
    return redirect(request.POST.get("next") or "store:shop")

def cart(request):
    cart_data = request.session.get("cart", {})
    items, total = [], 0
    products = Product.objects.filter(id__in=cart_data.keys(), is_available=True)
    for product in products:
        quantity = max(1, int(cart_data.get(str(product.id), 1)))
        line_total = product.price * quantity
        items.append({"product": product, "quantity": quantity, "line_total": line_total})
        total += line_total
    return render(request, "store/cart.html", {"items": items, "total": total})

@require_POST
def update_cart(request, product_id):
    cart_data = request.session.get("cart", {})
    quantity = int(request.POST.get("quantity", 1))
    if quantity <= 0:
        cart_data.pop(str(product_id), None)
    else:
        cart_data[str(product_id)] = min(quantity, 99)
    request.session["cart"] = cart_data
    return redirect("store:cart")

@require_POST
def remove_from_cart(request, product_id):
    cart_data = request.session.get("cart", {})
    cart_data.pop(str(product_id), None)
    request.session["cart"] = cart_data
    messages.info(request, "Item removed from your cart.")
    return redirect("store:cart")

def checkout(request):
    cart_data = request.session.get("cart", {})
    products = Product.objects.filter(id__in=cart_data.keys(), is_available=True)
    items, total = [], 0
    for product in products:
        quantity = max(1, int(cart_data.get(str(product.id), 1)))
        line_total = product.price * quantity
        items.append({"product": product, "quantity": quantity, "line_total": line_total})
        total += line_total
    if not items:
        messages.info(request, "Your cart is empty. Add a pin before checkout.")
        return redirect("store:shop")
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        address = request.POST.get("address", "").strip()
        if not name or not email or not address:
            messages.error(request, "Please complete all checkout fields.")
        else:
            request.session["demo_order"] = {
                "name": name, "email": email, "address": address,
                "total": total, "items": [
                    {"name": item["product"].name, "quantity": item["quantity"],
                     "line_total": item["line_total"]} for item in items
                ],
            }
            request.session["cart"] = {}
            return redirect("store:order_success")
    return render(request, "store/checkout.html", {"items": items, "total": total})

def order_success(request):
    order = request.session.get("demo_order")
    if not order:
        return redirect("store:home")
    return render(request, "store/order_success.html", {"order": order})

def about(request):
    return render(request, "store/about.html")

def contact(request):
    return render(request, "store/contact.html")
