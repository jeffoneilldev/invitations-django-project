# Django Full Stack Milestone Project
For my Django Full Stack Milestone Project, I have created a website called “Your Wedding Invitations”.  This website displays a variety of wedding invitation designs where the user can select the one they like and add their own wedding details to it.  They can then order and pay for their selected products through the website.  They can also register and log in to their user account at any time. 

## UX
I want my website to have a modern wedding feel and appearance.  It will have an intuitive interface and present the information clearly on mobile devices as it does on desktop.
A typical user of this app would be looking for the following: 

### User stories

1. **A person not used to navigating websites** will need a simple interface for them to navigate.  They will need to know immediately what options are available to them and what the website has to offer.
2. **A bride (or groom) to-be** would be immediately looking to see the different type/design of invitations that the site has to offer (upon landing on the page).
3. **A returning/registered user** will want to have secured access to the website.  They will want to clearly see what design they have selected and the price they will have to pay.  They would also like to see a their own details in a personalised profile.
4. **A user looking for further information** will be looking for information about the company and an option to submit a query.

### Mock-ups and Database Schema
The mock-ups I used for planning the application are in a "wireFrames" folder inside my images folder under the names **ProjectWireframe_1.png** , **ProjectWireframe_2.png** , **ProjectWireframe_3.png** , **ProjectWireframe_4.png** , **ProjectWireframe_5.png** and **ProjectWireframe_6.png**

My database schema can be found in the "database-schema" folder inside my images folder as **invitationsSchema.pdf**.  I created my database schema in dbdiagram.io.  

### Page template appearance
In the top section of every page I have a navigation bar with page destinations available to the user.  The navigation options change according to whether the user is logged in or not.  More access is granted to logged in users.  A background image of a collage of wedding invitations stretches halfway across the page where the name of the name of the site and a brief introduction underneath takes up the other half.  Underneath is a banner with the site tagline.  Then there is a footer with copyright details. 

This layout is fully responsive on mobile, medium and large screens.

## Features
### Existing Features
- **Nav bar**: provides page selections on every page for easy navigation.
- **Home Page**: On first landing on the app, the user sees a carousel displaying wedding images and comments on what the app is about.  I have a "login" facility which allows the signed in user to access all the facilities of the app.  A new user can register their details and log in also.
- **About Us**: Accessible from every page, this page gives details about the company and what it does.
- **Shop! (Button)**: If logged in, clicking this button will bring the user to the products page where the user can select their desired invitation and add the amount they desire to the shopping cart.  The user MUST be logged in to access this page. 
- **Shopping cart**: Stages the user's selections and gives the option to select more products or go to the checkout page.
- **Checkout**: Displays the proposed order and it's amount and a form for the user to enter their payment details and submit them for payment.
- **Customer Profile**: Displays the logged in user's details.
- **Footer**: Displays the copyright of the app on every page.

### Features Left to Implement
- Order status on submitted orders in the customer profile.
- add a "like" voting system for each invitation.

## Technologies Used
- Django: a Python web framework for building this app.
- Javascript: For Stripe functionality.   
- Bootstrap (startbootstrap.com): For page layout, snippets and grid system.
- Heroku Postgres database.
- Whitenoise for storing static files.
- HTML & CSS for template creation

## Testing
### Code Validation
- HTML 
- CSS 
- JAVASCRIPT 

**Testing as per user stories above:**

- **User story 1:**  Landing on the "Home" page for the first time, the inexperienced user can navigate the page easily because of the simple layout and obvious options available.
- **User story 2:**  The novice in the kitchen will find the ingredients and full cooking procedure to whatever recipe they select.
- **User story 3:**  The regular user can sign in to the app for full access to it's features, including adding their own recipes, editing current recipes or deleting any recipe from the app.
- **User story 4:**  The chef looking for recipe ideas can filter their selections by selecting a cuisine type and/or vegetarian or meaty recipes.  The result of their selection will appear on screen and if they want to see the full details of their selected recipe, they can select the "View Recipe" button.

**Other Testing...**

- All buttons and links have been tested and they all go to their desired destinations.
- Made sure that product, cart and checkout pages are restricted to logged in users only.
- The "User Registration" form works as it should.  When the user enters their details, they are brought to the products page. 
- Payment form for submitting credit card details to stripe was fully tested and is currently failing to accept payment.
- Responsiveness testing on desktop, tablet and mobile devices showed appropriate app layout on each.
- Python debugger for function testing in the console: when trying to figure out what was being inputted and retrieved to and from my functions I used print() etc

## Deployment
This app was developed in AWS Cloud 9.  I used git version control and kept all records of my app in my Github repository.  Before deploying, I made sure to switch my **debug** value to **False** in settings.py.

I took the following steps to deploy my project using **Heroku**:
- Logged in and created a new app called **invitations-django-project**

## Credits
### Content
Bootstrap "Small Business" Theme

### Media
Invitation images from **www..com, .com, .com, www..com, www..com**
Home Page images from **www.com**
To create my database schema, I used **dbdiagram.io**
To create my wireframes I used ****

### Acknowledgements
w3schools.com  
Bootstrap docs
Heroku docs
stackoverflow.com
Slack  
Code institute tutorials and Tutor support.  
My code institute mentor **Maranatha Ilesanmi** for advice throughout the project.



[![Build Status](https://travis-ci.org/jeffoneilldev/invitations-django-project.svg?branch=master)](https://travis-ci.org/jeffoneilldev/invitations-django-project)