from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Account:', validators=[validators.required(), validators.Length(min=6, max=16)])
    password = TextField('Mobile:', validators=[validators.required(), validators.Length(min=10, max=12)])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print(form.errors)
    if request.method == 'POST':
        account-number=request.form['account-number']
        full-name=request.form['full-name']
        fathers-name=request.form['fathers-name']
        # Take rest values in the same way and print below.
        print(account, " ", full-name, " ", fathers-name)
        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('login.html', form=form)
 
if __name__ == "__main__":
    app.run()