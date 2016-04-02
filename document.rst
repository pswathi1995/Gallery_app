================================
**Gallery Documentation**
================================

Application Overview
====================
	Gallery is an application used to store the details of all the students and present the selected student's profile to the recruiters.

	Overview:
		* The student registers into the application.
		* The administrator will approve the student profile.
		* After approval, the student will have access to view his batchmates profiles.
		* Administrator can generate a view page for recruiters to view the profiles of the selected students.

---------------------
Software Requirements
---------------------
	* postgresql 9.3.10
	* python 2.7
	* Django 1.9

PostgreSQL	
----------
	* Database is named as galleryapp. There are 8 tables in the database.
	
Modules
=======
	* Data collector
Database Schema
---------------

	* students

			+------------+--------------------------+
			|  Column    |           Type           |
			+============+==========================+
 			|id          | integer                  |
 			+------------+--------------------------+
 			|student_uid | character varying(20)    |
 			+------------+--------------------------+
			|created     | timestamp with time zone |
			+------------+--------------------------+
 			|updated     | timestamp with time zone |
 			+------------+--------------------------+
 			|first_name  | character varying(120)   |
 			+------------+--------------------------+
 			|last_name   | character varying(120)   |
 			+------------+--------------------------+
 			|email       | character varying(60)    |
 			+------------+--------------------------+
 			|mobile      | bigint                   |
 			+------------+--------------------------+

