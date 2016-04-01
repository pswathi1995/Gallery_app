================================
**Gallery Documentation**
================================

Application Overview
====================
	Gallery is an application used to store the details of all the students and present the selected students profiles to the recruiter.

	Overview:
		* The student registers into the application.
		* The admin will either approve or reject the student profile.
		* After approval, the student will have access to view his batchmates profiles.
		* Admin can generate a view page for the recruiter to view the profiles of the selected students.


Technical Requirements
======================

---------------------
Software Requirements
---------------------
	* postgresql
	* python 2.7
	* Django 1.9

PostgreSQL	
------------
	* Django allows varied languages for accessing databases. We have choosen postgresql for managing database.
	* Database is named as galleryapp. There are 8 tables in the database.


Modules
=======
	* Data collector

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
		* If his profile is rejected by the admin, a message will be displayed on the screen showing why it has been rejected, else he will be navigated to the batch gallery page.
		* If he is an existing user the stored data is retrieved and displayed where the student will be able to see his batchmates details.
		* The batch gallery page displays the profiles of all the batchmates in the form of a portfolio.
		* On clicking the portfolio, a modal is displayed which consists of all the details and an option to view resume also.
		* The student has an option to update his profile.
		* When the student clicks on update, the previous data will be shown on the screen with can be updated.
		* On click of submit button a request will be sent to the admin for approval and the changes are reflected only when the admin  approves them

	Admin:
		* Admin will login and all the pictures irrespective of the batches will be displayed on the screen, and on clicking the portfolio, that particular student's profile is displayed.
		* Pending approvals consisting of new registrations and updates is provided as a dropdown along with the count.
		* On clicking the new registrations the list of new registrations is displayed. Admin can view their profiles and can either approve or reject the request by the students.
		* Similarly on clicking updates, the list of updates are diaplayed. Admin can view their profiles and can either approve or reject.
		* Admin can create batches and assign the student to the batch at the time of approval.
