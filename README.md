# python-pool-scraper
A project to extract and use swimming pool schedules from https://www.portlandoregon.gov/parks. Built in Python using Flask and BeautifulSoup.

Changes 3/23/16

Done: 
	* I began creating a Flask application, swim-times-app. It is loosly based on the Flask tutorial at http://flask.pocoo.org/docs/0.10/tutorial/
	* The swim-times-app currently contains SQLite schema for the Pools table, an admin login, and the means to add new pools while logged in as admin.

Next steps:
	* Add Edit and Delete functionality to the admin Pools page
	* Add Activities and Events tables, and the means to manually add/edit/delete entries while logged in as admin
	* Add some sort of simple display for anyone (admin or not) to see the schedule
	* Complete the scraper code in other sections of the project to feed data into these tables. 


Changes 3/2/16

Done:
	* I made a bunch of (paper) notes last night outlining the functions I need to write and the database structure I want.
	* Today I typed up an extended version of the web scraper script outline in script-outlines/scraper.py

Next steps:
	* Continue typing up and elaborating on the paper notes. 
	* Write unit tests for the outlined functions. 
	* Learn about database interactions in Flask, and create the database I need. 
	* Implement and test the outlined functions.
	* Create a bare-bones front end interface. I have all kinds of fun ideas about how I'd like it to look eventually, but I think it'll be more important to get *something* up and running. 
	
Project thoughts:
	* Here are some of my goals for this project, in terms of what I hope to learn and practice:
		- test-driven development in Python. I've taken a Treehouse tutorial on it but am having a hard time wrapping my head around real-world usage of the concept. 
		- get better at front-end development (especially CSS) without Bootstrap. It's a great tool but I've become overly dependent on it. 
	* I'll add more goals as I think of them. 


------
Created 1/31/16 

Done:	
	Have created a script to extract and process the data from a sample page. 

Next steps:
	Clean up the script and make it more extensible. 
	Write a scraper that can find the relevant data on a page and find the relevant pages within the portlandoregon.gov site.
	Create a web app to display the data. Probably Flask, but I'm not committed to anything yet. 
	