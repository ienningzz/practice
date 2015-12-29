from flask import Flask, render_template, session, redirect, url_for, flash,request,abort
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:wzn19970314@127.0.0.1/mysql_python'
app.config['SQLAlchemy_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)




class User_Name(db.Model):
    __tablename__ = 'user_name'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(24), unique=True,index=True)
    password = db.Column(db.String(20),index=True)


class Page(db.Model):
    __tablename__ = 'passage'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150),unique=True,index=True)
    text = db.Column(db.String(2000))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def show_entries():
    entries = Page.query.all()
    return render_template('show_entries.html',entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    title = Page(title=request.form['title'],text=request.form['text'])
    db.session.add(title)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))



@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User_Name.query.filter_by(user=request.form['username']).first()
        if user is None:
            error = 'Invalid username'
        else:
            user_password = User_Name.query.filter_by(user=request.form['username']).first().password
            if user_password == request.form['password']:
                flash('Login success!')
                session['logged_in'] = True
                return redirect(url_for('show_entries'))
            else:
                error = 'Invalid password'
    return render_template('login.html',error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/logup',methods=['GET','POST'])
def logup():
    error=None
    if request.method == 'POST':
        user = User_Name.query.filter_by(user=request.form['username']).first()
        if user is None:
            user = User_Name(user=request.form['username'],password=request.form['password'])
            db.session.add_all([user])
            db.session.commit()
            flash("OK!You have logup success")
            return redirect(url_for('show_entries'))
        else:
            error = "Sorry,You had loguping!"
    return render_template('logup.html',error=error)
if __name__ == '__main__':
    db.create_all()
    manager.run()
