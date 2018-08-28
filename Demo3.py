#coding=utf-8
info = {"name": "test", "age": 18, "addr": "address"}
print("%s %d %s"%(info["name"], info["age"], info["addr"]))
a = [11,22]
b = [33]
a.extend(b)
print(a)
a.append(b)
print(a)
print(info.keys())