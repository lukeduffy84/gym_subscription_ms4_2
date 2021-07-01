from django.shortcuts import render
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.http import HttpResponseRedirect,JsonResponse
from .authorize import login_authorize, create_payment_charge,generate_card_token

# Create your views here.

def index(request):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    print("login_data:",login_data, islogin)
    return render(request,'index.html',{'islogin':islogin,'cart_price':cart_price})


def customer_login(request):
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("username",username,"password",password)
        check_user = Customer.objects.filter(username=username).exists()
        check_email = Customer.objects.filter(email=username).exists()
        if check_user:
            hash_password = Customer.objects.get(
                        username=username).password
            if check_password(password, hash_password):
                request.session['username']=username
                return HttpResponseRedirect('/')
        elif check_email:
            hash_password = Customer.objects.get(email=username)
            if check_password(password, hash_password.password):
                request.session['username']=hash_password.username
                return HttpResponseRedirect('/')
        else:
            error= "Username or password didn't match"
            messages.info(request, error)
            return HttpResponseRedirect('/login')

    return render(request,'login.html',{'cart_price':cart_price})


def customer_signup(request):
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_email = request.POST.get('confirm_email')
        confirm_password = request.POST.get('confirm_password')
        check_email = Customer.objects.filter(username=username).exists()

        if check_email:
            error= "This email is already taken"
            messages.info(request, error)
            return HttpResponseRedirect('/register')

        if email != confirm_email:
            error= "Email doesn't match"
            messages.info(request, error)
            return HttpResponseRedirect('/register')

        if password != confirm_password:
            error= "Password doesn't match"
            messages.info(request, error)
            return HttpResponseRedirect('/register')

        password_hash = make_password(password)
        data = {"email": email, "username": username,
                "password": password_hash}

        print(data)
        Customer.objects.create(**data)
        return HttpResponseRedirect('/login')

    return render(request,'register.html',{'cart_price':cart_price})



def add_product(request):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    csid = login_data['_id']
    if request.method == 'POST':
        name = request.POST.get('name')
        image_link = request.POST.get('image_link')
        rating = request.POST.get('rating')
        sku = request.POST.get('sku')
        price = request.POST.get('price')
        description = request.POST.get('description')
        has_sizes = request.POST.get('has_sizes')
        category = request.POST.getlist('category')
        data = dict(name=name,image_link=image_link,rating=rating,sku=sku,
        description=description,has_sizes=has_sizes,category=category[0],customer_id=int(csid),price=float(price))
        print("data:",data)
        Product.objects.create(**data)
        return HttpResponseRedirect('/myproduct')

    return render(request,'addProduct.html',{'islogin':islogin,'cart_price':cart_price})


def edit_product(request, pid):

    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False

    if not islogin:
        return HttpResponseRedirect('/login')

    product_data = Product.objects.get(id=int(pid))

    if request.method == 'POST':
        name = request.POST.get('name')
        image_link = request.POST.get('image_link')
        rating = request.POST.get('rating')
        sku = request.POST.get('sku')
        price = request.POST.get('price')
        description = request.POST.get('description')
        has_sizes = request.POST.get('has_sizes')
        data = dict(name=name,image_link=image_link,rating=rating,sku=sku,
        description=description,has_sizes=has_sizes,price=float(price))
        print("data:",data)
        product_data.name = name
        product_data.image_link = image_link
        product_data.rating = rating
        product_data.has_sizes = has_sizes
        product_data.description = description
        product_data.sku = sku
        product_data.price = float(price)

        product_data.save()
        return HttpResponseRedirect('/myproduct')
    return render(request,'editProduct.html',{'data':product_data,'islogin':islogin,'cart_price':cart_price,'pid':pid})


def delete_product(request,pid):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    if not islogin:
        return HttpResponseRedirect('/login')

    Product.objects.filter(id=int(pid)).delete()
    return HttpResponseRedirect('/myproduct')



def my_products(request):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    csid = login_data['_id']
    product_data = Product.objects.filter(customer_id=csid).all()
    count = product_data.count()
    return render(request,'my_product.html',{'data':product_data,'islogin':islogin,'cart_price':cart_price,'count':count})


def view_my_product(request, pid):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    product_data = Product.objects.get(id=int(pid))

    return render(request,'view_product.html',{'data':product_data,'islogin':islogin})


def view_single_product(request, pid):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    product_data = Product.objects.get(id=int(pid))

    return render(request,'singleProduct.html',{'data':product_data,'islogin':islogin,'cart_price':cart_price,'pid':pid})


def all_program(request,view_by):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    view_by = 'created_at' if view_by == 'all' else view_by
    product_data = Product.objects.all().order_by(view_by)
    count = product_data.count()
    if request.method == 'POST':
        searchstring = request.POST.get('searchstring','')
        sortby = request.POST.getlist('sortby')
        sort_by = 'createdon' if len(sortby) == 0 else sortby[0]
        orderby = {'createdon':'created_at','price_asc':'price','price_desc':'-price','name_asc':'name','name_desc':'-name','category_asc':'category','category_desc':'-category'}[sort_by]
        
        if len(searchstring) !=0:
            product_data = Product.objects.filter(name__contains=searchstring).all().order_by(orderby)
        else:
            product_data = Product.objects.all().order_by(orderby)
        count = product_data.count()
        print("searchstring",searchstring,sortby)
        return render(request,'products.html',{'data':product_data,'islogin':islogin,'cart_price':cart_price,'count':count})

    return render(request,'products.html',{'data':product_data,'islogin':islogin,'cart_price':cart_price,'count':count})


def merchandise(request):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    product_data = Product.objects.filter(category='Merchandise').all()
    count = product_data.count()
    return render(request,'merchandise.html',{'data':product_data,'islogin':islogin,'cart_price':cart_price,'count':count})


def supplements(request):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    product_data = Product.objects.filter(category='Supplements').all()
    count = product_data.count()
    return render(request,'supplements.html',{'data':product_data,'islogin':islogin,'cart_price':cart_price,'count':count})

def online_programs(request):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    product_data = Product.objects.filter(category='Online Coaching').all()
    count = product_data.count()
    return render(request,'category.html',{'data':product_data,'islogin':islogin,'cart_price':cart_price,'count':count})


def testimonials(request):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    product_data = Product.objects.all()
    return render(request,'testimonials.html',{'data':product_data,'islogin':islogin})


def blogs(request):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    return render(request,'blog.html',{'islogin':islogin})


def shopping_bag(request):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    cart_data = request.session['cart'] if 'cart' in request.session else {}
    has_item = True if len(cart_data)>0 else False

    return render(request,'bag.html',{'data':cart_data,'islogin':islogin,'cart_price':cart_price,'has_item':has_item})


def add_shopping(request):

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        pid = request.POST.get('product_id')
        price = request.POST.get('price')
        product_data = Product.objects.get(id=int(pid))
        subtotal = round(float(price) * int(quantity),2)
        total = subtotal+2.50
        cart_data =dict(name=product_data.name,image_link=product_data.image_link,quantity=quantity,pid=pid,price=price,subtotal=subtotal,sku=product_data.sku,total=total)
        print("***************************")
        print(cart_data)
        print("***************************")
        request.session['cart'] = cart_data
        request.session['cart_price'] = cart_data['subtotal']
        return HttpResponseRedirect('/shopping')
    

def delete_from_shopping_bag(request, pid):
    """Delete the item from the shopping bag"""
    del request.session['cart']
    del request.session['cart_price']

    return HttpResponseRedirect('/shopping')


def update_bag(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        pid = request.POST.get('pid')
        price = request.POST.get('price')
        product_data = Product.objects.get(id=int(pid))
        subtotal = round(float(price) * int(quantity),2)
        total = subtotal+2.50
        cart_data =dict(name=product_data.name,image_link=product_data.image_link,quantity=quantity,pid=pid,price=price,subtotal=subtotal,sku=product_data.sku,total=total)
        print("***************************")
        print(cart_data)
        print("***************************")
        request.session['cart'] = cart_data
        request.session['cart_price'] = cart_data['subtotal']
        return HttpResponseRedirect('/shopping')

def checkout(request):
    login_data = login_authorize(request)
    cart_price = request.session['cart_price'] if 'cart_price' in request.session else 0.00
    islogin = True if login_data["success"] else False
    cart_data = request.session['cart']
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        street_address1 = request.POST.get('street_address1')
        street_address2 = request.POST.get('street_address2')
        town_or_city = request.POST.get('town_or_city')
        county = request.POST.get('country')
        postcode = request.POST.get('postcode')
        card_number = request.POST.get('cardnumber')
        card_expyear = request.POST.get('expyear')
        card_expmonth = request.POST.get('expmonth')
        card_cvv = request.POST.get('card_cvv')

        print(card_number,card_expyear,card_expmonth,card_cvv,county)

        tokenid = generate_card_token(card_number,card_expmonth,card_expyear,card_cvv)

        payment_done = create_payment_charge(tokenid,cart_data['total'])
        print("payment_done",payment_done)
        del request.session['cart']
        del request.session['cart_price']
        return render(request,'thankyou.html')


    return render(request,'checkout.html',{'data':cart_data,'islogin':islogin,'cart_price':cart_price})



def log_out(request):
    logout(request)