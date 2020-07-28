def one_way_encrypt(password):
    alphabets_symbols = """abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()_+-={\}[]';/";:/?.>,<"""
    n = 43956889
    e = 6029
    crypt = ""
    for two_chars in range(int(len(password))-1):
        a = password[two_chars]
        b = password[two_chars+1]
        a_num = alphabets_symbols.index(a)
        b_num = alphabets_symbols.index(b)
        crypt = crypt + alphabets_symbols[((((66*a_num)+b_num)**(e))%n)%(len(alphabets_symbols))]
    return crypt


while True:
    a = input("Do you want to signup or login or exit?\n")
    if a == "exit":
        break
    if a == "signup" or a == "sign up":
        s = "{"
        file = open("login_system_data.txt")
        name = input("Enter your name\n")
        if file.read() != "":
            file.seek(
                0)  # go back to starting position and read from there again next time. If this code is not written next time when the file is read it will return an empty string.
            s = file.read()
            dataDict = eval(s)
            if name in dataDict.keys():
                print("Your account already exits. Please login.")
                continue
            else:
                s = s[0:len(s) - 1] + ","

        s += "\"" + name + "\"" + ":"
        while (True):
            password = input("Enter your password\n")
            cpassword = input("Retype password to confirm\n")
            if password == cpassword:
                print("Password confirmed!\n Your account has been created.")
                break
            else:
                print("You entered different passwords.")
        s += "\"" + one_way_encrypt(password) + "\"" + "}"
        file.close()
        file = open("login_system_data.txt", "w")
        file.write(s)
        file.close()
    if a == "login" or a == "log in":
        file = open("login_system_data.txt")
        s = file.read()
        dataDict = eval(s)
        name = input("Enter your name\n")
        if name not in dataDict.keys():
            print("Your account does not exist. Please signup.")
            continue
        while True:
            password = input("Enter your password\n")
            if one_way_encrypt(password) != dataDict[name]:
                print("wrong password")
                continue
            else:
                break
        print("You are logged into your account!")
        ans = input("Do you want to log out?\n")
        if ans == "y" or ans == "yes":
            continue
        else:
            break
