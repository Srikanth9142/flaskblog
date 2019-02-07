from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='7e4f75670462c4506dc181474b1e2bda'



posts=[
    {'author':'srikanth',
      'title':'first post',
      'date':'Febuary 6,2019',
      'content':'Hello Everyone im srikanth and iam new to this blog.'
    },
    {
      'author':'sriharsha',
      'title':'new post',
      'date':'Febuary 7,2019',
      'content':'Hello Everyone im sriharsha and iam new to this blog.'

    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!','success')
    return redirect(url_for('home'))
  return render_template('register.html',title='Register',form=form)


@app.route("/login")
def login():
  form = LoginForm()
  return render_template('login.html',title='Login',form=form)


if __name__=="__main__":
    app.run(debug=True)
