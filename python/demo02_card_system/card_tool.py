card_list = []

def show_menu():
    '''显示菜单'''
    print("*" * 50)
    print("Welcome")
    print("1. Add new card")
    print("2. Show hands")
    print("3. Search for card")
    print("0. Exit")
    print("*" * 50)

def new_card():
    """新增名片"""
    print("-" * 50)
    print("Add new card")
    name_str = input("Please enter name: ")
    phone_str = input("Please enter phone number: ")
    qq = input("Please enter qq: ")
    email = input("Please enter email: ")
    card_dict = {
        "name" : name_str,
        "phone": phone_str,
        "qq" : qq,
        "email" : email
    }
    card_list.append(card_dict)
    print("添加 %s 成功" % name_str)

def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("Show all")
    if len(card_list) == 0:
        print("empty card")
        #return 后面是空的，不会返回任何结果
        return
    for name in ["name", "phone", "qq", "email"]:
        print(name, end = "\t\t")
    print(" ")
    for card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card["name"], card["phone"], card["qq"], card["email"]))

def search_card():
    """搜索名片"""
    print("-" * 50)
    print("search card")
    find_name = input("enter searched name: ")
    for card in card_list:
        if card["name"] == find_name:
            print("There it is")
            print("name\t\tphone\t\tqq\t\temail")
            print("%s\t\t%s\t\t%s\t\t%s" % (card["name"], card["phone"], card["qq"], card["email"]))
            deal_card(card)
            break
    else:
        print("not on the list")

def deal_card(find_dict):
    """

    :param find_dict: 查找值之后的操作
    """
    account_operation = input("please select, 1 modify, 2 delete, 0 back to upper level")
    if account_operation == "1":

        find_dict["name"] = input_card_info(find_dict["name"], "modify name")
        find_dict["phone"] = input_card_info(find_dict["phone"], "modify phone")
        find_dict["qq"] = input_card_info(find_dict["qq"], "modify qq")
        find_dict["email"] = input_card_info(find_dict["email"], "modify email")
        print("modify success")
    elif account_operation == "2":
        card_list.remove(find_dict)
        print("delete success")

def input_card_info(value, message):
    """

    :param value: 字典原有的值
    :param message: 更新的值
    :return: 返回更新的值或者无修改的时候返回原有的值
    """
    attention_info = input(message)
    if len(attention_info) > 0:
        return attention_info
    else:
        return value
