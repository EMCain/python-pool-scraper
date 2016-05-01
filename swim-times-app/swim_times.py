# finished step 4 in flaskr tutorial here

__author__ = 'Emily'

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash
from contextlib import closing

DATABASE = '.\\tmp\\swim_times.db'
DEBUG = True
SECRET_KEY = 'devkey'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


# http://stackoverflow.com/questions/13484771/operationalerror-unable-to-open-database-file-in-pycharm-with-flask-ide-plug-in
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


# VIEWS
@app.route('/')
def show_pools():
    cur = g.db.execute('SELECT name, address, city, zip_code, neighborhood FROM POOLS ORDER BY name')
    pools = [dict(name=row[0], address=row[1], city=row[2], zip_code=row[3], neighborhood=row[4]) for row in cur.fetchall()]
    return render_template('show_pools.html', pools=pools)

@app.route('/add', methods=['POST'])
def add_pool():
    print 'adding pool'
    if not session.get('logged_in'):
        print 'not logged in'
        abort(401)
    print 'about to execute g.db'
    g.db.execute('INSERT INTO POOLS (name, address, city, zip_code, neighborhood) values (?, ?, ?, ?, ?)',
                 [request.form['name'], request.form['address'], request.form['city'], request.form['zip_code'], request.form['neighborhood']])
    print 'about to commit g.db'
    g.db.commit()
    flash('New pool was added')
    print 'about to redirect'
    return redirect(url_for('show_pools'))

@app.route('/activities')
def show_activities():
    cur = g.db.execute('SELECT * from ACTIVITIES ORDER BY id')
    activites = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
    return render_template('show_activities.html', activites=activites)

@app.route('/add_activity', methods=['POST'])
def add_activity():
    print "adding activity"
    if not session.get('logged_in'):
        print 'not logged in'
        abort(401)
    g.db.execute('INSERT INTO ACTIVITIES (name) values (?)',
                 [request.form['name']]
                 )
    g.db.commit()
    flash('new activity was added')
    return redirect(url_for('show_activities'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_pools'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_pools'))


if __name__ == '__main__':
    app.run()