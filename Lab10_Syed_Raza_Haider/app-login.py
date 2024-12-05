from flask import Flask, redirect, request, url_for#, Response
from flask_login import LoginManager, UserMixin, current_user,login_user,logout_user, login_required

app=Flask(__name__)

app.secret_key='super secret string'

login_manager=LoginManager()
login_manager.init_app(app)
users={'student@ryerson.ca':{'password':'secret'}}


class User(UserMixin):
    pass
       
#Login manager loads user by email from mock database
@login_manager.user_loader
def user_loader(email):
       if email not in users:
           return
       user = User()
       user.id = email
       return user
# Login manager loads user by email from form requesting username
#and password
@login_manager.request_loader
def request_loader(request):
       email = request.form.get('email')
       if email not in users:
           return
       user = User()
       user.id = email
       return user    
# Login route that is used to access secure routes.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return ''' <form action='login' method='POST'>
        username &nbsp;<input type='text' name='email' id='email'
placeholder='email'/> <br /> &nbsp; <br />
 password &nbsp;<input type='password' name='password'
id='password' placeholder='password'/> <br /> &nbsp; <br />
        <input type='submit' name='submit'/>
        </form>'''
 
    email = request.form['email']
    if email in users and request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        login_user(user)
        return redirect(url_for('protected'))
    return 'Incorrect login'
# Protected route hence user must be logged in to access it.
@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id
# Logout from current session
@app.route('/logout')
def logout():
    logout_user()
    return 'Logged out'
# Handle unauthenticated users that access protected routes
@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401


if __name__=='__main__':
    app.run(port=5000,debug=True)