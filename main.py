#python3 -m pip install flask;
#python3 -m pip install flask_session;
#pip3 uninstall Werkzeug
#pip3 install Werkzeug==0.16.0


from flask import Flask
from flask import render_template
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response 

from customer import customerList

import pymysql, json, time

from flask_session import Session #Serverside Sessions

app = Flask(__name__,static_url_path='')

SESSION_TYPE = 'filesystem'

app.config.from_object(__name__)
Session(app)

@app.route('/set')
def set():
    session['time'] = time.time()
    return 'set'
    
@app.route('/get')
def get():
    return str(session['time'])

@app.route('/nothing')
def nothing():
    print('hi')
    return ''

@app.route('/basichttp')
def basichttp():
    if request.args.get('myvar') is not None:
        a = request.args.get('myvar')
        return 'your var:' + request.args.get('myvar')
    else:
        return 'myvar not set' 

@app.route('/')
def home():
    return render_template('test.html', title='Home', msg='Welcome!')

@app.route('/index')
def index():
    user = {'username': 'Anusuya'}
    items = [
        {'name':'Apple','price':2.34},
        {'name':'Orange','price':4.88},
        {'name':'Grape','price':2.44}
    ]
    return render_template('index.html', title='MyPage', user=user, items=items)

@app.route('/main') 
def main():
    if checkSession() == False: #check to make sure the user is logged in
        return redirect('login')
    userinfo = 'Hello, ' + session['user']['fname']
    session['user']['type'] == '1'
    return render_template('main.html', title='Main Menu',msg=userinfo)

def checkSession():
    if 'active' in session.keys():
        timeSinceLastActive = time.time() - session['active']
        print(timeSinceLastActive)

        if timeSinceLastActive > 15:
            session['msg'] = 'Your Session has Timed Out.'
            return False
        else:
            session['active'] = time.time()
            return True
    else:
        return False

@app.route('/login', methods = ['GET','POST'])
def login():
 
    if request.form.get('email') is not None and request.form.get('password') is not None:
        c = customerList()
        if c.tryLogin(request.form.get('email'),request.form.get('password')):
            print("Login Ok") 
            session['user'] = c.data[0]
            session['active'] = time.time()

            return redirect('main')
        else:
            print("Login Failed...!!!") 
            return render_template('login.html', title='Login',msg='Incorrect Username or Password...!!!')
    else:
        #if 'msg' not in session.keys():
        if 'msg' not in session.keys() or session['msg'] is None:
            m = 'Type your email and password to continue.'
        else:
            m = session['msg']
            session['msg'] = None
        return render_template('login.html', title='Login', msg=m)

@app.route('/addCustomer', methods = ['GET','POST'])
def addCustomer():
    if checkSession() == False: #check to make sure the user is logged in
        return redirect('login')
    if request.form.get('fname') is None:
        c = customerList()
        c.set('fname','')
        c.set('lname','')
        c.set('email','')
        c.set('password','')
        c.set('subscribed','')
        c.add() 
        return render_template('addCustomer.html', title='New Customer', customers=c.data[0])

    else:
        c = customerList()
        c.set('fname',request.form.get('fname'))
        c.set('lname',request.form.get('lname'))
        c.set('email',request.form.get('email'))
        c.set('password',request.form.get('password'))
        c.set('subscribed',request.form.get('subcribed'))
        c.add() 
        if c.verifyNew():
            c.insert()
            print(c.data)
            return render_template('savedCustomer.html', title='Saved Customer', customer=c.data[0])
        else:
            return render_template('addCustomer.html', title='Customer Not Saved', customer=c.data[0], msg=c.errList)

@app.route('/editCustomer', methods = ['GET','POST'])
def editCustomer():
    if checkSession() == False: #check to make sure the user is logged in
        return redirect('login')
    c = customerList()
    c.set('id',request.form.get('id'))
    c.set('fname',request.form.get('fname'))
    c.set('lname',request.form.get('lname'))
    c.set('email',request.form.get('email'))
    c.set('password',request.form.get('password'))
    c.set('subscribed',request.form.get('subcribed'))
    c.add() 
    c.update()
    print(c.data)
    #return ''
    return render_template('savedCustomer.html', title='Customer Saved', customer=c.data[0])

@app.route('/allCustomers')
def allCustomers():
    if checkSession() == False: #check to make sure the user is logged in
        return redirect('login')
    c = customerList()
    c.getAll()
    print(c.data)
    #return ''
    return render_template('customers.html', title='Customer List', customers=c.data)

@app.route('/customersByID') 
def customersByID():
    if checkSession() == False: #check to make sure the user is logged in
        return redirect('login')
    c = customerList() 
    if request.args.get(c.pk) is None:
        return render_template('customersError.html', msg='No Customer ID is given.')
    
    c.getByID(request.args.get(c.pk))
    if len(c.data) <= 0:
        return render_template('customersError.html', msg='Customer ID does not exist')
    print(c.data)
    #return ''
    return render_template('customersByID.html', title='Customer', customer=c.data[0])

@app.route('/logout', methods = ['GET','POST']) 
def logout():
    del session['user']
    del session['active']
    return render_template('login.html', title='Login',msg='You have Logged Out...!!!')
    

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
   app.secret_key = '1234'
   app.run(host='127.0.0.1',debug=True)

