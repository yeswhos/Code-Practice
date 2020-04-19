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
    for name in ["name", "phone", "qq", "email"]:
        print(name, end = "\t\t")
    print(" ")
    for card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card["name"], card["phone"], card["qq"], card["email"]))

def search_card():
    """搜索名片"""
    print("-" * 50)
    print("search card")