# TriFlake Studio

TriFlake Studio is an MVP website for a creative design agency. The aim is to create a minimum viable product to showcase the work of the agency, while creating a unique user experience for a graphic design company, a user sign up section.
This website also deploys all my course learning to date with the Code Institute. The elements I used in creating this website are all practical techniques I have been learning, working through the modules of the Full Stack Developer Bootcamp.

You can view the deployed website here: <a href="https://triflake-studios.herokuapp.com/home" target="_blank">triflakestudio.herokuapp.com</a>

<img src="/media/triflake-studio.jpg" title="trifkale studio logo" height="300">

------

## Table of Contents:

1. [Project outline](#project-outline)
2. [UX](#ux)
3. [Features](#features)
4. [Technologies](#technologies)
5. [Building and Deployment](#building-and-deployment)
6. [Testing](#testing) 
7. [Future Development](#future-development)
8. [Credits](#credits)
19. [Acknowledgements](#Acknowledgements)


## Project Outline
The website has  a duel purpose. It was created for me to showcase my work as a web developer. The elements I used in creating this website are all practical coding techniques I have been learning, working through the Full Stack with Django modules of 
the Code Institute Bootcamp, with Kerry College in the winter of 2019/2020. The second purpose, is to showcase my graphic design skills, as all the graphic elements in the website have been designed by over the past few years, they are all actual projects and clients I have worked for.

***
## UX

The main function of the website is to create a visible presence for TriFlake Studio, a creative design studio.
To create the MVP I used the principles of Lean UX:

<img src="/media/leanux2.jpg" title="Cycle of Lean UX" height="300">

 - Outcomes, assumptions, hypotheses
 - Design
 - Create MVP
 - Research and Learning

The outcome was to create an MVP website for a creative design company,  with the expected elements e.g. portfolio, contact, about pages, but with some new features. 
With two types of users in mind, the graphic design company themselves, and their clients, I made assumptions and hypotheses about the elements that would be needed, 
common features, and new features that might appeal to both their existing clients but also to a new customer base. 

- *Strategy Plane* : Create a clean bright feel-good visually appealing website, with calls to action to engage new and existing customers.
    - User 1: TriFlake Studio - to showcase the work of the studio and create call to actions to easily contact the studio through the website.
    - User 2 : Clients - to view previous work of the studio and be able to contact them easily.
    - Research: creative design websites vary greatly, from extremely minimalist, to overly flashy. Surprisingly the majority of sites I looked at during the research phase were not great. They were either too brash and garish, or actually neglected looking, not a good look for a design studio! Some were so minimalist, to the point of being rude (as if to say “If you haven’t heard of us, then you are a nobody”).
    - The best design option was to reflect the mood of the studio, which is bright, bubbly, modern, yet fun. Minimalist fun, with a love of triangles. So focus was on bold bubbly headings, minimal content, with triangles reflecting the logo.
    - This website would have 2 features that did not exist on most creative design websites. The first is a shop page, where you can directly book consultations. The second is a user section with exclusive access for signed up members.

---
- *Scope Plane* : Creation of a MVW, minimum viable website with mixed content that has the potential to grow.
    - Needs: reflect the mood and work of the studio, with positive, enticing call to actions
    - Important features:
        - Impactful landing page that immediately reflects the modern playfulness of the studio.
        - Contact form - easy to fill in form
        - Portfolio and clients - visible work and client list to prove experience and competence
        - Shop - directly bookable consultancy sessions. Unusual for a design studio, but can help them grow as a forward thinking and approachable company. This could be a potential area of growth for the studio, in proposing different types of consultancy sessions, at different prices. It may appeal to SMEs with tight budgets and limited timelines, knowing upfront and directly how much sessions will cost. This could also help with cash flow, with prepaid work sessions providing instant payment, as opposed to the normal approach of chasing cheques. 
        - Client sign in area - again unusual for a design studio, but providing existing and potential customers with the feeling that they are getting more value for their money than just the consultancy or design work. This is another huge area of growth, not just for building potential customer base, but developing the studios reputation as resourceful, approachable, and as leaders in design innovation and trends.
---
- *Structure Plane*: A minimal website, with simple content yet visually stunning. The website needed to reflect the mood and work of the studio. 
With prominent calls to action, portfolio and shop features and sign in area. 

---
 - *Skeleton Plane* : Top priority is awareness about the studio and its services. Simple shapes and colours, give a sense of unity with playfulness. Minimalist but with bright colours and large triangles feature throughout the website, to play on the name and the logo. 
    - Support and connect with the project, through call to actions and links
    - Very structured navbar, with footer just on certain pages.
    - Deliberate color scheme, using the yellow, purple and blue that is in the logo.


Using UX strategies to develop the features and schema of the website , I first used post-its to build the initial wireframe, and develop the necessary features. I focused on the most prominent and important features I had listed in the strategy and scope research. I then developed the website layout, reframing the posits until I had a clearer idea of the website page layouts with links and buttons. 

<img src="/media/landing-page-2.jpg" title="Cycle of Lean UX" height="300">

The next step was to develop the post-its groundwork into a paper wireframe of the website in both mobile and desktop view. Working on each page and section, developing the different placement and features, call to actions, and more.

You can see a pdf of my process here: [ux-process mockup](https://github.com/OrlaBr/triflake-studios/blob/master/media/ux-wireframe.pdf).

---

- *Colour and Style* :

Using the visual identity of TriFlake Studio to develop a colour theme. I originally had a variety of colours to choose from, but narrowed down the selection to this:
You can see the full colour scheme I had to work with here: [colour-scheme](https://github.com/OrlaBr/triflake-studios/blob/master/ux/colour-scheme.jpg), but in the end I chose these colours:

<img src="/media/colours.jpg" title="Colour scheme for TriFlake Studios" height="100">

I used Google Fonts 'Noto Sans', for the main body of the text, and 'Titan One' for the h1 and h2, for impact. It mirrored the visual identity of TriFlake Studio to have large bold colourful headings.
I then created more visual mockups using the online graphics platform 'Canva'. I developed the mobile view first, and when I was happy with that, I created the desktop version.

<img src="/media/triflake-studio-designs.jpg" title="Screenshot of mobile and desktop view of website" height="300">


You can see the [mobile mockup here](https://github.com/OrlaBr/triflake-studios/blob/master/ux/triflakestudios-mobile-mock-up.pdf)
and [desktop mockup here](https://github.com/OrlaBr/triflake-studios/blob/master/ux/triflakestudio-desktop-mock-up.pdf)

---

 - *Surface Plane* : Using Canva as a mock up tool, I was able to create an accurate depiction of what I wanted the final website to look like, the colour schemes, placement, and fonts. I also decided to use font awesome icons, as these are now universally known. I also revised the text, to be included in the final web design. 
I made small changes from the mock up when coding, as I felt some small changes need to be made. Changes include:
    - Having separate about and contact pages. The navbar was getting too cluttered with all the different pages, so I decided to create a scroll down landing page that had all the basic information about the studio eg, services, about, contact. This is in keeping with my mobile first approach, and having all the relevant important information on the first scrollable page. This  also gave me more room to showcase the portfolio, shop, sign in area and shopping cart in the nav bar. 
    - Having the footer on every page. I felt the footer on every page was too repetitive and cumbersome, and instead placed it on just the landing page, and other important pages. These are also pages that had a bulk of information on them, with a scroll element in it, so you could access important links without having to scroll back up to the navbar or go back to relevant pages.

***

## Features

### For Users:

#### User 1: TriFlake Studio
 - Easily contactable through online contact form
 - Showcases work and clients in portfolio section
 - Sell workshops through the shop page
 - Provide extra service for signed up users

#### User 2: Clients
 - Able to view the company - about, and view portfolio
 - Able to contact the studio easily
 - Can create a user account 
 - Has access to exclusive features though signed in user section
 - Feels they can contact the studio easily through a more specific specialized contact form.
 - User can navigate the website using the top nav bar on large screens and hamburger toggle side navbar
 - Can purchase workshops through site with Stripe - secure payments system,

---

#### Breakdown of  features

 - Contact Us Form- The website goal is to create a visual presence for TriFlake Studios online. Research showed that some graphic design studios placement of the contact form was like an after though. They showcased all their work first, almost like a wall for blasting design work at you, and then did a call to action. I designed this website the opposite, by putting the contact form at the front landing page, I made the website more approachable. Being based in Kerry, the likelihood is of working with smaller SMEs on regular projects, rather than big flash campaigns for big companies. Being approachable was more important.  
 - Register and log in - getting users to sign up to the website, is a new feature not seen on many design websites. It has great potential to develop a relationship with existing and new clients. Offering freebies, resources, and a special contact form develops a more trusting and long term relationship with the customer.
 - Shop- and other features that have great potential, especially for the cash flow of the studio. Again, this could be developed to offer a variety of products and consultancy, especially within the developing remote working world.


***

## Technologies

 - HTML - HTML5
 - CSS - CSS3
 - Bootstrap - framework
 - Javascript - bootstrap javascript for functionality
 - Gitpod - to write and develop the website
 - Github - to host the project in an online repository
 - Django - to build the python framework
 - Heroku - to host the website
 - Stripe -  payments technology

*Other web applications used:*

 - Canva - to create a detailed wireframe
 - Adobe Photoshop - to edit the photographs
 - Google Fonts - stylesheet linked to use customize fonts
 - Font Awesome - stylesheet linked to use customize icons


*** 

## Building and Deployment

#### Website Build
The website was built using Gitpod, using a Django framework to build up the different sections of the website. I relied heavily on Code Institute tutorials 
in creating the basic build, following the principles of the ecommerce and blog tutorials. One of the reasons 
I followed the tutorials again was to make sure I understood them fully, especially in relation to using building up multiple Django apps within one project. 
Once I had the basic functionality working, I was able to personalize it to suit my project.

***
#### Sections Build
My website was developed using Gitpod and hosted using Github, generated from a template created by the Code Institute, and then deployed directly from the master branch. Regular changes were made and all updates were then committed to the master branch.
Using the django framework,  I created and developed the website in stages. Building the first app ‘ecommerce’ and then each section of the website in turn. Django has a built in database sqlite, which was used to build the website. I built the following django apps:
 - Ecommerce - main app
 - Static - css stylesheet and stripe javascript 
 - Accounts - user section
 - Products - shop section
 - Checkout - shopping section created using stripe for payments
 - Cart - shopping process
 - Media - images for the website and shop
 - Pages - static pages such as the home and portfolio pages
 
 *Other install requirements:*
 - Pillow -  a Python Imaging Library. This adds image processing capabilities to my Django project.
 - WhiteNoise -  allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service.
 - Stripe -  installing stripe and adding the Stripe keys as environment variables, and updating the settings file to extract those variables into the Django project.


Github is a great resource for deploying web applications but as it only hosts static files it cannot be used to host a dynamic application, 
in this instance, with database functionality. It is necessary to deploy to a cloud platform that can display the project correctly. 
In this instance I used Heroku. Once I had the basic structure of the app complete I deployed to Heroku. This way, I could make sure any changes 
I made and viewed in Gitpod could be successfully transferred to public viewing in Heroku.

***
#### Heroku

Before deploying to Heroku, I add a few more steps to do. I needed to transfer all the files in my database  from django's sqlite to Heroku PostRes.
You do this by setting the keys and values in Config Vars, in the Heroku Platform, and also your settings.py file

```  
Heroku - TrifkaleStudioAdd - Settings - Reveal Config Vars
```

Add the following:

```
PostRes Key <add if/else statement to settings.py to use either the sqlite or the postgres database> 
Add sqlite ‘SECRET_KEY’
Add ‘STRIPE PUBLISHABLE' key
Add ‘STRIPE_SECRET’ key

```

Its also important to do the following actions, create requirements.txt, and a Procfile
```
pip3 freeze --local > requirements.txt 
echo web: python run.py > Procfile 
```
I also changed the deployment method settings in Heroku . I connected my account to Github, and set the deploy to automatic, so each push I make in gitpod to github would automatically push to heroku too.
```
Automatic deploys from  master are enabled
```
***

## Testing

#### Manual Testing
This web application has been manually tested with different scenarios that the user may experience.
*HomePage*
 - Homepage - Click on the brand logo in the navigation bar. Be directed back to ‘home’ 
 - Navigation- Click on each of the nav items in desktop and mobile view
 - Contact Form - checked all fields for required
 - Sign Up links - connect to register page
 - Footer - check links work
 ```
 Submitted the form with an invalid email address to verify that a relevant error message appears
 Submitted the form with all inputs valid and verify that a success message appears.
 ```
*Portfolio Page:*
 - Pictures present correctly in desktop and mobile view. Links work correctly
*Shop Page:*
 - Products display correctly in mobile and desktop view
 - Shopping cart works correctly - adding quantities, displays number of items in the shopping cart.
 - Contact us link works
 - Shopping cart - checked updating quantities, adding to cart, and filling out payment systems are working correctly.
*Login Page:*
 - Log in working correctly, links to forget password and join now also working
 - Checked forgot password links
*Sign in Page:*
 - Created a new user account : <janedoebooks29> to check the process and access the user section as a customer: <password: JD_20!0?>
 - Checked downloads work and contact form worked
 - Proofreading - all text added to a Google doc for spelling and grammar check.
 - Checking Links - tested all links including: relative, absolute, text, bookmark, e-mail, external
 - Validating Forms
 
_Dev Tools_:
These tools were used throughout the project build.
* Google Chrome DevTools ~ used throughout the project for testing and debugging
* Firefox Developer Tools ~ used throughout the project for testing and debugging

_Code Validation:_
    I used a few online validators and formatters to check the code at regular intervals throughout the build.
* <a href="https://validator.w3.org/" target="_blank">W3C HTML Validator</a> 
* <a href="https://validator.w3.org/" target="_blank">W3C CSS Validator</a> 
* <a href="https://jshint.com/" target="_blank">JSHint</a> - Javascript validator
* <a href="http://pep8online.com/" target="_blank">PEP8</a> - Python validator
* <a href="https://chrome.google.com/webstore/detail/chromelens/idikgljglpfilbhaboonnpnnincjhjkd?hl=en" target="_blank">Chrome Lens</a> - Accessibility validator


_Elements testing_

| Feature      	| Elements                             	| Tested 	| Working 	 |
|--------------	|--------------------------------------	|--------	|---------	 |
| Navigation    | html links                         	| ✔      	| ✔       	|
| Contact Forms | Fill and send                         | ✔      	| ✔       	|
| HTML Links   	| page links                        	| ✔      	| ✔       	|
| Database      | data presenting correctly         	| ✔      	| ✔       	|
| PRODUCTS      | DATABASE OPERATIONS                   	                     |
| Add  	        | ability to add products               | ✔      	| ✔       	|
| Select        | ability to add and edit to cart       | ✔      	| ✔       	|
| buy   	    | ability to pay for items in cart      | ✔      	| ✔       	|
| USER  	    | AUTHENTICATION                        |        	|       	 |
| Register  	| Create a user account                 | ✔      	| ✔       	|
| Sign in 	    | ability to sign in user section       | ✔      	| ✔       	|
| Password Reset| ability to reset password             | ✔      	| ✔       	|



<img src="/media/cross-browser.jpg" title="triflake studios website on different devices" height="300">

| Testing   | Cross-browser/ cross-device           |
|---------	|--------------------------------------	|
| Browser   |Chrome, Firefox, Safari, Opera         |
| Device    | Mobile, Tablet, Desktop               |
| Systems   | iOS, Android, Linux                   |


#### Other Tests 

*Stripe*
 - A key element of this project was to create a working shopping cart. For this I used Stripe. It was installed in the build phase in Gitpod, and I did a preliminary test before adding my products, and wentt through the process of filling out the payments form, using Stripes own test credit card.
```
    Stripe Credit Card: 42424242424242  CCV No: 111
```
 - I successfully bought an item
<img src="/media/test-stripe-payment.jpg" title="screenshot of strip dashboard with payment" height="100">

 - And my success message worked
<img src="/media/test-stripe.jpg" title="screenshot of strip dashboard with payment" height="100">

*Products*
 - I ran a successful test when building the products app to check the database was working successfully

```
class ProductTests(TestCase):

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
```

<img src="/media/products-test.jpg" title="screenshot of strip dashboard with payment" height="100">

***

#### Pre Deployment Snag List:
I had  many bugs to fix during build and pre deployment.

*Major fails included*

 - Building the Accounts Folder: I imported the accounts app from a previous project, and double checking all the settings and url code was correect, I could not get the app to work. It turns out I had put the backends.py file into the wrong folder. 
 - After building the main apps for the project, the accounts, the products, cart sections, 
    I wanted to create the home page and and work on the navbar, so I could get working links, 
    and easily move to one page or another before working properly on the styling and customized css. REading through different documentation online in django, and Stackoverflow, 
    I created what I thought was the correct path to building the home 'pages' app. but after much frazzled thingking, I went back over the Stack Overflow questions/answer I had followed, and realised it was an old post,
    using older version of django, and I had to take several steps back in my commit history, to fix the error. Learning the benefits of a cgood commit history with meaningful commit messages!
 - I had issues with the deployment from Gitpod to Heroku and had to avail of tutor support, As I just could not see my error. I had an incorrect error in the Procfile, and this caused a migration fail, from the sqlite database to the postgres database in Heroku.
  I had also spelled DATABASES wrong in the settings.py file. Small errors, but somethimes the little ones are the hardest to see, and cause the most distress.

<img src="/media/heroku-fail.jpg" title="screenshot of heroku log error" height="100"> <img src="/media/migrate-database-error.jpg" title="screenshot of console log error" height="100">

***

#### Post Deployment Snag List:

*Major fails include: *

- When I got my database to migrate to Heroku, the products didnt show. When I went back into sqlite, they were not their either, so I had to manually imput the products again.
    Luckily, this being an MVP, I had only added the minimal amount of projects, so it was an easy fix.
- When tidying up the CSS I had deleted what I thought were unused styles, but it was the Navbar toggle Icon. I had to build a navbar toggle icon myself, in order to style it the way I wanted. 
     (bootstrap didnt allow me to create different outline and bars). I had to rebuild this toggle icon.
- After deployment, I wanted to retest all the interactive elements of the site, so tested the forms and user sign up pages. I realised I hadnt applied my custom CSS styling to the password reset pages and options.
     I felt this was important to the overall branding of TriFlake Studios.


*Minor bugs include:
*
 - Images on Shop page - these appeared smaller than I likes, I needed to resize them - fixed
 - I had not added the links to the Home Page footer social media icons - added 
 - Missing metatags in header - added
 - Spelling errors - fixed
 *Console log errors:*
 - Favicon missing - added
 - Chrome 'SameSite' cookies error - New Chrome cookie policy. 
 - Accessibility Errors - its easy to forget to add accessibility tags, alts and arias, so I went back over all the website, page by page, and added in as many accessibility features as I could find. This included alt tags to images, aria-hidden to font awesome icons, and titles to any icons that acted as buttons.

***

## Future Development
This was a huge project to undertake, a full stack django ecommerce platform, and I feel I could work on it for weeks, constantly tweaking, and changing sections. However, keeping in line with the Lean UX model I wanted to follow, it satisfies my idea of an MVP for a creative design website. With expected and unexpected features. 

*Existing features that need developing:*

 - Desktop view. I designed the website mobile view first, and I love the feel of the home page, when you see it on mobile. However the placement of sections feels slightly off on the desktop version. I would play around with that some more.
 - Portfolio Page: Develop a better portfolio showcase, be able to click on images to increase size and read about projects. Add logos of clients rather than text.
 - Shop: better range of products in the shop
 - User account: better selection of resources for the client. Is a huge area of potential for the studio, as is an unusual feature for a business of this sort.
 - A pop up modal to encourage people to create a user account
 - A pop up message when people have sent a message via the contact form
 - Development of a blog to include articles, tutorials and more
 - Instagram application with rolling images in footer, better social connection.

 ***

## Credits
All text by author: Orla Breslin. 
All graphics and images photos copyright from TriFlake Studio. 
All icons copyright free from https://fontawesome.com/.

***
## Acknowledgements

 
*Project Django Tutorials:*
 - Code Institute, YouTube Tutorials eg Traversy Media, Academind, Corey Schafer


*Github, Gitpod and Markup Tutorials:*
 - Code Institute, Various via Google eg Github Help, Git SCM
*Extras*
 - smashtheshell on YouTube for a great little tutorial on the new HTML5 download button [https://www.youtube.com/watch?v=7c4cNgD5KNA&t=314s]
 ```
    <a href="" download="" alt="">download</a>
 ```
