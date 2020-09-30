# Sweet_moments_milestone
click [here](https://sweet-moments.herokuapp.com/) for the deployed project. 
Sweet Momens is my final milestone project. It is a Full-Stack Django Frameworks ecommerce store. Users can browse for vegan sweets and make an order , submit a payment via Stripe. All products and images were added through the Django admin dashboard. 

Please note - to make a payment, you must make an order as a registered user and at the checkout form you can put in the card number 4242424242424242


## Goal
The page is for users who are seeking out Vegan friendly confectionary. 

## User Stories:
##### Accounts:
1. As a customer: I need to authenticate myself in order to see my past purchases and private information
1. As a customer: Registering for an account means I must be shown errors im making , so I can fix them as fast as possible

#### Products
1. As a customer: When searching for a product , I need to be presented with all relevant choices to find what im looking for. 
1. As a customer: I must be informed of any benefits or discounts from the company. 

#### Payment
1. As a customer: When making a payment I need to be able to input my card details and have appropriate messages being displayed to me. E.g error , success.
1. As a customer: Once Ive made a purchase I need verification of that purchase as soon as possible as to avoid contacting customer service/support. 
#### Vegan Diet;
1. As a vegan customer:There must be a clear indication upon entry to the page that the site is suitable for my diet.

## Purpose
The purpose of the website is to show how, with the use Django frameworks ,Python and Stripe API you can create a fully functional e
commerce site.

## Design
The design is very simplistic , yet colourful. As a sweet store the majority of the content is bright and colorful. With that in mind I wanted to have a clean white background and navbar. 
The navbar is fixed so it provides fast navigation for the user no matter their location on the site. 

## Mockup
![index](https://i.ibb.co/cYy9W9G/sweethome.png)
![products](https://i.ibb.co/vX6ZvDQ/sweetproduct.png)
![cart](https://i.ibb.co/92cvsNw/sweetcart.png)
I used "Miro" to create a wireframe .

## Features

### Navbar:
The Navbar contains a search input for keywords that a user may want to search. Along with this there is a dropdown 
list of categories that the user can search via. If the user is logged in successfully the accounts icon will display a dropdown link item that will 
give them the option to redirect to the profile. If the user is not logged in they will only be given a dropdown choice of register or login. 

### User Registration:
This features supplys the customer with their own personal profile where all of their private details are stored, e.g shipping info and past purchases. 

### Cart: 
The user can select products which they can add to a cart. There , all of the product information is stored. In this window the user can see product name, quantity , weight and subtotal price fields. 

### Stripe Checkout:
The user must complete a checkout form and provide all relevant details regarding shipping, contact and personal information. Once this is complete the user can input there card details and submit the payment. Upon successful payment the user will be redirected to a successs page with a review of their order. 
From this window the user can redirect to their profile page and view all order history on that account. 

### Coupon:
A coupon code is displayed on site which the user can apply at the checkout page. The grand total and discounted total is displayed to show the user what their savings are. 

## Technologies & Languages Used:
1. HTML5
1. CSS
1. Bootstrap
1. Javascript
1. jQuery
1. Github
1. Stripe
1. Postgres/Sqlite3
1. Heroku
1. Django
1. Python3
1. Font Awesome
1. AWS 
1. Boto3

## Testing
### Browsers
The website was tested on Google Chrome, Firefox, Internet Explorer and Safari. The pages defensive design displayed on all browsers. 

### Registration & Login
The website was tested manually regarding registering users. All registration was successful each time. The sites admin confirmed the presence of the created user aswell as the successful login.
Upon successful registration the user is redirected to the home page to continue their shopping as normal. Once logged in, the user has the option to enter their profile page. Here is where they can input , edit/update their personal information. Along side that is a tab with all of their order history details if said user has some. 

### Updating Personal info
On the profile page the user can input their personal details and save. If the user needs to update or edit any of these details they can do so successfully. 

### Log out 
Once the logout link is clicked the user is successfully redirected to the signout html template which prompts them on whether or not they are sure, if so the user may select proceed and log out. All cart items that may have been selected are cleared in this moment successfully. 

### Products
The purchase functionality was tested manually on many different viewports and devices. The user can successfully view products. Once a product is clicked on the page redirects to a product detail page. Here the option to add to cart becomes available. A choice of "weight" selection is offered to the user which once selected , successfully increments the price depending on said weight. 

## Submit Payment To Stripe
At the checkout form, if any field is missing the user will not be able to submit the payment. The user is alerted about the required fields that must be filled. 

Once the checkout form is filled and the user clicks "complete payment" , the page redirects with a thank you message, order numnber and order review. Please refer to the stripe events to see payment succeeded. 
![stripe](https://i.ibb.co/8NwLQ5J/stripeproject.png)



## Validators
1. W3schools HTML and CSSS validators were used. 

## Deployment
* The App is running live on Heroku. 
* Go to your Heroku account and __create an app__ with chosen name.
* Click on the __resources__ tab and add __Heroku Postgres__ 
* In you __settings__ tab you must navigate to you __Config Vars__
* Here you will see your __DATABASE URL__ which you must replace the current one with in your project 
level __settings.py__ file. 
* Run all migrations using command __python3 manage.py makemigrations__
* Create a new __superuser__
* create a __Procfile__ and inside set __web: gunicorn sweet_moments.wsgi:application__
* In Herokus dashboard click the "deploy" tab and select Github as your method. Search your repoistory and select it. 
* In the __Reveal Config Vars__ section set the following vars:
AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY ,DATABASE_URL ,DISABLE_COLLECTSTATIC <1>

* In your Heroku dashboard - click the "Deploy" tab, go down to the "Manual Deploy" section, select the master branch of your repo, and "Deploy Branch".

Dont forget to add your Heroku app url to the settings.py file:

__ALLOWED HOSTS = ['your_heroku_app_name_url','local]__

## Content
All images were provided by "unsplash.com"











