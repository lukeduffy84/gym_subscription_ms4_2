from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from store.models import Product, Customer

DEFAULT_CART = {"items": [], "total": 0}


def render_cart(request):
    cart_data = request.session.get("cart", DEFAULT_CART)
    items_rendered = []
    for item in cart_data["items"]:
        item["product"] = Product.objects.get(id=item["product_id"])
        items_rendered.append(item)
    cart_data["items"] = items_rendered
    return cart_data


def tag_router(request, tag):
    return redirect(tag.lower())


def home(request):
    return render(request, "home.html")


def register(request, next="home"):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            Customer.objects.create(user=user)
            return redirect(next)
        else:
            print(form.errors)
    return render(request, "register.html", context={"form": form})


def fitness(request):
    products = Product.objects.filter(category="ONLINE_COACHING")
    return render(request, "products.html")


def all_products(request):
    products = Product.objects.all()
    context = {"title": "All Products", "products": products}
    return render(request, "products.html", context=context)


def supplements(request):
    products = Product.objects.filter(category="SUPPLEMENTS")
    context = {"title": "Supplements", "products": products}
    return render(request, "products.html", context=context)


def merchandise(request):
    products = Product.objects.filter(category="MERCHANDISE")
    context = {"title": "Merchandise", "products": products}
    return render(request, "products.html", context=context)


def online_coaching(request):
    products = Product.objects.filter(category="ONLINE_COACHING")
    context = {"title": "Online Coaching", "products": products}
    return render(request, "products.html", context=context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {"title": f"{product.category}: {product.name}", "product": product}
    return render(request, "product_detail.html", context=context)


def testimonials(request):
    return render(request, "testimonials.html")


def cart(request):
    cart_data = render_cart(request)
    print(cart_data)
    return render(request, "cart.html", context={"cart_data": cart_data})


def add_to_cart(request):
    if request.method == "POST":
        product = Product.objects.get(id=request.POST["product_id"])
        quantity = int(request.POST.get("quantity", 1))
        subtotal = product.price_cents * quantity / 100
        new_item = {
            "product_id": product.id,
            "quantity": quantity,
            "subtotal": subtotal,
        }

        cart = request.session.get("cart", DEFAULT_CART)
        cart["items"].append(new_item)
        cart["total"] += subtotal

        request.session["cart"] = cart

        return redirect("cart")


def update_cart_item(request):
    return redirect("cart")


def remove_cart_item(request, id):
    return redirect("cart")


def checkout(request):
    cart_data = render_cart(request)
    return render(request, "checkout.html", context={"cart_data": cart_data})


def clear_session(request):
    request.session.clear()
    return redirect("home")
