from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from store.models import Product, Order
from staff.forms import NewProduct


@staff_member_required
def product_list(request):

    products = Product.objects.all()

    return render(
        request, "product_list.html", {"title": "Products", "products": products}
    )


@staff_member_required
def add_product(request):

    form = NewProduct(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("product_list")

    return render(request, "product_form.html", {"title": "Add product", "form": form})


@staff_member_required
def edit_product(request, pid):
    product = Product.objects.get(id=pid)
    if request.POST:
        form = NewProduct(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        context = {
            "title": f"Edit product {pid}",
            "product": product,
            "form": NewProduct(instance=product),
        }
        return render(request, "product_form.html", context=context)


@staff_member_required
def delete_product(request, pid):
    Product.objects.filter(id=int(pid)).delete()
    return redirect("products")


@staff_member_required
def orders(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"title": "Orders", "orders": orders})
