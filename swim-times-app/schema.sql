DROP TABLE IF EXISTS POOLS;
CREATE TABLE POOLS(
	id integer primary key autoincrement,
	name text not null,
	address text not null,
	city text not null,
	zip_code text not null,
	neighborhood text not null
);