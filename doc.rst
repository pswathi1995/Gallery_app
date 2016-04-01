================================
**Gallery Documentation**
================================

Application Overview
====================
	Gallery is an application used to store the details of all the students and present the selected students profiles to the recruter.

	Overview:
		* The student will be able to register into the application.
		* The admin will approve or reject the student profile.
		* After approval, the student will be able to view his batchmates profiles.
		* Admin can generate a view for the recruter to view the profiles of the selected students.


Technical Requirements
======================

--------------------
Hardware Requirement
--------------------
	Based on number of hits, system must be configured.

---------------------
Software Requirements
---------------------
	* postgresql
	* python 2.7
	* Django 1.9
	
mysql-client
------------
	* Django allows varied languages for accessing databases. We have choosen postgresql for managing database.
	* Database is named as galleryapp. There are 21 tables in the database.


Modules
=======
	* Data collector
	* Resume generator
--------------
Data collector
--------------

Models
------
	* A model in Django is a special kind of object - it is saved in the database.
	* We will be using a Mysql database to store our data.
	* SQLite is the default Django database adapter.

Template
--------
	* All the .html pages are represented as templates in Django.
	* Django template tags allow us to transfer Python-like things into HTML, so you can build dynamic websites faster and easier.

URL
---
	* URL's have prominent role in django.
	* URL's are used to map functions in views.
	* They use regular expression to create a pattern that will match the url.

Views
-----
	* A view is a place where we put the "logic" of our application.
	* It will request information from the model you created before and pass it to a template.
	* They are python functions.

Implementation
--------------
	Student:
		* Student will be able to login and for the first time, he will be able to see the registration page.
		* Student will fill the registration form with all the details and uploads the required files.
		* Data is validated and a request is sent to the admin for approval.
		* The student will not be able to view batch gallery until his profile has been approved.
		* If his profile is rejected by the admin, a message will be displayed on the screen showing why it has been rejected.
		* If it is an existing user the stored data is retrieved and displayed where the student will be able to see his batchmates details.
		* Displays the pictures of all the batchmates which on click on the picture will display their profile.
		* The profile contains all the information provided by the student and a button to view resume.
		* On click of that button a PDF file containing the resume will be displayed which has a option to save.
		* The student has an option to update his profile.
		* When the student clicks on update, the previous data will be shown on the screen with can be edited.
		* On click of submit button a request will be sent to the admin for approval and the changes are reflected only when the admin  approves them

	Admin:
		* Admin will be able to login and all the pictures irrespective of the batches will be visible on the screen, and on click on the picture, that particular student's profile is visible.
		* The  
