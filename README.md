![Imgur](https://imgur.com/71IA3bY.jpg)

# Luke Duffy Fitness: Fitness and Supplement E-commerce Website

In a world where health, fitness and aesthetics are playing an increasingly important role in our lives, this project was created with the goal of making a fitness e-commerce website for the instagram generation. The website was developed for the target audience of amateur gym goers who increasingly get their gym products from the new generation of fitness 'influencers'. This website is catered for the fans and followers of fitness influencer 'Luke Duffy' and those looking to buy fitness nutrition, merchandise and gym plans from his brand.


 **Click [here](https://luke-duffy-fitness.herokuapp.com) to view the deployed site**


# UX

## User Goals

### Non-registered Users

- Allows guest user to search recipe database using search bar available under the navbar.
- Allows guest user to visit 'All Recipes' section and examine all recipes uploaded so far to the database by clicking on the  'all recipes' button on the navbar. sbsbsbbsbsbhubu
- Allows guest user to hover over an image of a recipe to see display of recipe title.
- Allows guest user to click on the image of a recipe and subsequently be brought to the full recipe page, which will display more information about the recipe including the ingredients and instructins for that particular recipe.
- Allows guest user to see the 'about us' section, which gives a quick general history and overview of 'Cook Club' while providing a convient 'Sign Up' button that directs guest user to registration page.
- Allows guest user to click on the 'login/register' button in the navbar and be brought to the registration page where they can sign up for a Cook CLub account. 

### Logged In Users
- Allows click on the 'Log In / Register" button where they will be subsequently be brought to the registration page, where they will be given the option to 'login' if they are already a member of the site.
- Allows logged in users to add their own recipes by clicking on the 'Add recipes' button within the navbar. On clicking the button, they will be taken to a page where they will be presented with five seperate input fields that allows users to upload a Recipe Name, Image URL, Required Ingredients, Cooking Instructions and finally select a radio button option for which meal the recipe in question pertains to.
- Allows logged in users to check which recipes they have uploaded to Cook Club by clicking on the 'My Recipes' button within the navbar. On clicking the button, they will be taken to a seperate page where they will be presented photos of each of the recipes they've uploaded and the option to visit each recipe page individually. 
- Allows logged in users to edit and delete the recipes they've uploaded through the 'edit' and 'delete' buttons at the bottom of their own recipes. 
- Allows logged in users to sign out of their profile on Cook Club by clicking on the 'Log Out' button within the navbar.


# Design 

## Color Scheme

For my website I used the 'Canva' Pallete generator service to ensure a understated, yet clean color scheme for my website.

![Imgur](https://imgur.com/36f0GuB.jpg)


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

### Purchasing Supplement
- Click on 'Supplements' button on Navbar
- Does it bring you to correct page?
- Hover over image of recipe to display each recipe title
- click on recipe image
- Does it bring you to correct page for corresponding recipe?

### Registering 
- Click on 'Log In / Register' button on Navbar
- Does it render the registration inputs?
- Submit details
- Does it bring you login page to thus login in with new account details?
- Does it allow login with the newly created account details?

### Logging In 
- Click on 'Log In / Register' button on Navbar
- Click on 'Already a member? Login' button at bottom of Registration page
- Does it bring you to login input form?
- After inputting profile username and password, does it render correct corresponding account?
- Does the navbar change to include the Cook Club 'add recipes', 'my recipes' and 'log out' buttons?

### Adding a Recipe
- Click on 'Add Recipes' button on Navbar
- Does website render correct form?
- On clicking 'submit' button, does website bring user back to home page to view newly added recipe?
- Does it render image correctly when recipe is added?
- When clicking on image, does it retrieve correct inputted recipe details?

### Editing a Recipe 
- Click on 'My Recipes' button on Navbar or click on an image of recipe user has already uploaded from their own account
- Does 'Edit' button appear at the bottom of the page?
- After clicking button, is the 'Edit Recipe' page rendered correctly with already inputted details rendering also?
- After editing text/images, are requested changes correctly made to recipe data after clicking the 'submit' button?

### Deleting a Recipe 
- Click on 'My Recipes' button on Navbar or click on an image of recipe user has already uploaded from their own account
- Does 'Delete' button appear at the bottom of the page?
- After clicking button, is user returned correctly the 'My Recipes' page?
- Has seleted recipe been correctly removed from 'all recipes' and 'my recipes' database?


### Searching for a Recipe 
- Input desired recipe keyword into search box on Cook Club webpage
- Does correspinding recipe option render correctly?
- If keyword is uncorresponding to recipe in database, does no recipe show up in results?

### Logging Out 
- Click on 'Log Out' button on Navbar as an already logged in user
- Does website return user to login webpage?
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
- [Rob Lipsett](https://www.roblipsett.com/)
- [Mike Thurston](https://thrstofficial.com/)

## Credits and Acknowledgements 
- I would like to say thank you to my mentor Oluwaseun Owonikoko, who has been of immense help and kindness during my coding journey so far.
- I would like the Code Institute tutors, who have shown great patience in assisting me with my many, many questions.
- I would also like to say thanks the code institute studentcare team who have been really helpful in helping me manage the balance of coding with my ongoing University studies