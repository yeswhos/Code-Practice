import card_tool

while True:
    # TODO(Fanhui) 显示功能菜单
    card_tool.show_menu()

    account_str = input("Select operation: ")
    print("Your choice is: %s" % account_str)

    if account_str in ["1", "2", "3"]:
        if account_str == "1":
            pass
        elif account_str == "2":
            pass
        elif account_str == "3":
            pass

    elif account_str == "0":
        print("Thanks for using, see you later")
        break

    else:
        print("invalid choice, select again please")