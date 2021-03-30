# Job-Portal

A website that allows user to search and post job. Before the user can search or post a job he/she has to authenticate himself/herself.
User authentication for three different users - Admin, User & Recruiter
User can search for job according to their specific domin of skills.
Recruiter can select the appropriate candidate according to their requirements.

# 
![Screenshot from 2021-03-30 22-34-50](https://user-images.githubusercontent.com/65526550/113028926-78602700-91a9-11eb-9068-261b2f06c118.png)

#
![Screenshot from 2021-03-30 22-35-14](https://user-images.githubusercontent.com/65526550/113028932-79915400-91a9-11eb-9fbe-e1472fbaef2d.png)
#

![Screenshot from 2021-03-30 22-35-27](https://user-images.githubusercontent.com/65526550/113028938-7ac28100-91a9-11eb-9ccc-a4f8afea53bf.png)


### Main Features
* User Authentication
* User Registration
* Password Change
* Searching Facilities in tables
* Profile Page
* Job Posting
* Job Searching


# How to start with the project 

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd into the repository
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

