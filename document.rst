================================
**Resume Builder Documentation**
================================

Application Overview
====================
	Resume Builder is an application used to produce resume using different templates.

	Implementation details
		* Generation of different templates.
		* Collect the required data from the user.	
		* Provide various templates of resume to the user.
		* Generate the resume in the selected template format.
		* Provide the resume pdf to the user for download.

Features
========
	User data is saved even if the complete data has not been entered.

Technical Requirements
======================

--------------------
Hardware Requirement
--------------------
	Based on number of hits, system must be configured.

---------------------
Software Requirements
---------------------
	* CV-Boiler plate
	* Pandoc
	* mysql-client
	* celery
	* yaml
	* python 2.7
	* Django
	* LaTex 
	* Rabbitmq

CV-Boiler Plate and Pandoc
--------------------------
	* A boilerplate is used to ease the pain of building and maintaining a CV or resume using LaTeX.   
	* Pandoc is a universal document converter.
	* Cv-Boiler plate provides us with a make file.
	* CV-Boiler Plate helps in merging the LaTex and data in the form of yaml file to produce a pdf. It uses pandoc for this purpose in the rule set of the makefile. 
	* It is a open source software.
	* Link: https://github.com/mrzool/cv-boilerplate 

Celery and Rabbitmq
-------------------
	* Celery maintains a job queue. 
	* It has a broker, which is Rabbitmq in this application.
	* Brokers are used for signaling the worker about the task in the queue. When the worker receives signal it starts executing the task in the queue.
	* Link: http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html
		
LaTex and yaml
--------------
	* LaTex is easier for development of resume pdf.
	* CV-Boiler plate provides pandoc which uses yaml files for merging the Latex templates and yaml file.  
	* LaTex uses variables which are replaced with yaml file content when pandoc command is executed.
	* Yaml file has key value pairs.
	* link: http://www.yaml.org/start.html
		
mysql-client
------------
	* Django allows varied languages for accessing databases. We have choosen mysql for managing database.
	* MySQL is a database which uses structured query langugae(SQL). 
	* Database is named as Resumebulider. There are 21 tables in the database.

Class Diagram
=============

E-R Diagram 
===========

.. :image:: ../Resumebuilder.JPEG


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

----------------
Resume generator
----------------

	* Dictionary is received and validated and yaml file is created.
	* Using the latex template and yaml file, resume pdf is generated for the selected template of resume. The makefile provided by the 	CV- Boiler plate with pandoc is used.
	* Contents of makefile:
		* yml file - studentId.yml
		* latex template - selectedTemplate.tex 
		* resume pdf - studentIds.pdf
	* The make file contains a variable template which is replaced by the selected template while execution of the make file. 
	* Make file is executed.
	* Pdf is named with the students ID and are placed in appropriate path and stored in Database as well.
	* The database is updated once the server is invoked, while processing and after resume is generated as pending, processing and Done 		respecively.

Risk
====
	* Resume is content dependent, so the pagebreak is not adviced to use in the template. Hence there can be a case where heading and content are in different pages.

Constraint
==========
	* The images or pdf of certificates, profile picture are not retrieved if the user is a existing user.

Assumption
==========
	* LaTeX with the following extra packages: fontspec fontspec-extra geometry multicol xunicode xltxtra marginnote sectsty ulem hyperref 	polyglossia.
