# Assignment 6.2 - Development
Assignment 6.2 for BTEC IT Lvl 3 course.
This repository is managed with Git - to see history you can view previous commits.

I did not need to publish this under GNU GPL v3 but I did anyway.

## Spec Overview
This website is developed for a fictional company, "Fizz and Funk". They specialise in novelty items.
The (also fictional) client has requested a number of pages, all with requirements.

## Strucutre Overview
As of writing, this only contains the front-end. It is structured so that it can easily be hosted as a simple Flask or Quart app in Python with the template directory as ./src/templates and static directory as ./src/static. Furthermore, the static path should be set to /src/* as that is how it is referenced.

I have included a demo.py file. This simply runs a web server that hosts as mentioned above but does not implement any other backend functions. This is so that I can test this, as the references (/src/*) would not work otherwise.