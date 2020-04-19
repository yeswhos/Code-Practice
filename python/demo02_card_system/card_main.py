while True:

    account_str = input("Select operation: ")
    print("Your choice is: %s" % account_str)

    if account_str in ["1", "2", "3"]:
        pass

    elif account_str == "0":
        print("Thanks for using, see you later")
        break

    else:
        print("invalid choice, select again please")