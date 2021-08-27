import datetime
from flask import Flask, render_template,jsonify, request,g, abort, session, redirect, url_for
from dao.dataDao import DataDao
from untils.getConfig import getConfig
from entity.user import User
from entity.article import Article


app = Flask(__name__)
app.config['DEBUG'] = getConfig('flask','DEBUG')
app.config['SECRET_KEY'] = getConfig('flask','SECRET_KEY')
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(minutes=int(getConfig('flask','SESSION_TIME')))


@app.before_first_request
def start():

    pass

@app.before_request
def authentication():
    """
    身份认证
        所有模块需要登录才能进行访问
            通过比对cookie信息和session
    """

    """
        session如果被清空了,重新初始化        
    """

    try:
        temp = session['userID']
        temp = session['message']
    except KeyError as e:
        session['userID'] = None
        session['message'] = None

    def filter():
        """
        添加不需要身份认证的url
        :return: true:不需要身份验证 false:需要身份验证
        """

        # 静态文件
        if request.path.endswith('.css') or request.path.endswith('.js'):
            return True

        # 登录注册页面,注册页面
        if request.path == '/login' or request.path == '/regist' or request.path == '/checkid':
            return True

        return False

    if filter():
        pass
    else:
        userID = request.cookies.get('userID')
        if userID == session['userID']:
            pass
        else:
            return redirect(url_for('login'))

@app.after_request
def cookie(response):
    """
    设定cookie
        用户信息:从session中获取
    """
    userID = session['userID']
    if not userID is None:
        response.set_cookie('userID',userID)
    return response




@app.route('/',methods=['GET','POST'] )
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        userid = request.form.get('userNameOrEmailAddress')
        userpwd = request.form.get('password')
        user = User(userid,password=userpwd)
        result = user.login()
        if result:
            session['userID'] = userid
            session['message'] = result
            return redirect(url_for('index'))
        else:
            return '密码错误,请重新登录'

@app.route('/regist',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        userID = request.form.get('userID')
        userpwd = request.form.get('password')
        username = request.form.get('username')
        useremail = request.form.get('email')
        user = User()
        result = user.regist(userID,userpwd,username,useremail)
        if result:
            return redirect(url_for('login'))
        else:
            abort(500)

@app.route("/checkid",methods=['POST'])
def checkid():
    id = request.form.get("id")
    result = User().checkID(id)
    if result == 3:
        abort(500)
    if result:
        return jsonify({'check':'fail'})
    else:
        return jsonify({'check':'ok'})



@app.route('/index',methods=['GET'])
def index():
    limit = 10  # 每页10条
    pageNum = request.args.get('page')    # 页码
    if pageNum is None:
        pageNum = 0
    else:
        pageNum = int(pageNum)-1
    username = session['message'][1]
    now = datetime.datetime.now()
    time = now.strftime('%Y-%m-%d %H:%M:%S')
    articles = Article().getArticles(pageNum,limit)
    totalNum = Article().getTotalNum()

    totalPageNum = totalNum//limit+1
    pageNum += 1

    return render_template(
        'index.html',time=time,username=username,articles = articles,pageNum=pageNum,
        totalPageNum = totalPageNum
    )


@app.route('/page/<int:num>')
def page(num):
    """
        文章详情页面
    """
    username = session['message'][1]
    now = datetime.datetime.now()
    time = now.strftime('%Y-%m-%d %H:%M:%S')

    article = Article()
    data = article.getText(num)

    return render_template('page.html',time=time,username=username,data = data,num=num)


@app.route('/data/<int:num>')
def data(num):
    """
        文章内容页
    """
    article = Article()
    data = article.getText(num)

    return render_template('data.html',text = data[1])


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)