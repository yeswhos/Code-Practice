#缺省参数

gl_list = [6, 3, 9]
gl_list.sort()
gl_list.sort(reverse = True)
print(gl_list)

def print_info(name, gender = True):
    """

    :param name:
    :param gender: True 男生，False女生
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))

print_info("Fanhui")
print_info("Lulu", False)