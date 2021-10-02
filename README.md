![Imgur](https://imgur.com/71IA3bY.jpg)

# Luke Duffy Fitness: Fitness and Supplement E-commerce Website

In a world where health, fitness and aesthetics are playing an increasingly important role in our lives, this project was created with the goal of making a fitness e-commerce website for the instagram generation. The website was developed for the target audience of amateur gym goers who increasingly get their gym products from the new generation of fitness 'influencers'. This website is catered for the fans and followers of fitness influencer 'Luke Duffy' and those looking to buy fitness nutrition, merchandise and gym plans from his brand.


 **Click [here](https://luke-duffy-fitness.herokuapp.com) to view the deployed site**


# UX

## User Goals

### Non-registered Users

- Allows guest user to search database for fitness item using search bar available within navbar.
- Allows guest user to clearly navigate to each of the clearly marked four sections of the website, including 'Fitness Programs', 'Supplements', 'Merchandise' and 'Online Coaching'.
- Allows guest user to scroll down home page and access 
the 'Testimonials' page, which will show the customer feedback from each the websites clients.
- Allows guest user to add a product to the shopping bag.
- Allows guest user to click on the 'My Account' button and the 'register' button to sign up to Luke Duffy Fitness, where the guest user will be brought to a seperate web page to input their account details. 
- Allows guest user to click on the shopping bag icon to view products already added to bag and 'Grand Total'.
- Allows guest user to to click on Secure Checkout to purchase the items in their bag, as well as changing the quantities of the the product they wish to purchase.
- Allows guest user to subsequently input debit card details and complete purchase of products.


### Logged In Users

- Allows logged in users to click on the login button where they will be subsequently be brought to the login site of the page and asked to input their details. 
- Allows logged in user to click on the shopping bag icon to view products already added to bag and 'Grand Total'.
- Allows logged 'Super Users' to click on 'My Account' button and click on the 'My Product' button where super users can add, edit and delte the products they want to sell on the website. 
- Allows logged in user to sign out of their profile on Luke Duffy Fitness by clicking on the 'Log Out' button within the 'My Account' section on the Navbar.


# Design 

## Color Scheme

For my website I used the 'Canva' Pallete generator service to ensure a understated, yet clean color scheme for my website.

![Imgur](https://imgur.com/36f0GuB.jpg)

## Database Schema
The website is made up of The site is made up of two apps: fitness_app & 
allauth. They contain the following models: Customer, Product, Account & SocialAccount as shown in the diagram below.

![Imgur](https://imgur.com/xv6gRIZ.jpg)

## Technoliges Used

<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />

<img src="https://img.shields.io/badge/CSS-239120?style=for-the-badge&logo=css3&logoColor=white" />

<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />

<img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />

<img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" />
<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray" />
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" />

<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" />




# Testing and Deployment 

## Code Validators

[![W3C HTML Validator](https://img.shields.io/badge/HTML%20Validator-W3C%20HTML%20Validator-red)](https://validator.w3.org/) 
[![W3C CSS Validator](https://img.shields.io/badge/CSS%20Validator-W3C%20CSS%20Validator-darkred)](https://jigsaw.w3.org/css-validator/) 
[![Pep8 Online](https://img.shields.io/badge/Python%20Validator-PEP8%20online-white)](http://pep8online.com/) 

## Features Testing 

### Navigating the Website
- Click on 'Supplements' button on Navbar
- Does it bring you to correct page?
- Click on 'Mechandise' button on Navbar
- Does it bring you to correct page?
- Click on 'Online Coaching' button on Navbar
- Does it bring you to correct page?
- Click on 'Fitness Programs' button on Navbar
- Does it bring you to correct page?


### Registering 
- Click on 'My Account' button on Navbar
- Does the dropdown menu render?
- Click on 'Register' button.
- Does it bring you login page to thus login in with new account details?
- Does it allow login with the newly created account details?

### Logging In 
- Click on 'My Account' button on Navbar
- Click on 'Login' within dropdown menu
- Does it bring you to login input form?
- After inputting profile username and password, does it render correct corresponding account?
- Does the navbar change to include the 'My Products' and 'log out' buttons?

### Adding item to Basket
- Click on the 'Fitness Programs' button within the Navbar.
- Does website render correct page?
- Click on 'Leak Bulking Program'
- Does correct product page load?
- When clicking on 'Add to Bag' button, does shopping bad correctly update?

### Purchasing items in Basket  
- Click on basket icon in top right hand corner of Navbar. 
- Does website render basket page?
- Can users clear items from basket?
- Can users change the quantity of items they have in their bag by clickon on the + and - buttons?
- Click on 'Secure Checkout' button.
- Does website render payments input webpage?
- Input correct details and click purchase.
- Is 'Thank You' webpage correctly 
### Searching for an Item 
- Input desired recipe keyword into search box within the Navbar.
- Does correspinding product option render correctly?
- If keyword is uncorresponding to recipe in database, does no product item show up in results?

### Logging Out 
- Click on 'Log Out' button on Navbar as an already logged in user
- Does website return user to home webpage?
- Does Navbar change to 'Non-logged in' variant with corresponding buttons? 

## Deployment

- This project has been stored on Github and is built from 
a master branch by one author at the following link: (https://github.com/lukeduffy84/gym_subscription_ms4_2)
- This project has been deployed on Heroku under the following URL: (https://luke-duffy-fitness.herokuapp.com/) 

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