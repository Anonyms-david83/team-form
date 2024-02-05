from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SECRET_KEY'] = '7713004508cf70ebb23bccd5d3a7689f0a166936b122896d' 

db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    fname = db.Column(db.String, nullable=True)
    lname = db.Column(db.String, nullable=True)
    score = db.Column(db.Float, nullable=True)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    template_name = 'index.html'

    if request.method == 'POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        score = request.form['score']

        new_entry = Form(fname=first_name, lname=last_name, score=score)
        db.session.add(new_entry)
        db.session.commit()
        
       
        flash('Your data has been successfully saved!', 'success')

        return redirect(url_for('success'))

    return render_template(template_name)


@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run()
