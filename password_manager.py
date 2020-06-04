# Create and encryption and decryption mechanism
#import random
alphabets = """abcdefghijklmnopqrstuvwxyz@1234567890!#$%^&*()_+=\|}]{["':;?/><,"""
#random_numbers = random.sample(range(len(alphabets)),len(alphabets))
#temp_map = {}
#c = 0
#for num in random_numbers:
#    temp_map[alphabets[c]] = alphabets[num]
#    c+= 1

#reverse_temp_map = {}
#for key in temp_map:
#    reverse_temp_map[temp_map[key]] = key


perm_map = {'a': '{', 'b': 'u', 'c': '!', 'd': 'g', 'e': 'p', 'f': '*', 'g': '[', 'h': '1', 'i': 'e', 'j': 't', 'k': '<', 'l': 'v', 'm': '>', 'n': '\\', 'o': 'f', 'p': ']', 'q': '^', 'r': '|', 's': 'j', 't': '9', 'u': ':', 'v': '=', 'w': '6', 'x': 'd', 'y': 'b', 'z': '7', '@': 'q', '1': 'a', '2': 'z', '3': 'k', '4': 'm', '5': ';', '6': 'h', '7': '?', '8': '3', '9': '0', '0': ',', '!': '8', '$': 'o', '%': 'x', '^': 's', '&': '5', '*': '%', '(': '}', '_': '/', '+': 'w', '=': 'y', '\\': '_', '|': '+', '}': 'r', ']': '@', '{': 'l', '[': 'n', ':': 'c', ';': '(', '?': 'i', '/': '2', '>': '4', '<': '$', ',': '&'}
reverse_perm_map = {'{': 'a', 'u': 'b', '!': 'c', 'g': 'd', 'p': 'e', '*': 'f', '[': 'g', '1': 'h', 'e': 'i', 't': 'j', '<': 'k', 'v': 'l', '>': 'm', '\\': 'n', 'f': 'o', ']': 'p', '^': 'q', '|': 'r', 'j': 's', '9': 't', ':': 'u', '=': 'v', '6': 'w', 'd': 'x', 'b': 'y', '7': 'z', 'q': '@', 'a': '1', 'z': '2', 'k': '3', 'm': '4', ';': '5', 'h': '6', '?': '7', '3': '8', '0': '9', ',': '0', '8': '!', 'o': '$', 'x': '%', 's': '^', '5': '&', '%': '*', '}': '(', '/': '_', 'w': '+', 'y': '=', '_': '\\', '+': '|', 'r': '}', '@': ']', 'l': '{', 'n': '[', 'c': ':', '(': ';', 'i': '?', '2': '/', '4': '>', '$': '<', '&': ','}

def encrypt(password):
    encrypted_password = ""
    for letter in password:
        encrypted_password = encrypted_password + perm_map[letter]
    return encrypted_password



def decrypt(password):
    decrypted_password = ""
    for letter in password:
        decrypted_password = decrypted_password + reverse_perm_map[letter]
    return decrypted_password

#Retrieving encrypted data
while True:
    try:
        old_stored_passwords_file = open("punames.txt", "r")
        data = old_stored_passwords_file.readlines()
    except:
        create_a_new_password_file = open("punames.txt", "w")
        create_a_new_password_file.write("Username, Password, Sitename")
        create_a_new_password_file.close()
        old_stored_passwords_file = open("punames.txt", "r")
        data = old_stored_passwords_file.readlines()


    old_usernames = []
    old_passwords = []
    old_sitename = []
    for items in data:
        separated_items = items.split(",")
        old_usernames = old_usernames + [separated_items[0]]
        old_passwords = old_passwords + [separated_items[1]]
        old_sitename = old_sitename + [separated_items[2].strip()]
    old_stored_passwords_file.close()
# Ask whether to add or retrieve data

    what_to_do = input(
        "If you want to add a new password type 'y'.\nIf you want to retrieve and old password type 'n'.\n Else type'exit': ")

    if what_to_do == "y" or what_to_do == "n":
        if what_to_do == "n":
            # Input the site whose password you want
            try:
                site_to_search = input("Please Enter the site to retrieve the password: ")
                print(decrypt(old_passwords[old_sitename.index(site_to_search)]))
                continue
            except:
                print("Could not find the site you mentioned.")
                continue
        else:
            new_username = input("Enter a username: ")
            new_password = input("Enter a password: ")
            site_name = input("Website: ")
            char_in_list = True
            for x in new_password + new_username + site_name:
                #print(x,new_password+new_username+site_name)
                if x not in alphabets:
                    print("""Can't use values other than""" + alphabets)
                    char_in_list = False
                    break
            if not char_in_list:
                print("This is executed")
                continue

            if site_name in old_sitename:
                print("One account already exists for this site. you are creating another one")
                if new_username in old_usernames:
                    print("error. This username already exists for this site")
                # Write the data to a file
                else:

                    new_puname = open("punames.txt", "w")
                    for x in range(len(old_usernames)):
                        new_puname.write("{},{},{}\n".format(old_usernames[x], old_passwords[x], old_sitename[x]))
                    new_puname.write("{},{},{}".format(encrypt(new_username), encrypt(new_password), encrypt(site_name)))
                    new_puname.close()

            # Check if there is no comma
            elif "," in new_password or "," in new_username or "," in site_name:
                print("Can't use a comma. sorry.")


            # write the username and password to a file
            else:

                new_puname = open("punames.txt", "w")
                for x in range(len(old_usernames)):
                    new_puname.write("{},{},{}\n".format(old_usernames[x], old_passwords[x], old_sitename[x]))
                new_puname.write("{},{},{}".format(encrypt(new_username), encrypt(new_password), site_name))
                new_puname.close()
        continue
    elif what_to_do == "exit":
        break
    else:
        print("Please enter 'y' or 'n' or 'exit' and nothing else.")
        continue