# date = 04/13/2023
# author = Jakob

# 学生信息管理系统正式代码

# 01 主函数设计

# 结构：引入模块+文件地址+主函数+其他函数+main调用

# 引入模块
import time
import os

# 主函数
filename = 'student.txt'
# 函数01
def main():
    while True:
        menu() # 02 主界面模块
        choice = input('请输入指令')
        # 增加强制退出指令
        if choice == 'exit' or choice == 'Q':
            break
        elif choice.isdigit(): # 判断输入指令是否为数字
            if choice =='1':
                insert() # 03 录入学生信息模块
            elif choice =='2':
                search() # 04 查找学生信息模块
            elif choice =='3':
                delet() # 05 删除学生信息模块
            elif choice =='4':
                alter() # 06 修改学生信息模块
            elif choice =='5':
                sorting() #07 学生成绩排名模块
            elif choice =='6':
                summ() # 08 统计学生总人数模块
            elif choice =='7':
                show_all() # 09 显示全部学生信息模块
            elif choice =='0':
                answer = input('您确认要退出吗？y/n')
                if answer == 'y':
                    print('谢谢使用，再见！') # 退出主界面
                    break # 退出系统
                else:
                    continue
            else:
                print('请输入数字0-7选择功能')
                time.sleep(2)

        else:
            print('请输入数字0-7选择功能')
            time.sleep(2)

# 02 主界面模块
# 函数02
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

# 03 录入学生信息模块，包括insert和save 2个函数
# 单个学生的信息以字典存储，学号、姓名、成绩分别是一组键值对，所有学生信息汇总到列表中，再用for循环分行写入txt文件
# 函数03
def insert():
    student_lst=[] # student_lst为所有学生信息汇总，即[{stu01},{stu02}]
    while True:
        id = int(input('请输入学号（如10001）:')) # ID 改为int类型，可以按学号排序
        if not id:
            break
        name = input('请输入姓名:')
        if not name:
            break
        try:
            chinese = int(input('请输入语文成绩:')) # 成绩为int类型，可以按大小进行排序
            eng = int(input('请输入英语成绩:'))
            math = int(input('请输入数学成绩:'))
        except:
            print('输入无效，请输入有效成绩')
            continue
        student={'id':id,'name':name,'chinese':chinese,'eng':eng,'math':math} # student是字典类型，即{'key01':value01,'key02':value02}
        student_lst.append(student)
        # 把原始存储数据读取到缓存
        student_lst_old = []
        load(student_lst_old)
        # 把新增的学生信息加到缓存列表中
        for i in student_lst_old:  # 这里i指的是每一个学生的信息，即列表里的字典
            student_lst.append(i)
        answer = input('是否继续添加？y/n')
        if answer == 'y':
            continue
        else:
            break

    # 把录入的信息添加到文件里
    # 这里加一步排序，保证存储文件中按ID进行排序
    print('*****')
    save(student_lst)
    time.sleep(1)
    print('学生信息录入完毕！')
    time.sleep(2)
    print()

# 函数04
# 保证读存一致，存时交进来的是列表包字典格式，读时给出去的也是同样形式，都用student_lst参数表示
# 好处是增删改查只需要处理到student_lst的层面，剩下的交给2个函数
def save(lst):
    # 按学号排序(包括原始+新增部分)
    lst.sort(key=lambda x: int(x['id']), reverse=False)
    # 写入文件，真正的save部分，覆盖模式
    with open(filename, 'w', encoding='utf-8') as file:
        for i in lst:
            file.write(str(i)+'\n')

# 04 查找学生信息模块
# while循环内可持续查询，将txt存储文件中str类型分行还原为字典，再通过for循环把与查询ID、姓名匹配的字典放到缓存列表里，通过show函数进行显示
# 函数05
def search():
    student_lst = []
    load(student_lst)
    while student_lst:
        # 选择查询类型
        mode = input('按ID查找请输入1，按姓名查找请输入2')
        student_query = []  # 放在循环里面，放外面不会被初始化
        flag = False  # 初始化为负，找到后为正
        if mode == '1':
            id = input('请输入学生ID')
            for student in student_lst:
                if student['id'] == id:
                    student_query.append(student)
                    flag = True
        elif mode == '2':
            name = input('请输入学生姓名')
            for student in student_lst:
                if student['name'] == name:
                    student_query.append(student)
                    flag = True
        # 显示查询结果
        if flag:  # 这一层能不能提出来？
            show_student(student_query)
        else:
            print('未找到符合条件的学生或输入错误')
        # 是否继续查询
        answer = input('是否继续查询？y/n')
        if answer == 'y':
            continue  # 这里继续下一轮循环，列表被初始化
        else:
            break  # 这里有问题
    else:
        print('无学生信息！')
        time.sleep(2)

# 05 删除学生信息模块
# 函数06
def delet():
    student_lst = []
    load(student_lst)
    while student_lst:
        student_lst_new = []
        flag = False
        student_id = input('请输入要删除的学生ID：')
        for student in student_lst:
            if student['id'] != student_id:
                student_lst_new.append(student)
            else:
                flag = True
        student_lst= student_lst_new
        if flag:
            print(f'id为{student_id}的学生信息已被删除！')
        else:
            print(f'未找到id{student_id}为的学生信息！')
        save(student_lst)
        show_all()
        answer = input('是否继续删除？y/n')
        if answer == 'y':
            continue
        else:
            break
    else:
        print('无学生信息！')
        time.sleep(2)




# 06 修改学生信息模块

# 函数07
def alter():
    # 显示所有学生信息
    show_all()
    # 加载学生列表到缓存列表，数据格式还是列表包字典
    student_lst = []
    load(student_lst)
    while student_lst:
    # 输入要修改的学生ID
        student_id = int(input('请输入要修改的学生ID：'))
        id_lst =[i['id'] for i in student_lst]
        print(id_lst)
        if student_id in id_lst:
            print('请开始修改')
            student_lst =[i for i in student_lst if i['id'] != student_id]
            d = {}
            d['id'] =student_id
            d['name']=input('请输入姓名：')
            d['chinese'] = int(input('请输入语文成绩：'))
            d['eng'] = int(input('请输入英语成绩：'))
            d['math'] = int(input('请输入数学成绩：'))
            print(d)
            student_lst.append(d)
            print('修改完成')
            # 保存数据到文件
            save(student_lst)
            # 判断是否继续修改
            answer = input('是否继续修改？y/n')
            if answer == 'y':
                continue
            else:
                return
        # 没有输入的ID，报错提示并返回循环
        else:
            print('未查询到ID为的学生信息，请重试')
            continue
    # 不存在学生信息，提示并直接退出




#07 学生成绩排名模块
# 函数08
def sorting():
    # 显示所有学生信息
    show_all()
    student_lst = []
    load(student_lst)
    while student_lst:
        students_temp = student_lst
        asc_or_desc = int(input('请选择（0. 升序 1. 降序）：'))
        # 选择按哪个字段排序
        flag = True
        mode = input('1. 按语文排序 2. 英语 3. 数学 0.总成绩')
        if mode == '1':
            students_temp.sort(key=lambda x: int(x['chinese']), reverse=asc_or_desc)
        elif mode == '2':
            students_temp.sort(key=lambda x: int(x['eng']), reverse=asc_or_desc)
        elif mode == '3':
            students_temp.sort(key=lambda x: int(x['math']), reverse=asc_or_desc)
        elif mode == '0':
            students_temp.sort(key=lambda x: int(x['chinese']) + int(x['eng']) + int(x['math']),
                              reverse=asc_or_desc)
        else:
            print('输入有误，请重试')
            flag = False # 这里还是不太理想
        # 显示结果
        if flag:
            show_student(students_temp)
            # 是否继续
            answer = input('是否继续查询？y/n')
            if answer == 'y':
                continue
            else:
                return
    else:
        return
    # 选择升序和降序


# 08 统计学生总人数模块
# 函数09
def summ():
    student_lst = []
    load(student_lst)
    if student_lst:
        print(f'一共有{len(student_lst)}名学生')
    else:
        print('暂未保存数据..')

# 09 显示全部学生信息模块
# 包括show_student和show_all 2个函数
# 函数10
def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息！')
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
# 函数11
def show_all():
    student_lst = []
    load(student_lst)
    show_student(student_lst)


# 函数12
# 加一个load函数，加载缓存，把原始文件中的str转换成单行字典，再交给一个列表
def load(lst):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_old = file.readlines()
            for i in student_old:
                student = dict(eval(i))
                lst.append(student)

if __name__ == '__main__':
    main()
