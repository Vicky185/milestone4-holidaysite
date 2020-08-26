# MyHoliday travels

## A holiday purchasing website for keen travellers!

#### A website which uses a full stack of frameworks, primarily using Django.

In this website, users will be able to view, purchase, review holidays, register and login to their own profile and keep up to date with their purchasing and travel plans. 

By registering, our users will be able to gain access to multiple travel options, purchase a holiday plan and also review  orders in your very own profile page. 

The purpose of this website really is to entice people to travel, to feel inspired by a holiday and want a quick and easy way to purchase one. 

[Visit the 'MyHoliday travels' website here](https://myholiday-travels.herokuapp.com/)

The website is fully responsive. It uses a combination of Django, Python, Javascript, HTML & CSS. It also uses a PostgresSQL database in which is stored the different holiday package options. 

The 'Packages' page, lists and shows all the available package holidays in the order that they are uploaded but this can be altered via the sorting dropdown (sorting can be amended by price, alphabetically, rating and category ie. type of holiday).

Each holiday is held in a Bootstrap 4 styled 'card', which holds a snippet of details for what each single holiday involves. Each single package page can be found by clicking on the name or the image of the card. The user can also look up similar holidays by clicking on the category tag, i.e. type of holiday like beach, and will be taken to a new page with all of the holidays that are in the same category. 

The superuser/administrator can add a new options, edit and delete any of the current and available options through their own additional menu option 'Package Management' and in each of the single pages only admins/superusers will be able to see the option of 'Edit' and 'Delete' buttons. But as a regular and registered user, you cannot amend, delete or add any of the packages. 

An additional feature for existing and newly registered users is adding comments/reviews to holidays. At the bottom of each single package page you can see a comments section where you can leave a review. If you are not registered or logged in you can only view previous comments made by other users and you cannot add one. In future it would be good for users to also have the option to provide ratings as well. Administrators and superusers are the only ones who have access to edit or delete these comments as well.

## The User Experience (UX)

#### Project Purpose

To provide an e-commerce site for holidays which lets any one want to travel. This website is for keen travellers, seeking comfort and convenience by having things lined up for them with quick and easy purchase. They will be able to easily sign up or do a one-off purchase of travel packages. They will also be able to store their information securely and submit credit details securely through the site, receiving a confirmation email as well to ensure success, security and authenticity of their purchase. 

The following requirements were set at the beginning of the project;
* primary target audience is travellers, including solo, family and groups of all ages who want to have a set travel plan provided to them
* the look of the project needs to feel inspiring of travel
* the user needs to have an option to register and keep track of their purchases
* the user should be able to revisit and review their holiday Experience
* the site needs to be easy to move through, there needs to be a really smooth search functionality and filtering function for sorting packages via category and this needs to be easily accessible in the menu and on the page itself (in addition to the search bar)
* the admin/superuser needs to be able to delete, add and edit the packages
* the user should be able to login easily and submit credit card details securely.

#### User Stories
As a general user:
* I want the page to be inspiring and I want to feel motivated to travel
* I want it to be easy to use and easy to search for things
* I want to feel like my credit and personal details will be kept safe

As an existing and registered user:
* I want to find new packages easily
* I want to be able to purchase things quickly and perhaps multiple options at any one time
* I want to be able to have plenty of clear options for whatever my mood
* I want to be able to revisit pages and leave my thoughts/reviews on my experiences to help with others' choices of package
* I want a place where I can quickly get my personal details stored and also where I can see previous orders

As a potential user of the site:
* I want immediately to feel like this is a travel site
* I want to be able to see the different options quickly and want to move through pages easily and smoothly
* I want to be inspired for my holiday choice 

As a team member/administrator:
* I want to be able to see clearly the different users on the site and i want to be able to filter through them quickly and easily
* I want to be able to remove, edit and also add new packages quickly when they become available and I want them to be clearly positioned on the site for all to see
* I want my customers to have a seamless process, I want them to feel safe and that their money is being wellspent and that their card details are secure
* I want the users to be inspired by the packages on offer and I want them to feel excited about travelling when they look at this site - it needs to be inviting.

## Features

For this site, a range of features was used:
* HTML, CSS, Javascript, Django, Python, Stripe, Heroku, GitPod, GitHub, Bootstrap, Amazon AWS,
* A number of additional features were used, these are all included in our [Requirements.txt file](https://github.com/Vicky185/milestone4-holidaysite/blob/master/myholiday/requirements.txt)
* A mobile first approach
* The site was tested on Browsers, e.g. Google Chrome, Microsoft Edge, Safari and Android (Samsung Web browser)
* Responsive navigation - scroll to top button, when packages are added to the cart then a toast appears in response to your process to purchase
* Pagination - when new packages are addded, new page numbers are added to the all packages page (packages app)
* Comments form in every single travel package page, which greets the logged in user (if you are not logged in or registered you can't post a comment/review)
* A video background for the homepage which is on autoplay, is muted and runs smoothly
* Social media links are included in the footer of every page
* Search bar functionality which allows a keyword search of the site
* Smooth notification of errors are also included via Toasts and also in forms, e.g. crispy forms

Additional features for the site (in any future development) would include: 
* Users will be able to review all of their previous comments on their profile page (in similar way to their order history)
* Users can store and save their credit card details
* Added login functionality will also include signing in through social accounts, like GMail/Google accounts
* More package options, with coupon and last chance/latest available options

## Structure

#### Skeleton

###### [Wireframes](https://github.com/Vicky185/milestone4-holidaysite/tree/master/myholiday/Wireframes):
* [Home page](https://github.com/Vicky185/milestone4-holidaysite/blob/master/myholiday/Wireframes/home-page.jpeg)
* [All Packages page](https://github.com/Vicky185/milestone4-holidaysite/blob/master/myholiday/Wireframes/all-packages-page.jpeg)
* [Single Package page](https://github.com/Vicky185/milestone4-holidaysite/blob/master/myholiday/Wireframes/single-package-page.jpeg)
* [Profile page](https://github.com/Vicky185/milestone4-holidaysite/blob/master/myholiday/Wireframes/profile-page.jpeg)
* [Shopping Cart page](https://github.com/Vicky185/milestone4-holidaysite/blob/master/myholiday/Wireframes/shoppingcart-page.jpeg)
* [Checkout page](https://github.com/Vicky185/milestone4-holidaysite/blob/master/myholiday/Wireframes/checkout-page.jpeg)
* [Allauth/Sign up/out/in pages](https://github.com/Vicky185/milestone4-holidaysite/blob/master/myholiday/Wireframes/login-allauthmessagepages.jpeg)
* [Add or edit page](https://github.com/Vicky185/milestone4-holidaysite/blob/master/myholiday/Wireframes/add-edit-page.jpeg)

#### Surface/Design

###### Fonts
* [Alata](https://fonts.google.com/specimen/Alata) - a font for general text, doesn't stand out as much but provides a nice humbling contrast to the header fonts
* [Pacifico](https://fonts.google.com/specimen/Pacifico) - an inviting cursive font for headings and logo

###### Colors
Color hexcodes were taken from the Home Page video which was from pexels.com free videos here: https://pixabay.com/videos/beach-ocean-water-wave-palm-trees-42894/ [They are stored here](https://github.com/Vicky185/milestone4-holidaysite/blob/master/holiday%20colours.png).

#### Technologies

Below is listed all of the technologies used to create this site:
* [Django](https://www.djangoproject.com/)
* Python 3
* CSS and [Bootstrap 4](https://getbootstrap.com/)
* Javascript and [JQuery](https://jquery.com/)
* HTML
* Json - for fixtures of intial data files
* Django Crispy Forms - for all of the input Forms
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* PostgresSQL
* CSRF tokens to protect data in Forms
* [Stripe](https://stripe.com/
* [Google Fonts](https://fonts.google.com/) - API and keys, for purchasing, webhook handlers and caching data
* Gitpod - as the IDE
* GitHub as the remote backup used on this project and for other project users to view the code
* [Heroku](https://www.heroku.com/) - for deployment method
* AWS S3 buckets for static and media file storage
* [Temp Email](https://temp-mail.org/)
* W3C HTML & CSS Validator

## Testing

#### UX
* The user is able to see up to 8 package options per page on the full packages page (packages app)
* The user is able to navigate the page with a navbar which is clearly atop every page, showing access to proifle, shoppingcart and search bar (and home page on desktop or med-screen sizes)
* The user is able to search via keywords in the search bar, then upon keyword search is taken to search results page
* The user can look at every single package in detail (one_package_detail.html template in the packages app), capturing options of airport, length, rating and viewing other past user comments. 
* If the user is logged in or registered they are greeted by the page and can log a new review or comment.
* If the user is not registered or signed in they can see all comments but not add any until they have logged in.
* Users can easily update the contents of their shopping cart, adding multiple and removing multiple.
* Navbar menu becomes a dropdown on small screens
* The user can scroll down and scroll back up quickly and easily with a button at the bottom right
* The user can make a quick purchase of a package and then in their profile review their order and order history in their account page (profile app)
* The user's personal details can also be stored in their profile page
* The user is notified when they log in/log out and told when they don't have access to elements of the site 
* The user receives a confirmation email upon purchase.

*Examples*:
* When the user clicks on the image of a package, they are taken to a single page view of that package where they get a detailed description and can see previous users' experiences in the comments at the bottom of the page. The user can amend the quantity and add this to their shopping cart. They can then move through to a secure checkout and purchase it with confirmation email and also a page telling you that you've completed the payment. 

[For a description of the different screen sizes, visit here.](https://github.com/Vicky185/milestone4-holidaysite/blob/master/SCREENS.md)

#### Manual Testing
My tests to ensure that it is all working:
* Deployment to Heroku and loading the home page, all worked, video present and playing on autoplay
* Click on the 'Take a look' button on the centre of the page and you're taken to the full packages site
* View single page of package - click on image or name of item and you'll go to single page view with description of the holiday and option to add to cart
* Click number of packages and add to cart - view a toast which takes you to the checkout where you can then purchase securely the package with card and user details
* Search bar - click the search, taken to all packages, search 'beach' and everything in the site that has a keyword 'beach' will come up
* Menu - two options where you can find pages sorted by price, name, type (which is an additional searching option that you can also do on the full packages web page on the top right) and then alternative is catgory search (e.g. Types of Holiday which is also a navbar menu option). In the latter you have the option to search by type of holiday according to category codes of holiday (i.e. beach/city/culture etc, these are found in the packages models.py)
* Profile Page - You can look at your order history and you can update your personal information on the form on the left of the page 
* As a superuser - you can go to package management and add a new package, if no image then 'No Image' image will appear with this package, errors occur when forms are filled incorrectly, and you are notified when new package has been added. 
* As a superuser you can delete any package clicking delete on full packages or single package pages
* As a superuser, you can edit any of the current packages on the site clicking edit and this will be updated to the page
* When the user adds a package to the cart, the price on the top hand corner will update. In the cart if you amend (via update button) the price will amend accordingly, if you click remove the cart will clear of the package you removed. 
* As a logged in user you can add comments, I used the @login_required on several apps to ensure this functionality and also a number of {% if user.is_authenticated %} statements as well. 
* Upon purchase, the user will receive an email confirmation providing a summary and link to order summary 
* Stripe testing involved using their automated card details:
    * Card number - 4242424242424242, CVC 
    * Any 3 digit number
    * Expiry date - Any date in the future

As the site is built with responsive design, I have checked it's functionality on IPhone, MS SurfacePro 6, Samsung Andriod, Desktop Laptop and mini iPad. I have also tested this on various browser types such as Chrome, Firefox, Safari and Edge. 

## Deployment
This project was built and coded using [GitPod](https://gitpod.io/workspaces/) and then uploaded via Git onto [GitHub](https://github.com/Vicky185/milestone4-holidaysite). 

This project used Amazon AWS to store all static and media files and this was connected to Gitpod via Boto3 and S3 and using a Bucket on Amazon AWS. 
It was deployed to Heroku. In Heroku I used a number of config variables for secret keys, the stripe handling, database url, the email host and the aws keys.   

The details of the deployment and the files involved are in our requirements.txt, Procfile, settings.py and wsgi.py files of the myholiday app. This project  used a Procfile to help Heroku recognise the commands which were being run by the app's dynos. It was also used to help Heroku understand how to run different parts of the apps and module migrations (myholiday, checkout, home, packages, profiles and shoppingcart).

*On first deployment, there were a couple of issues regarding the directory format. This meant that towards the end there were a number of repetitive commits to ensure that the deployment was picking up the changes and would enable being deployed to the final site. My mentor really helped me realise this (see below recognition and acknowledgements section).*

To deploy I used the following: 
* git add .
* git commit -m "*commit message*"
* git push 

At this stage my heroku was not automatically deploying and so I had to run this manually. However, Enable Automatic Deploys on Heroku was later added for ease. 

If you want to access the project code and view the repository, please log into GitHub and go to select:
_https://github.com/Vicky185/milestone4-holidaysite_ responsitory. 

From here you can access the apps, the modules, the HTML templates, the static and media files (including CSS and Javascript) as well as the django and python files. *To add this to your own repository, please go to the 'Code' tab and click the green button 'Clone/Download'.*

If you want to access the project through Heroku, please search: https://dashboard.heroku.com/apps/myholiday-travels.

## Credits and Acknowledgements 
1. For Text and contents
* I referred a lot to [British Airways](https://www.britishairways.com/) and [Kuoni](https://www.kuoni.co.uk/) for inspiration and examples of travel plan descriptions

2. Media and static
* For Home Page video - https://pixabay.com/videos/search/ 
* For travel images - https://www.pexels.com/

3. Acknowledgements
As always, thanks to my mentor Spencer Barriball who has genuinely been through as much as I have with all of the trials and tribulations this project has brought us! He's really helped me with links for code and handling the migrations, he helped me get started and was always really positive. He particularly helped me solve the issues with deployment. 
Also, thanks so much for Code Institute's Tutor support who really helped me through a lot of uncertainty and always provided clear and positive responses. 

Inspiration for the style of the site:
* [Kuoni](https://www.kuoni.co.uk/)
* [The Blonde Abroad](https://theblondeabroad.com/)

Help with coding and styling:
* [Pinterest](https://www.pinterest.co.uk/)
* [Stack Overflow](https://stackoverflow.com/)
* [Slack](www.slack.com)
* [W3Schools](https://www.w3schools.com/)









