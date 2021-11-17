![Imgur](https://imgur.com/71IA3bY.jpg)

# Luke Duffy Fitness: Fitness and Supplement E-commerce Website

In a world where health, fitness and aesthetics are playing an increasingly important role in our lives, this project was created with the goal of making a fitness e-commerce website for the instagram generation. The website was developed for the target audience of amateur gym goers who increasingly get their gym products from the new generation of fitness 'influencers'. This website is catered for the fans and followers of fitness influencer 'Luke Duffy' and those looking to buy fitness nutrition, merchandise and gym plans from his brand.


 **Click [here](https://luke-duffy-fitness-store.herokuapp.com/) to view the deployed site**


# UX

## User Goals

### Non-registered Users

- Allows guest user to search database for fitness item using search bar available within navbar.
- Allows guest user to clearly navigate to each of the clearly marked four sections of the website, including 'All Products', 'Supplements', 'Merchandise' and 'Online Coaching'.
- Allows guest user to add a product to the shopping bag.
- Allows guest user to click on the 'My Account' button and the 'register' button to sign up to Luke Duffy Fitness, where the guest user will be brought to a seperate web page to input their account details. 
- Allows guest user to to click on Secure Checkout to purchase the items in their bag, as well as changing the quantities of the the product they wish to purchase.
- Allows guest user to subsequently input address and debit card details and complete purchase of products.


### Logged In Users


- Allows users to click on 'login button and input their details to succesfully login.
- Allows logged in user to click on the shopping bag icon to view products already added to bag and 'Grand Total'.
- Allows logged in 'Staff' users to navigate to a staff dashboard where they can add, edit and delete the products available on the site. 
- Allows logged in user to sign out of their profile on Luke Duffy Fitness by clicking on the 'Log Out' button within the 'My Account' section on the Navbar.


# Design 

## Color Scheme

For my website I used the 'Canva' Pallete generator service to ensure a understated, yet clean color scheme for my website.

![Imgur](https://imgur.com/36f0GuB.jpg)

## Database Schema
Customer, Product, OrderItem and Order models are implemented 
by the store app. 

The product table stores the basic details of each
product including its name, image, category sku and price. 

A table of order items associates products with quantities and an order.
The order table stores the details of each order including shipping 
details (gathered via the Stripe checkout page), an order id, and an 
optional customer field, populated if the order was placed by 
a logged-in user.

Orders are associated with users via a customer table to allow for additional
fields to be associated with each customer, such as a field for loyalty points.
Although a loyalty points system was implemented, this database structure
means such a feature could be added in the future without the need for
a major refactoring of the overall schema.


## Technoliges Used

<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
<img src="https://img.shields.io/badge/CSS-239120?style=for-the-badge&logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
<img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" />
<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" />

# Testing and Deployment 

## Used Programs to Validate Code

[![W3C HTML Validator](https://img.shields.io/badge/HTML%20Validator-W3C%20HTML%20Validator-red)](https://validator.w3.org/) 
[![W3C CSS Validator](https://img.shields.io/badge/CSS%20Validator-W3C%20CSS%20Validator-darkred)](https://jigsaw.w3.org/css-validator/) 
[![Pep8 Online](https://img.shields.io/badge/Python%20Validator-PEP8%20online-white)](http://pep8online.com/) 



## Testing From User Stories

### Non-registered Users

#### Guest user to search database for fitness item using search bar available within navbar.

Result: Pass :white_check_mark:, all users, regardless of registered/logged in status, can browse through all products, add to bag and make a purchase.

#### Allows guest user to clearly navigate to each of the clearly marked four sections of the website, including 'All Products', 'Supplements', 'Merchandise' and 'Online Coaching'.

Result: Pass,regardless of registered/logged in status, can browse through all sections of website

#### Allows guest user to add a product to the shopping bag.

Result: Pass, guest users can add items to a temporary basket assigned to them, this will stay there even if page refreshed opened in new tab

#### Allows guest user to click on the 'My Account' button and the 'register' button to sign up to Luke Duffy Fitness, where the guest user will be brought to a seperate web page to input their account details.

Result: Pass, guest users can create a username and password to register for the site.

#### Registration Username and Password Requirements 

Result: Pass, attempts to circumvent these requirements returns the following prompts to users,
'This password is too short. It must contain at least 8 characters', 'This password is too common' and 'This password is entirely numerical'

#### Allows guest user to to click on Secure Checkout to purchase the items in their bag, as well as changing the quantities of the the product they wish to purchase.

Result: Pass, guest users can change the quantities for each item as well as move to a secure checkout and payment via stripe

### Logged In Users

#### Allows users to click on 'login button and input their details to succesfully login to website

Result: Pass, website navbar changes also to reflect new options available to logged in account.

#### Allow logged in users to view their entire order history from Luke Duffy Fitness

Result: Pass,logged in users are presented with a 'My Orders' option in the dropdown menu where they can view their order history with the option of an 'order again' button. 

#### Adding Products to the website
- Use the staff login details to add/edit/remove products, 
   - Username: luke 
   - Password: testing321
   Result: Pass, Staff login reveals yellow banner at top of screen that brings staff to dashboard to add/edit/remove products from the website

#### Allows logged in user to sign out of their profile on Luke Duffy Fitness by clicking on the 'Log Out' button within the 'My Account' section on the Navbar.

Result: Pass, website defaults back to guest experience after a user logs out

## Deployment

- Create an account on www.heroku.com and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
- Log the cli in to your heroku account:
```commandline
heroku login
```
- From within a freshly cloned copy of this repo run:
```commandline
heroku create YOUR_APP_NAME
```
- This command creates a Heroku "dyno" to which our project can be deployed. It also creates
a hobby tier postgresql database, which will be used by the project once deployed.


- Once the app is created the command will return 
the url at which the newly created app is running
(e.g. https://YOUR_APP_NAME.herokuapp.com/).
Take note of this url as we will need it in the next step 
as our BASE_URL environment variable.


- Some environment variables must be set in order for the site to run:
  - ENV: Set this value to "PRODUCTION"
  - SECRET_KEY: A long random string. See [django docs](https://docs.djangoproject.com/en/3.2/ref/settings/).
  - BASE_URL: The url of the heroku app we just created.
  - ALLOWED_HOST: Same as BASE_URL but without https:// or any slashes (e.g. YOUR_APP_NAME.herokuapp.com)
  - STRIPE_SK: Your [Stripe secret key](https://stripe.com/docs/keys) (may be a test key eg: sk_test_xxx...)
  - EMAIL_HOST_PASSWORD: Password for email account which will send order confirmation emails.


- Use the Heroku CLI to set these variables:
```commandline
heroku config:set STRIPE_SK="your_stripe_sk"
```
```commandline
heroku config:set SECRET_KEY="your_secret_key"
```
```commandline
heroku config:set ENV="PRODUCTION"
```
```commandline
heroku config:set BASE_URL="https://YOUR_APP_NAME.herokuapp.com/"
```
```commandline
heroku config:set ALLOWED_HOST="YOUR_APP_NAME.herokuapp.com"
```
```commandline
heroku config:set EMAIL_HOST_PASSWORD="YOUR_EMAIL_PASSWORD"
```

- As the project has the django-heroku package installed, environment variables
containing database connection parameters are automatically handled.


- Open settings.py and edit EMAIL_HOST, EMAIL_HOST_USER and EMAIL_PORT
to values that will be compatible with your email provider.


- Push the project files to Heroku:
```commandline
git push heroku master
```

- Heroku detects a django project, deploys the site files, runs pip install using the project's 
requirements.txt and runs the manage.py collectstatic command for us.


- The site should now be live. However, if we click into of the product sections we will get
a 500 error. This is because we still need to run database migrations.


- To run initial database migrations and create a superuser account, open a bash session on
the server by running:
```commandline
heroku run bash
```

- From within this session, run the following commands, following prompts as required:
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```
```commandline
python manage.py createsuperuser
```

- Your deployment of Luke Duffy Fitness should now be fully up and running. Static files are
being served by whitenoise with no additional configuration required.
Log in with the superuser just created to start adding products!


- For a full walk through of a Django/Heroku deployment, see [this video](https://www.youtube.com/watch?v=6DI_7Zja8Zc).


## Media 
- This project has used photos, images and inspiration from the following websites: 

- [Pexels](https://www.pexels.com)
- [Unsplash](https://www.unsplash.com)
- [Google Images](https://www.google.com/imghp?hl=en)
- [1234RF Images](https://www.123rf.com)
- [Rob Lipsett Fitness](https://www.roblipsett.com/)
- [Mike Thurston Fitness](https://thrstofficial.com/)
- [Joe Delaney Fitness](http://www.jd-fitness.com/About)


## Credits and Acknowledgements 
- I would like to say thank you to my mentor Oluwaseun Owonikoko, who has been of immense help and kindness during my coding journey so far.
- I would like the Code Institute tutors, who have shown great patience in assisting me with my many, many questions.
- I would also like to say thanks the code institute studentcare team who have been really helpful in helping me manage the balance of coding with my ongoing University studies