# 打印系统基本信息
print("="*50)
print("学生管理系统 V1.0")
print("1. 新增学生信息.")
print("2. 修改学生信息.")
print("3. 查询学生信息.")
print("3. 查询学生信息.")
print("4. 删除学生信息.")
print("5. 退出系统.")
print("="*50)

# 学生的详细信息
stu_infos = []

while True:
    num = int(input("请输入选项序号:"))
    if num == 1:
        stu_no = input("请输入学生学号:")
        stu_name = input("请输入学生姓名:")
        stu_age = int(input("请输入学生年龄:"))
        stu_phone_num = input("请输入学生联系电话:")
        stu_addr = input("请输入学生地址:")
        stu_info = {"no": stu_no, "name": stu_name, "age": stu_age, "phone": stu_phone_num, "address": stu_addr}
        # 将字典添加到列表中
        stu_infos.append(stu_info)
    elif num == 2:
        # 修改学生姓名
        mod_stu_no = input("请输入修改学生学号：")
        mod_stu_name = input("请输入要修改的学生姓名：")
        for student in stu_infos:
            for item in student:
                if item["no"] == mod_stu_no:
                    item["name"] == mod_stu_name
                else:
                    break
    elif num == 3:
        # 查询学生信息
        query_stu_no = input("请输入要查询的学生学号:")
        if query_stu_no == "":
            for student in stu_infos:
                print(student)
        else:
            for student in stu_infos:
                if student["no"] == query_stu_no:
                    print(student)
                    break
                else:
                    continue
    elif num == 4:
        # 删除学生信息
        del_stu_no = input("请输入要删除的学生学号：")
        for student in  stu_infos:
            if student["no"] == del_stu_no:
                stu_infos.remove(student)
                break
            else:
                continue
    elif num == 5:
        break
    else:
        print("输入有误，请重新输入.")