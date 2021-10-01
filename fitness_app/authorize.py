import os
from .models import Customer
import traceback
import stripe
from dotenv import load_dotenv
from django.shortcuts import render
from functools import wraps

load_dotenv()

stripe.api_key = os.getenv('STRIPE_KEY')


def verify_request(f):
    @wraps(f)
    def decorated_function(request, *args, **kws):
        try:
            return f(request, *args, **kws)
        except Exception as e:
            trackerror = traceback.format_exc()
            print("error", trackerror)
            return render(request, 'error.html', {})

    return decorated_function


# login  of user is verified by querying by email and id is returned
def login_authorize(request):
    try:
        token_user = request.session['username'] \
            if 'username' in request.session else ''
        if len(token_user) == 0:
            return {"success": False, "_id": None, 'cart_price': 0.00}
        cart_price = request.session['cart_price'] \
            if 'cart_price' in request.session else 0.00
        check_user = Customer.objects.filter(username=token_user).exists()
        user_data = Customer.objects.get(username=token_user) \
            if check_user else Customer.objects.get(email=token_user)
        if token_user == str(user_data.username) \
                or token_user == str(user_data.email):
            return {
                "success": True,
                "_id": str(user_data.id),
                "username": user_data.username, 'cart_price': cart_price
            }
        else:
            return {"success": False, "_id": None, 'cart_price': cart_price}

    except Exception as e:
        print("error:---", traceback.format_exc())
        return {"success": False, "_id": None, 'cart_price': 0.00}


def generate_card_token(cardnumber, expmonth, expyear, cvv):
    data = stripe.Token.create(
        card={
            "number": str(cardnumber),
            "exp_month": int(expmonth),
            "exp_year": int(expyear),
            "cvc": str(cvv),
        })
    card_token = data['id']

    return card_token


def create_payment_charge(tokenid, amount):
    payment = stripe.Charge.create(
        amount=int(amount) * 100,  # convert amount to cents
        currency='usd',
        description='Example charge',
        source=tokenid,
    )

    payment_check = payment['paid']  # return True for payment

    return payment_check
