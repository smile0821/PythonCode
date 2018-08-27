#coding=utf-8
names = []
names.append("aa")
names.append("bb")
print(names)
names.insert(0,123)
print(names)
names2 = [123,456,789]
names3 = names + names2
print(names3)
names.extend(names2)
print(names)
names.pop()
print(names)
names.remove(123)
print(names)
print(names[-1])
print(names[2:3])
del names[0]
print(names)
#修改
names[0] = "aa"
print(names)
if 123 in names:
    print("存在")