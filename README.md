This blog is the final project of the CoderHouse Python course.

######### Explanatory video #########

https://vimeo.com/user146765799

######### Technologies used #########

HTML5, CSS (Front End)
Python with Django (Back-End)

Instructions:

1.  Clone the project (or download the zip file)

        - *git clone https://github.com/EmanuelViltre/FinalProject.git

2.  Install project dependencies:

        - *pip install django*
        - *pip install Pillow*
        - *pip install django-ckeditor*

3.  Enter the project folder

        - *cd WebBlog*

4.  Run the application

        - *python manage.py runserver*

5.  enter the website

        - (http://127.0.0.1:8000/)

######### About Blog #########

Anyone who enters the blog can see the initial page posts, you can also see the image, the author, when the post was created and see the full detail but, if you want to edit, delete and create a Post it is necessary to be logged in.

######### About #########

It has a section where it talks about the creator of the Blog and a Linkedin action button

######### Posts #########

Each post consists of a title, subtitle, slug, image, content, author and publication date, when you click on the Post it takes you to the full Post and it also has a Recent Post section where it takes you to a different Post.

######### Profile #########

Each user can edit their profile information, add or edit their Avatar and send a new message or check the inbox.

Each user consists of a username, password and an email as mandatory data.

The user's profile also lists the date of their last login and the date they joined (registered) the blog.

######### Messenger service #########

Users have a messaging system as a direct message.
Messages can only be seen by the intended users and the user who sent the message.

######### Database #########

The data is saved in a SQLite3 engine database by default
