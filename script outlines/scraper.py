# PURPOSE: to scrape the various Portland Parks sites for public swimming pool schedules and update the project database.
# This will be a Flask project, so I'm outlining these functions with this in mind. 

# I'm starting out with comments describing the functions, plus the planned inputs and outputs for each function.

pages = # some list of page urls 

def init():
	# open DB connection 
	readPages(pages)
	# close database connection
	
# each page in pages will correspond to one pool. 	
def readPages(pages):
	for page in pages:
		processPage(page)

# this function will update the "pools" table		
def scrapePage(page):
	# find information about the swimming pool e.g. address, phone number, hours
	pool = Pool.objects.get(name= # whatever name we just found)
	# update the database entry on that pool
	
	tables = # use BeautifulSoup to get all the <table>s in the page
	for table in tables:
		parseTable(table, pool)

# something similar to parseTable and processCell already exist in table-scrape.py.
# I'm outlining here how they'll interact with the larger system. 			
def parseTable(table, pool):
	for row in rows:
		for cell in row:
			if # cell appears to contain the type of schedule info we're looking for 
				processCell(cell, position)
		


# The "activities" table contains listings of particular activity types. The "events" table lists when and where they are scheduled. 
def processCell(cell, position):
	day_of_week = # use the cell's position in the row to determine day of week 

	values_dict = {}
	# use regex to grab relevant strings like activity name and start and end times and put them in values_dict
	for key, value in values_dict:
		# create a new entry in the "events" table
		if key=='name':
			if Activity.objects.get(name=value) is None: # i.e. we don't have records of that activity yet
				activity = Activity()
				activity.save()
			
			
		if key in ['start_time', 'end_time']:
			values_dict[key] = # convert the value to a datetime object
			# will need to figure out whether the event is entirely in AM, entirely in PM, or starts in AM and ends in PM
		
		event = Event(
				pool=pool,
				day_of_week=day_of_week,
				activity=values_dict['activity'],
				start_time=values_dict['start_time'],
				end_time=values_dict['end_time'],
				)				
		event.save()