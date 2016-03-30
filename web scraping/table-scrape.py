# This is the initial proof of concept for the core functions of the PDX Pool Schedule Scraper. 
# Fairly disorganized, as I'm just playing with examples here. 

# 31 Jan 2015 - Created by Emily Cain

# thanks to the authors of "Automate the Boring Stuff with Python", which was my starting point for this project.
# https://automatetheboringstuff.com/chapter11/

import requests, bs4, re

class TableScraper:
	def __init__(self, table):
		"""Keyword Arguments:
		table - in the form beautiful_soup.select(selector)[optional index]
		"""
		self.table = table
		
	def __str__(self):
		if self.table.get("id"):
			return "table id " + str(self.table.get("id"))
		else:
			return None
			
	

# eventually I will take some data from this page...

# url = "https://www.portlandoregon.gov/parks/60939"
# res = requests.get(url)
# pool_soup = bs4.BeautifulSoup(res.text)

# ... but for now I will just use a sample file drawn from that page. 

example_file = open('sample-table.html')
example_soup = bs4.BeautifulSoup(example_file)

########################
# list of lists method #
########################

list_of_lists = []

for row in example_soup.select('table')[0].select('tr'):
	i = 0
	for cell in row.select('td'):
			# if list hasn't been populated with lists, do so 
			try: 
				list_of_lists[i]
			except IndexError:	
				list_of_lists.append([])
				
			# put cell data into the list. encode properly to avoid errrors	
			try:
				list_of_lists[i].append(str(cell.text.encode('UTF-8')))
			except:
				list_of_lists[i].append('err')
			i += 1
			
print 'here is the list of lists'

for item in list_of_lists:
	print '----------------------------'
	print item
	
#####################
# add to dictionary #
#####################

days_dict = {
	'Monday' : [],
	'Tuesday' : [],
	'Wednesday' : [],
	'Thursday' : [],
	'Friday' : [],
	'Saturday' : [],
	'Sunday' : [],
}	

days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day_number_dict = {
	0: [],
	1: [],
	2: [],
	3: [],
	4: [],
	5: [],
	6: [],

}

# for sublist in list_of_lists:
	# schedule_day = ''
	# for string in sublist: 
		# for day_of_week in days_list:
			# if day_of_week in string:
				# schedule_day = day_of_week
	
		# if schedule_day != '':
			# days_dict[schedule_day] = string
			
for j in range(0, len(list_of_lists), 1):
	sublist = list_of_lists[j]
	day_of_week = days_list[j]
	
	print 'using', day_of_week, 'as key for', sublist
	
	for string in sublist: 
		days_dict[day_of_week].append(string)

for key in days_dict:
	print '----------'
	print key
	print days_dict[key]
	
print 'now attempting to parse time values' 

from time import strftime, strptime

def parse_inner(txt):
	times = re.findall('\d{1,2}:\d{1,2}', txt)
	if len(times) == 2:
		start_time_str = times[0]
		end_time_str = times[1]
	
		start_am = txt.split(start_time_str, 1)[1][0:2].lower() == 'am'
		start_pm = txt.split(start_time_str, 1)[1][0:2].lower() == 'pm'	

		end_am = txt.split(end_time_str, 1)[1][0:2].lower() == 'am'
		end_pm = txt.split(end_time_str, 1)[1][0:2].lower() == 'pm'
	
		am_pm = ''
		
		# do it this way because the times are not consistently marked 
		if start_am and end_pm:
			am_pm = 'midday'
			start_time = strptime(start_time_str, '%H:%M')
			end_time = strptime(end_time_str+'pm', '%I:%M%p')			
		elif start_pm and end_am: 
			am_pm = 'midnight'
			start_time = strptime(start_time_str+'pm', '%I:%M%p')			
			end_time = strptime(end_time_str, '%H:%M%')			
		elif start_am or end_am:
			am_pm = 'AM'
			start_time = strptime(start_time_str, '%H:%M')
			end_time = strptime(end_time_str, '%H:%M')
		elif start_pm or end_pm:
			am_pm = 'PM'
			start_time = strptime(start_time_str+'pm', '%I:%M%p')			
			end_time = strptime(end_time_str+'pm', '%I:%M%p')			
	
	
	
		return {
			'start_time': start_time,
			'end_time' : end_time,
			'am_pm' : am_pm,
			'activity': txt.split(times[1])[-1].split('\n')[1],
			}
	return None
	# add some functionality to find am/pm/md	

	
day_time_dict = {}

for key in days_dict:
	day_time_dict[key] = []
	for string in days_dict[key]:
		if parse_inner(string) is not None:
			day_time_dict[key].append(parse_inner(string))
			
for day in day_time_dict:
	print day
	for entry in day_time_dict[day]:
		print '%s starts at %s and ends at %s.' % (
													entry['activity'], 
													strftime('%I:%M%p', entry['start_time']), 
													strftime('%I:%M%p', entry['end_time'])
													)

print 'thanks for playing!'
	