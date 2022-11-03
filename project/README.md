# Calories Counter
#### Video Demo:  <URL https://youtu.be/QSzzPCQjHX8>
#### Author: Łukasz Marszałek
#### Description:

## What is it?

**Calories Counter** is a Web App created as **CS50 final project**. It uses Python with Flask library as back-end and for database sqlite3 with sqlalchemy. For front-end app uses html and css bootstrap. Front-end seems extremly boring for me and that's why App looks ugly, I just didn't pay attention. It also lacks half of features from original plan for example: meal creator (In "Add meal" > "Meal creator" there is a preview of what was supposed to be implemented - allow user create meal by chosing previously added products and amount used and it's the only place you can find usage of Ajax), statistics (allow user to define what is his calorie/macro intake and then show whats the % days user followed, and what are AVG daily intakes). I didn't finish the project as I planned, because I struggled a lot with things that turned out to be extremly simple and I want to move forward to more exciting stuff, no more Web Dev at least for now.

## Main Features
Here are just a few of the things that Calories Counter does well:

  - Register users, keep their data safely in db, also protects functions from getting accesd by non logged users
  - Allows user to add meal and specify it's calories and macro
  - Allows user to chose meal from list and consume it
  - Counts calories and macros consumed by user each day
  - Allows user to add products (was meant for not implemented functions, I don't want to get rid off it as one day I might want to finish it)

## How to Use
App is not and will not be deployed online. To use it run **main.py** file.

## Functionality
  - "main.py" runs program
  - "__init__.py" contains all App setup, so it registers blueprints, define user via login_manager and create database
  - "auth.py" contains all functions used to login, logout and sign up user
  - "schema.py" contains structures of database. There are 5 tables: User for user information, Meal stores information about calories and macros of each meal, Product stores information about products added, Food combines information which user ate what and when, lastly there is Product_meal which is not used atm, but i store it for possible future additions to project, It was supposed to store informations which products are in each meal
  - "stats.py" has just one function to calculate daily Calories intake and Macros, file was meant to store all statistical function which are not implemented
  - "views.py" contains all functions used to gather information about Meals, Products and what meal was eaten when
  - In "templates" folder you can find all the templates and the layout is stored in layout.html
  - "instance" folder was automatically created by app and contains database


## Disclaimer & Contact
You are welcome to use my code and do whatever you want with it as long as it's legal.
**I'm also very happy to hear tips and constructive criticism.**
If you wish to contact me, best way is via e-mail lukasz.marszalek320@gmail.com