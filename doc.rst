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

	* student_details

		+-----------------+--------------------------+
		|     Column      |           Type           |
		+=================+==========================+
		|id               | integer                  |
		+-----------------+--------------------------+
		|created          | timestamp with time zone |
		+-----------------+--------------------------+
		|updated          | timestamp with time zone |
		+-----------------+--------------------------+
		|description      | character varying(3000)  |
		+-----------------+--------------------------+
		|audio_path       | character varying(100)   |
		+-----------------+--------------------------+
		|video_path       | character varying(100)   |
		+-----------------+--------------------------+
		|resume_path      | character varying(100)   |
		+-----------------+--------------------------+
		|profile_pic_path | character varying(100)   |
		+-----------------+--------------------------+
		|ppt_path         | character varying(100)   |
		+-----------------+--------------------------+
		|student_id_id    | integer                  |
		+-----------------+--------------------------+
		
	* students_pending_approvals
	
		+-----------------------+--------------------------+
		|        Column         |           Type           |
		+=======================+==========================+
		| id                    | integer                  |
		+-----------------------+--------------------------+
		| student_uid           | character varying(20)    |
		+-----------------------+--------------------------+
		| created               | timestamp with time zone |
		+-----------------------+--------------------------+
		| updated               | timestamp with time zone |
		+-----------------------+--------------------------+
		| first_name            | character varying(120)   |
		+-----------------------+--------------------------+
		| last_name             | character varying(120)   |
		+-----------------------+--------------------------+
		| email                 | character varying(60)    |
		+-----------------------+--------------------------+
		| mobile                | bigint                   |
		+-----------------------+--------------------------+
		| updated_fields        | character varying(200)   |
		+-----------------------+--------------------------+
		| comment_for_rejection | character varying(30)    |
		+-----------------------+--------------------------+
		
	* studentsdetails_pending_approval
	
		+------------------+--------------------------+
		|      Column      |           Type           |
		+==================+==========================+
		| id               | integer                  |
		+------------------+--------------------------+
		| created          | timestamp with time zone |
		+------------------+--------------------------+
		| updated          | timestamp with time zone |
		+------------------+--------------------------+
		| description      | character varying(3000)  |
		+------------------+--------------------------+
		| audio_path       | character varying(100)   |
		+------------------+--------------------------+
		| video_path       | character varying(100)   |
		+------------------+--------------------------+
		| resume_path      | character varying(100)   |
		+------------------+--------------------------+
		| profile_pic_path | character varying(100)   |
		+------------------+--------------------------+
		| ppt_path         | character varying(100)   |
		+------------------+--------------------------+
		| student_id_id    | integer                  |
		+------------------+--------------------------+
	
	* batches

		+------------+--------------------------+
		|   Column   |           Type           |
		+============+==========================+
		| id         | integer                  |
		+------------+--------------------------+
		| created    | timestamp with time zone |
		+------------+--------------------------+
		| updated    | timestamp with time zone |
		+------------+--------------------------+
		| batch_name | character varying(30)    |
		+------------+--------------------------+
		
	* student_batch

		+---------------+--------------------------+
		|    Column     |           Type           |
		+===============+==========================+
		| id            | integer                  |
		+---------------+--------------------------+
		| created       | timestamp with time zone |
		+---------------+--------------------------+
		| updated       | timestamp with time zone |
		+---------------+--------------------------+
		| batch_id_id   | integer                  |
		+---------------+--------------------------+
		| student_id_id | integer                  |
		+---------------+--------------------------+
		
	* student_comments
	
		+-----------------------+--------------------------+
		|        Column         |           Type           |
		+=======================+==========================+
		| id                    | integer                  |
		+-----------------------+--------------------------+
		| created               | timestamp with time zone |
		+-----------------------+--------------------------+
		| updated               | timestamp with time zone |
		+-----------------------+--------------------------+
		| comment_text          | character varying(100)   |
		+-----------------------+--------------------------+
		| student_comment_id_id | integer                  |
		+-----------------------+--------------------------+
		| student_id_id         | integer                  |
		+-----------------------+--------------------------+
		
	* student_likes

		+--------------------+--------------------------+
		|       Column       |           Type           |
		+====================+==========================+
		| id                 | integer                  |
		+--------------------+--------------------------+
		| created            | timestamp with time zone |
		+--------------------+--------------------------+
		| updated            | timestamp with time zone |
		+--------------------+--------------------------+
		| student_id_id      | integer                  |
		+--------------------+--------------------------+
		| student_like_id_id | integer                  |
		+--------------------+--------------------------+
	
Modules
=======
	* Data collector

Application Flow
----------------
	Student:
		* Student will be able to login and for the first time, he will be able to see the registration page.
		* Student will fill the registration form with all the details and uploads the required files.
		* Data is validated and a request is sent to the administartor for approval.
		* The student will not be able to view batch gallery until his profile has been approved.
		* If his profile is rejected by the administartor, a message will be displayed on the screen showing why it has been rejected, else he will be navigated to the batch gallery page.
		* If he is an existing user the stored data is retrieved and displayed where the student will be able to see his batchmates details.
		* The batch gallery page displays the profiles of all the batchmates in the form of a portfolio.
		* On clicking the portfolio, a modal is displayed which consists of all the details and an option to view resume also.
		* The student has an option to update his profile.
		* When the student clicks on update, the previous data will be shown on the screen with can be updated.
		* On click of submit button a request will be sent to the admin for approval and the changes are reflected only when the administartor approves them.

	Administrator:
		* Administrator will login and all the pictures irrespective of the batches will be displayed on the screen, and on clicking the portfolio, that particular student's profile is displayed.
		* Pending approvals consisting of new registrations and updates is provided as a dropdown along with the count.
		* On clicking the new registrations the list of new registrations is displayed. Administartor can view their profiles and can either approve or reject the request by the students.
		* Similarly on clicking updates, the list of updates are diaplayed. Administrator can view their profiles and can either approve or reject.
		* Administrator can create batches and assign the student to the batch at the time of approval.

Pending Functionalities
-----------------------
	* Likes for the profile, for students
	* Assign students to batch
	* Student and administrator authentication
	* Paginator
	* Filter functionality for recruiters
	* Search bar: by name only
	* Buttons to approve selected, approve all
	* Create view page for recruiters
	* Student approval notification through email
	* Discussion Forum
	* Recent Activity Panel : New Profiles, Updates, Posts, Comments
	* Comments on students profiles	
