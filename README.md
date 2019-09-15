# Django Full Stack Milestone Project
For my Django Full Stack Milestone Project, I have created a website called “Your Wedding Invitations”.  This website displays a variety of wedding invitation designs where the user can select the one they like and add their own wedding details to it.  They can then order and pay for their selected products through the website.  They can also register and log in to their user account at any time. 

## UX
The main demographic for this kind of website would be women in their late 20s / early 30s.  I want to appeal to this audience using a modern wedding feel with a pink and purple colour scheme for appearance.  It will have an intuitive interface and present the information clearly on mobile devices as it does on desktop.

**A typical user of this app would be looking for the following: **

### User stories

1. **A person not used to navigating websites** will need a simple interface for them to navigate.  They will need to know immediately what options are available to them and what the website has to offer.
2. **A bride (or groom) to-be** would be immediately looking to see the different type/design of invitations that the site has to offer and what the company is about.
3. **A returning/registered user** will want to have secured access to the website.  They will want to clearly see what design they have selected and the price they will have to pay.  They would also like to see a their own details in a personalised profile.
4. **A user looking for further information** will be looking for information about the company and an option to submit a query.

### Mock-ups and Database Schema
The mock-ups I used for planning the application are in my "projectPlan" folder inside my 'static' folder under the names **ProjectWireframe_1.png** , **ProjectWireframe_2.png** , **ProjectWireframe_3.png** , **ProjectWireframe_4.png** , **ProjectWireframe_5.png** and **ProjectWireframe_6.png**

My database schema can be found in my "projectPlan" folder inside my 'static' folder as **invitations_dbSchema.pdf**.  

### Page template appearance
In the top section of every page I have a navigation bar with page destinations available to the user.  The navigation options change according to whether the user is logged in or not.  More access is granted to logged in users.  A background image of a collage of wedding invitations stretches halfway across the page where the name of the site and a brief introduction underneath takes up the other half.  Underneath is a banner with the site tagline.  Then there is a footer with copyright details. 

This layout is fully responsive on mobile, medium and large screens.

## Features
### Existing Features
- **Nav bar**: provides page selections on every page for easy navigation.  
- **Home Page**: On first landing on the app, the user sees a carousel displaying wedding images and comments on what the app is about.  I have a "login" facility which allows the signed in user to access all the facilities of the app.  A new user can register their details and log in also.
- **About Us**: Accessible from every page, this page gives details about the company and what it does.  Each invitation image used on the page is a link to the 'products' page (or log in page if not logged in).
- **Shop! (Button)**: If logged in, clicking this button will bring the user to the products page where the user can select their desired invitation and add the amount they desire to the shopping cart.  The user MUST be logged in to access this page. 
- **Shopping cart**: Stages the user's selections and gives the option to select more products or go to the checkout page.  If the user is logged in, the amount of cart items the user has selected is displayed in the nav bar.  The cart can be accessed by clicking on the nav bar link.
- **Checkout**: Displays the proposed order and it's amount.  Underneath is a form called "Your Wedding Information" for the user to enter their details.  Below that, there's another form for the user to enter their payment details and submit them for payment.
- **Customer Profile**: Displays the logged in user's details.  I also added an "order status" where I can manually update it to let the user know the status of their order.
- **Footer**: Displays the copyright of the app on every page.

### Features Left to Implement
- Automated order status on submitted orders in the user's customer profile.
- add a "like" voting system for each invitation.

## Technologies Used
- Python / Django: a Python web framework for building this app.
- Javascript: For Stripe functionality.   
- Bootstrap (startbootstrap.com): For page layout, snippets and grid system.
- Heroku for Postgres database and deployment.
- Whitenoise for storing static files.
- HTML & CSS for template creation.
- Stripe API for credit card payments.

## Testing

### Travis
I connected my Github repository to Travis for continuos testing.  Whenever my code updated, a new build would begin in Travis and turn green if my code passes all tests.  The Travis link at the end of this README displays the current testing status of my app.  This current build is "Passing".

### Code Validation
- HTML validated using W3C Markup Validation Service.  DOCTYPE and html tags are extended from base.html to other pages.
- CSS was validated using Jigsaw with no errors found.
- JAVASCRIPT was validated using JSHint.  It says I have 2 undefined variables, $ and stripe.  However, jQuery and stripe are loaded/referenced already in my checkout.html (and my base.html via head_js).

**Testing as per user stories above:**

- **User story 1:**  Landing on the "Home" page for the first time, the inexperienced user can navigate the page easily because of the simple layout and obvious options available.
- **User story 2:**  The bride or groom will instantly see a carousel with positive comments and images about the website.  The 'about us' page is accessible from the nav bar.
- **User story 3:**  The returning user can log in to their account and access all the features of the website securely.  They can also view their customer profile while logged in.
- **User story 4:**  This user can go straight to the "About us" page for further information and an email address they can contact.

**Other Testing...**

- All buttons and links have been tested and they all go to their desired destinations.
- Made sure that product, cart and checkout pages are restricted to logged in users only.
- The "User Registration" form works as it should.  When the user enters their details, they are brought to the products page. 
- Payment form for submitting credit card details to stripe was fully tested and is currently failing to accept payment.
- Responsiveness testing on desktop, tablet and mobile devices showed appropriate app layout on each.
- Python debugger for function testing in the console: when trying to figure out what was being inputted and retrieved to and from my functions I used print() etc

## Deployment
This app was developed in AWS Cloud 9.  I used git version control and kept all records of my app in my Github repository.  Before deploying, I make sure to switch my **debug** value to **False** in settings.py.

I took the following steps to deploy my project using **Heroku**:
- Logged in and created a new app called **invitations-django-project**
- I selected the Postgres addon and copied the value of DATABASE_URL from config vars.
- Back in my Terminal, I installed dj-database-url and psycopg2.
- I imported dj_database_url into my settings.py
- I created an env.py file to store my SECRET_KEY and DATABASE_URL and STRIPE values.
- I cut the value of the SECRET_KEY from settings.py (replaced with os.environ.get(..)) and put it into the config vars of my Heroku app.
- In Terminal I put ./manage.py makemigrations then migrate.
- I installed gunicorn and created a Procfile.
- I updated my requirements.txt file.
- Then I added the name of my app in heroku to ALLOWED_HOSTS in settings.py.
- Back to Heroku, Deploy, Connect to Github and connect to my repository name.
- Manual deploy and deploy branch.  Enable automatic deploys.
- Here is the live link to my heroku app **https://invitations-django-project.herokuapp.com/**

## Credits
### Content
Bootstrap "Small Business" Theme

### Media
Invitation images from **https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR_tIoCOlskiyQXfTwCs9rQyfC41xRCTnhacUzakYqzGl0Rl3Z, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpDzwDtDB5HL6C3Y-M0CCFNp3jwQxZiDv0mppAY-Hbf-s5ZyMg, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTVChEqUYRpD8p2Z5Q-6Sp9P0Hcm5YCaFZeprln5l2I6C0C6aD&reload=on, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpDzwDtDB5HL6C3Y-M0CCFNp3jwQxZiDv0mppAY-Hbf-s5ZyMg, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCDDsXKAGsXG9rBCCjQM7t0jBhoW3_FZZcDJKMV0ZgoEVeRnpQ**

Page header image from **https://www.weddinginvitations.org.uk/wp-content/uploads/2016/07/montage.jpg, https://www.google.com/**

Carousel images from **http://cadldg.com/wp-content/uploads/2019/01/photo-collage-thank-you-cards-wedding-multi-card-personalized-template-thanks-for-invitation-online.jpg**, https://junebugweddings.com/wedding-blog/wp-content/uploads/2014/12/American-Wedding-Marketplace-Invitation-Collage.jpg**, https://i.pinimg.com/originals/a4/50/7d/a4507d7a26566dc7a792a5f0442858b5.jpg**

To create my database schema, I used **dbdiagram.io**

To create my wireframes I used **balsamiq**

### Acknowledgements
w3schools.com  
Bootstrap docs
Heroku docs
Stripe API
stackoverflow.com
Slack  
Code institute tutorials and Tutor support.  
My code institute mentor **Maranatha Ilesanmi** for advice throughout the project.



[![Build Status](https://travis-ci.org/jeffoneilldev/invitations-django-project.svg?branch=master)](https://travis-ci.org/jeffoneilldev/invitations-django-project)