##              BOUN-SWE573

##      Software-Development-Practice

##        2021719105-Ali Eren Ohtaroglu


# About

Aim of the project is to create a social media app. Social media users are experiencing problems while remembering the information.
An easy mind app will help the user save the urls, tag them, and add actions per each link. The added URLs will be grouped under different headers.
Each header will be open by other users visit and contribution. 

Due to time constraints, some of the features is not working for now. My aim is to make it better before the start of 2nd semester.

Developed by using Python - Django environment. As database project started with mySQL but due to problems in deploying to AWS, it was migrated to postgreSQL Dockerized. And finally deployed by AWS.

While creating the project different tutorials, web pages and documents helped. Nearly all of them can be found under wiki files. 

Passwords are disabled by .env file. This was not posted here.One can see the file details as below. 

DATABASE_NAME=xxx
DATABASE_USER=xxx
DATABASE_PASSWORD=xxx
SECRET_KEY=xxx
DEBUG=TRUE

My personal aim in this project is to understand the good practices in software development. 

Those were using version control practices, requirements understanding and deploying, mock-up making and presenting, following up a time schedule, and recording the time spent.

On the other hand, technical knowledge about the above mentioned platforms are gained. 

To make the project from scratch, I advise to inspect the excel file uploaded in wiki section. All the pre-requirements gathered from user, app flows, and various details are there.

# Demo

One can reach the AWS deployed version from:

http://ec2-54-208-213-7.compute-1.amazonaws.com

When using the docker container:

http://localhost:8000/

# Installation

Python, Django, Docker, and AWS should be up and running in your enviroment. 

After copying latest version from Github, start the Docker infrastructure. Creating a new superuser for your Django enviroment is advised.

# Outside help

I want to personally thank to Ali Kenan Yagmur for all his help.

Similar repositories can be found in Github by searching SWE573 for much better examples. 

