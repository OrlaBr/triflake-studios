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
4. [Technologies](#technologies_used)
4. [Building and Deployment](#building-and-deployment)


## Project Outline
The website has a dual purpose. It was created for a new local community group to use, but it also deploys all my course learning to date with the Code Institute. 
The elements I used in creating this website are all practical techniques I have been learning, working through the User Centric Front End Development modules of 
the Full Stack Developer Bootcamp.

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



## Technologies Used

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


#### Heroku

Before deploying to Heroku, I add a few more steps to do. I needed to transfer all the files in my database  from django's sqlite to Heroku PostRes.
You do this by setting the keys and values in Config Vars, in the Heroku Platform, and also your settings.py file

```  
Heroku - TrifkaleStudioAdd - Settings - Reveal Config Vars
```
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

