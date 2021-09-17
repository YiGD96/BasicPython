import os
from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy'

@app.route('/user')
def user():
    return '익명'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/user/<username>/<int:age>')
def show_user_profile2(username,age):
    return f'User {username} age {age}'

# get 방식으로 받을때
@app.route('/login')
def login():
    user = request.args.get('name')
    age = request.args.get('age')
    return f'user {user} age:{age}'

# Post 방식으로 받을때
@app.route('/login',methods=['POST'])
def login2():
    user = request.form['name']
    age = request.form['age']
    return f'user {user} age:{age}' 

# Post 방식으로 받을때2
@app.route('/login',methods=['POST'])
def login3():
    # user = request.form['name']
    # age = request.form['age']
    return render_template('result.html',result=request.form)

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        f=request.files['file'] # name을 받아서 넘어옴
        dirname=os.path.dirname(__file__)+'/uploads/'+f.filename
        print(dirname)
        f.save(dirname)
        return redirect('/') # 첫페이지로 보내기


if __name__ =='__main__':
    app.run(debug=True,port=80) #5000포트 까지는 아니고 80은 생략가능해서


# {%  %} #if, for문 사용
# {{ }}  #값을 찍어줄때
# {{# #}} #여러문장 주석