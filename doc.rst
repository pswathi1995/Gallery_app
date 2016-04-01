================================
**Gallery Documentation**
================================

Application Overview
====================
	Gallery is an application used to store the details of all the students and present the selected students profiles to the recruter.

	Implementation details
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

Overview
--------
	* Details are taken from the end user.
	* Data is validated and saved in Database.
	* If it is an existing user the stored data is retrieved and displayed.
	* Displays the various templates available for user to select one of their choice.
	* Dictionary is produced using the ResumeBuilder.conf file and is sent to generatePdf.py by starting the worker.
