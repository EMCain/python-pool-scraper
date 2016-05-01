DROP TABLE IF EXISTS POOLS;
CREATE TABLE POOLS(
	id integer primary key autoincrement,
	name text not null,
	address text not null,
	city text not null,
	zip_code text not null,
	neighborhood text not null
);

CREATE TABLE ACTIVITIES(
	id integer primary key autoincrement,
	name text not null
);
/* eventually will add more info like age restrictions */

CREATE TABLE DAYS_OF_WEEK(
	id integer primary key autoincrement,
	name text not null
);

CREATE TABLE EVENTS(
	id integer primary key autoincrement,
	activity_id integer not null,
	day_of_week_id integer not null,
	pool_id integer not null, 
	start_time time not null,
	end_time time not null
);
/* create foreign key constraints with activity, day, pool tables */