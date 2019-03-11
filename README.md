
URLShortcode
============

URLShortcode is a Django app.

Note that URLShortcode is not yet feature complete.

The latest source code is available at http://github
.com/sonlinux/django-urlshortcode.

* **Developers:** See our `project setup guide`_ and `developer guide`_

Quick Project Setup
-------------------

Refer to `project setup guide`_ for in depth information.

Make sure docker is installed, and project
already opened using PyCharm. Then run these command:


Quick Installation Guide
------------------------
For deployment I use `docker`_ so you need to have docker
running on the host. URLShortcode is a django app so it will help if you have
some knowledge of running a django site.

    git clone git://github.com/sonlinux/django-urlshortcode.git
    
    cd /project/root/dir/deployment
    
    make build
    
    make permissions
    
    make web
    
    make run
    
    # Wait a few seconds for the DB to start before to do the next command
    
    make migrate
    
    make collectstatic

    # You can access the project in two ways
    
    1. Via web server nginx by going to address in the web browser  
    
    >> http://0.0.0.0:60209/
    
    2. By setting up the local development server with Pycharm and this will
     expose the address. See instructions on setting up with pycharm locally
      in the README-dev.md file
     
      >> http://0.0.0.0:60206/
    

    
So as to create your admin account:
```
make superuser
```

Using the app service
---------------------

The application service will be available on the base url.

* Pass (post) in the json valid URL data and you will be redirected with the
 shortened URL.
 
* copy the url returned and load it in the browser tab
* this will take you to the initial/original URL that was shortened

NOTE: the service needed to allow clicking on the returned URL directly to 
load the reference but that is what I have not implemented yet and it is 
something I would love to add soon.


Thank you
_________

Authored By.
* Alison Mukoma: mukomalison@gmail.com
