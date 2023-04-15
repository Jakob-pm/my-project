# date = 04/15/2023
# author = Jakob
print('hello world!')

# P6，表单标签

# 引入模块
from flask import Flask, render_template,request

# 函数部分
app = Flask(__name__)

@app.route('/index02')
def index():
    return render_template('index02.html')

# 案例：用户注册
@app.route('/register', methods =['GET','POST'])
def register():
    if request.method =='GET':
        return render_template('register.html')
    else:
        print(request.form)
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        gender = request.form.get('gender')
        hobby_lst = request.values.getlist('hobby')
        print(hobby_lst)
        for i in hobby_lst:
            print(type(i))
        city = request.form.get('city')
        strength_lst = request.values.getlist('strength')
        remark = request.form.get('remark')
        print(remark)
        # 将用户信息写入文件
        user_lst = []
        user_info = {}
        city_lst = ['北京', '上海', '深圳', '广州', '张店', '青岛', '怒江']
        gender_lst = ['女', '男']
        hobby_lst_0 = ['唱', '跳', 'rap', '两年半']
        strength_lst_0 = ['阿里嘎多美羊羊桑', '一切邪恶终将绳之于法', '鸡汤来喽', '战鹰']
        user_info['用户名'] = user
        user_info['密码'] = pwd
        user_info['性别'] = gender_lst[int(gender)]
        user_info['爱好'] = [hobby_lst_0[int(i)] for i in hobby_lst]
        user_info['城市'] = city_lst[int(city)]
        user_info['擅长领域：'] = [strength_lst_0[int(i)] for i in strength_lst]
        user_info['备注'] = remark
        user_lst.append(user_info)
        save(user_lst)
        return '注册成功'

@app.route('/do/reg')
def do_register():
    print(request.args)
    return '注册成功'

# @app.route('/post/reg',methods =['POST'])
# def post_register():
#     print(request.form)
#     user = request.form.get('user')
#     pwd = request.form.get('pwd')
#     gender = request.form.get('gender')
#     hobby_lst = request.values.getlist('hobby')
#     print(hobby_lst)
#     for i in hobby_lst:
#         print(type(i))
#     city = request.form.get('city')
#     strength_lst = request.values.getlist('strength')
#     remark = request.form.get('remark')
#     print(remark)
#     # 将用户信息写入文件
#     user_lst = []
#     user_info = {}
#     city_lst = ['北京','上海','深圳','广州','张店','青岛','怒江']
#     gender_lst =['女','男']
#     hobby_lst_0 = ['唱','跳','rap','两年半']
#     strength_lst_0 =['阿里嘎多美羊羊桑','一切邪恶终将绳之于法','鸡汤来喽','战鹰']
#     user_info['用户名'] = user
#     user_info['密码'] = pwd
#     user_info['性别'] = gender_lst[int(gender)]
#     user_info['爱好'] = [hobby_lst_0[int(i)] for i in hobby_lst]
#     user_info['城市'] = city_lst[int(city)]
#     user_info['擅长领域：'] = [strength_lst_0[int(i)] for i in strength_lst]
#     user_info['备注'] = remark
#     user_lst.append(user_info)
#     save(user_lst)
#     return '注册成功'

def save(lst):
    filename = 'user_storge.txt'
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            for i in lst:
                file.write(str(i) + '\n')
    except:
        with open(filename, 'w', encoding='utf-8') as file:
            for i in lst:
                file.write(str(i)+'\n')

# 登录页面
@app.route('/login', methods =['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        print(request.form)
        return '登录成功'

# main函数
if __name__ == '__main__':
    app.run()


print('goodbye!')