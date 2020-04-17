student = [{
        "name":"zhangsan",
        "age": 16,
    },
    {
        "name" : "lisi",
        "age" : 17,
    }
]
for stu in student:
    if stu["name"] == "wangwu":
        print("here")
        break
else:
    print("查无此人")