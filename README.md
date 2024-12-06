# Assignment 6.2 - Development
Assignment 6.2 for BTEC IT Lvl 3 course.
Copyright (C) 2024 gr8big

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


This repository is managed with Git - to see history you can view previous commits.
I did not need to publish this under GNU GPL v3 but I did anyway.

## Spec Overview
This website is developed for a fictional company, "Fizz and Funk". They specialise in novelty items.
The (also fictional) client has requested a number of pages, all with requirements.

## Strucutre Overview
As of writing, this only contains the front-end. It is structured so that it can easily be hosted as a simple Flask or Quart app in Python with the template directory as ./src/templates and static directory as ./src/static. Furthermore, the static path should be set to /src/* as that is how it is referenced.

I have included a demo.py file. This simply runs a web server that hosts as mentioned above but does not implement any other backend functions. This is so that I can test this, as the references (/src/*) would not work otherwise.

## Why the license?
Since this is for an assessment, it's worth releasing the source to the general public. However, there's no gaurantee some dingus will make a company called "Fizz & Funk" and use the exact site for commercial purposes. As such, I have selected GNU AGPL v3.