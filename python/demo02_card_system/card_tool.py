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
    name = input("Please enter name: ")
    phone = input("Please enter phone number: ")
    qq = input("Please enter qq: ")
    email = input("Please enter email: ")
    card_dict = {
        "name" : name,
        "phone": phone,
        "qq" : qq,
        "email" : email
    }
    card_list.append(card_dict)
    print("添加 %s 成功" % name)

def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("Show all")

def search_card():
    """搜索名片"""
    print("-" * 50)
    print("search card")