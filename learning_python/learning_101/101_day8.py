# date = 04/14/2023
# author = Jakob
print('hello world!')

# P2，前端引入和html标签

# 引入模块
from flask import Flask, render_template

# 函数部分
app = Flask(__name__)

@app.route('/show/info')
def index():
    # return '中<h1>国</h1><span style="color:red;">联通</span>' # 一句里面引号如果有包含关系，需要用双引号和单引号区分
    return render_template('index01.html')

@app.route('/get_news')
def get_news():
    # return '中<h1>国</h1><span style="color:red;">联通</span>' # 一句里面引号如果有包含关系，需要用双引号和单引号区分
    return render_template('index.html')


# main函数
if __name__ == '__main__':
    app.run()


print('goodbye!')