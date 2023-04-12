# date = 04/11/2023
# author = Jakob
print('hello world!')

# 学生信息系统

# 01 需求分析
# 应该具备的功能如下：
# 添加学生及成绩信息
# 将学生信息保存到文件中
# 修改和删除学生信息
# 查询学生信息包括成绩
# 根据学生成绩进行排序
# 统计学生的总分

# 02 系统设计
# 包括7大模块：
# 录入学生信息模块
# 查找学生信息模块
# 删除学生信息模块
# 修改学生信息模块
# 学生成绩排名模块
# 统计学生总人数模块
# 显示全部学生信息模块


# 03 系统开发必备
# 操作系统：macOs
# Python解释器版本:Python 3.10.4
# 开发工具：PyCharm
# 第三方库：os，re
# 文件包括，.py & students.txt


# 04 主函数设计

# 引入模块
import time
import os

# 主函数
filename = 'student.txt'
def main():
    while True:
        menu()
        choice0 = input('请输入指令')
        if choice0 == 'exit' or choice0 == 'Q':
            break
        elif choice0.isdigit():
            # print('*')
            choice = int(choice0)
            if choice ==1:
                insert()
            elif choice ==2:
                search()
            elif choice ==3:
                delet()
            elif choice ==4:
                alter()
            elif choice ==5:
                sorting()
            elif choice ==6:
                summ()
            elif choice ==7:
                show_all()
            elif choice ==0:
                answer = input('您确认要退出吗？y/n')
                if answer == 'y':
                    print('谢谢使用，再见！')
                    break # 退出系统
                else:
                    continue
            else:
                print('请输入数字0-7选择功能')
                time.sleep(2)

        else:
            print('请输入数字0-7选择功能')
            time.sleep(2)
# 函数01






# 主界面
def menu():
    print('=============学生信息管理系统=============')
    print('-------------功能菜单-------------') # 左13 右13
    print('1. 录入学生信息')
    print('2. 查找学生信息')
    print('3. 删除学生信息')
    print('4. 修改学生信息')
    print('5. 排序')
    print('6. 统计学生总人数')
    print('7. 显示所有学生信息')
    print('0. 退出')
    print('---------------------------------')  # 左13 右13
# 函数02

# 05 学生信息维护模块设计
def insert():
    student_lst=[]
    while True:
        id = input('请输入学号（如10001）:')
        if not id:
            break
        name = input('请输入姓名:')
        if not name:
            break
        try:
            chinese = int(input('请输入语文成绩'))
            eng = int(input('请输入英语成绩'))
            math = int(input('请输入数学成绩'))
        except:
            print('输入无效，请输入有效成绩')
            continue
        student={'id':id,'name':name,'chinese':chinese,'eng':eng,'math':math}
        student_lst.append(student)
        answer = input('是否继续添加？y/n')
        if answer == 'y':
            continue
        else:
            break

    # 把录入的信息添加到文件里
    print('*****')
    save(student_lst)
    time.sleep(1)
    print('学生信息录入完毕！')
    time.sleep(3)
    print()
# 函数03

def save(lst):
    try:
        stu_txt = open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename,'w',encoding='utf-8')
    for i in lst:
        stu_txt.write(str(i)+'\n')
    stu_txt.close()
# 函数04

def delet():
    while True:
        student_id = input('请输入要删除的学生ID：')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename,'r',encoding ='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []

            flag = False
            if student_old:
                with open(filename,'w',encoding ='utf-8') as wfile:
                    d = {}
                    for i in student_old:
                        d = dict(eval(i))
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除！')
                    else:
                        print(f'未找到id{student_id}为的学生信息！')
            else:
                print('无学生信息！')
                break

            show_all()
            answer = input('是否继续删除？y/n')
            if answer == 'y':
                continue
            else:
                break
# 函数06

def alter():
    show_all()
    if os.path.exists(filename):
        with open(filename,'r',encoding ='utf-8') as file:
            student_old = file.readlines()
    else:
        return
    student_id = input('请输入要修改的学生ID：')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for i in student_old:
            d = dict(eval(i))
            if d['id'] == student_id:
                print('请开始修改')
                while True:
                    try:
                        d['name']=input('请输入姓名：')
                        d['chinese'] = input('请输入语文成绩：')
                        d['eng'] = input('请输入英语成绩：')
                        d['math'] = input('请输入数学成绩：')
                        print(d)
                        wfile.write(str(d) + '\n')
                        print('修改完成')
                    except:
                        print('您的输入有误')
                    else:
                        break
            else:
                wfile.write(str(d)+'\n')
    answer = input('是否继续修改？y/n')
    if answer == 'y':
        alter()
    else:
        return
# 函数07

# 06 查询/统计模块设计

def search():
    while True:
        id = ''
        name = ''
        student_query = []
        if os.path.exists(filename):
            mode = input('按ID查找请输入1，按姓名查找请输入2')
            if mode =='1':
                id = input('请输入学生ID')
            elif mode == '2':
                name = input('请输入学生姓名')
            else:
                print('输入有误，请重试')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for i in student:
                    d = dict(eval(i))
                    if id != '':
                        if d['id'] ==id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)

            show_student(student_query)
            # student_query.clear()
            answer= input('是否继续查询？y/n')
            if answer == 'y':
                continue
            else:
                return
# 函数05


def summ():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
           students = rfile.readlines()
           if students:
               print(f'一共有{len(students)}名学生')
           else:
               print('暂无学生信息..')
    else:
        print('暂未保存数据..')
# 函数09

# show_student应该是我这里的show_all函数
def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息')
        return
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','语文','英语','数学','总分'))
    format_data = '{:^6}\t{:^12}\t{:^10}\t{:^12}\t{:^5}\t{:^10}'
    for i in lst:
        print(format_data.format(
            i.get('id'),
            i.get('name'),
            i.get('chinese'),
            i.get('eng'),
            i.get('math'),
            int(int(i.get('chinese'))+int(i.get('eng'))+int(i.get('math')))
        ))
# 函数10


def show_all():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
        for i in students:
            student_lst.append(eval(i))
        if student_lst:
            show_student(student_lst)
    else:
        print('暂未保存过数据！')
# 函数11




# 07 排序模块设计

def sorting():
    show_all()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
        students_new =[]
        for i in students:
            d = dict(eval(i))
            students_new.append(d)
    else:
        return
    asc_or_desc = input('请选择（0. 升序 1. 降序）：')
    if asc_or_desc =='0':
        asc_or_desc_bool =False
    elif asc_or_desc =='1':
        asc_or_desc_bool =True
    else:
        print('您的输入有误，请重试')
        sorting()

    mode = input('1. 按语文排序 2. 英语 3. 数学 0.总成绩')
    if mode == '1':
        students_new.sort(key=lambda x:int(x['chinese']),reverse=asc_or_desc_bool)
    elif mode == '2':
        students_new.sort(key=lambda x:int(x['eng']), reverse=asc_or_desc_bool)
    elif mode == '3':
        students_new.sort(key=lambda x:int(x['math']), reverse=asc_or_desc_bool)
    elif mode == '0':
        students_new.sort(key=lambda x:int(x['chinese'])+int(x['eng'])+int(x['math']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重试')
        sorting()
    show_student(students_new)
    answer = input('是否继续查询？y/n')
    if answer == 'y':
        sorting()
    else:
        return
# 函数08

# 08 项目打包
#（课程只教了win系统打开，查一下github怎么在苹果打包，或者把这个项目更新到github上--使用mkdocs的服务）

if __name__ == '__main__':
    main()

print('done!')


print('Goodbye')