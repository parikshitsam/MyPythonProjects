# Create and encryption and decryption mechanism
import random
alphabets = "abcdefghijklmnopqrstuvwxyz"
random_numbers_between_0_26 = random.sample(range(len(alphabets)),len(alphabets))
temp_map = {}
c = 0
for num in random_numbers_between_0_26:
    temp_map[alphabets[c]] = alphabets[num]
    c+= 1

reverse_temp_map = {}
for key in temp_map:
    reverse_temp_map[temp_map[key]] = key

perm_map = {'a': 'l', 'b': 'f', 'c': 'p', 'd': 'z', 'e': 'd', 'f': 't', 'g': 'j', 'h': 'w', 'i': 'b', 'j': 'v', 'k': 's', 'l': 'a', 'm': 'i', 'n': 'q', 'o': 'y', 'p': 'c', 'q': 'g', 'r': 'u', 's': 'e', 't': 'r', 'u': 'h', 'v': 'm', 'w': 'x', 'x': 'k', 'y': 'o', 'z': 'n'}
reverse_perm_map = {'l': 'a', 'f': 'b', 'p': 'c', 'z': 'd', 'd': 'e', 't': 'f', 'j': 'g', 'w': 'h', 'b': 'i', 'v': 'j', 's': 'k', 'a': 'l', 'i': 'm', 'q': 'n', 'y': 'o', 'c': 'p', 'g': 'q', 'u': 'r', 'e': 's', 'r': 't', 'h': 'u', 'm': 'v', 'x': 'w', 'k': 'x', 'o': 'y', 'n': 'z'}


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

# Ask whether to add or retrieve data

what_to_do = input("If you want to add a new password type 'y'. If you want to retrieve and old password type 'n': ")

if what_to_do == "y" or what_to_do == "n":
    if what_to_do == "n":
        # Input the site whose password you want
        try:
            site_to_search = input("Please Enter the site to retrieve the password: ")
            print(decrypt(old_passwords[old_sitename.index(site_to_search)]))
        except:
            print("Could not find the site you mentioned.")
    else:
        new_username = input("Enter a username: ")
        new_password = input("Enter a password: ")
        site_name = input("Website: ")
        if site_name in old_sitename:
            print("One account already exists for this site. you are creating another one")
            if new_username in old_usernames:
                print("error. This username already exists for this site")
            # Write the data to a file
            else:
                old_stored_passwords_file.close()
                new_puname = open("punames.txt", "w")
                for x in range(len(old_usernames)):
                    new_puname.write("{},{},{}\n".format(old_usernames[x], old_passwords[x], old_sitename[x]))
                new_puname.write("{},{},{}".format(encrypt(new_username), encrypt(new_password), encrypt(site_name)))

        # Check if there is no comma
        elif "," in new_password or "," in new_username or "," in site_name:
            print("Can't use a comma. sorry.")


        # write the username and password to a file
        else:
            old_stored_passwords_file.close()
            new_puname = open("punames.txt", "w")
            for x in range(len(old_usernames)):
                new_puname.write("{},{},{}\n".format(old_usernames[x], old_passwords[x], old_sitename[x]))
            new_puname.write("{},{},{}".format(encrypt(new_username), encrypt(new_password), site_name))
else:
    print("Please enter 'y' or 'n' and nothing else.")

