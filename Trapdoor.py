def alt_even_nums(nums):
    lst = []
    for num in range(nums):
        if num%2 == 0:
            lst.append(num)
    return lst

def alt_odd_nums(nums):
    lst = []
    for num in range(nums):
        if num%2 != 0:
            lst.append(num)
    return lst

def alt_char_of_str(password):
    lst = []
    if len(password)%2 == 0:
        even_nums = alt_even_nums(len(password))
        for num in even_nums:
            first_char = password[num]
            second_char = password[num+1]
            lst.append(first_char+second_char)
        return lst
    else:
        odd_nums = alt_odd_nums(len(password))
        for num in odd_nums:
            first_char = password[num-1]
            second_char = password[num]
            lst.append(first_char+second_char)
        lst.append(password[-1])
        return lst
#print(alt_char_of_str("abcdefghi"))



def encrypt2(password):
    alphabets_symbols = """abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()_+-={\}[]';/";:/?.>,<"""
    p = 7523
    q = 5843
    n = p*q
    e = 6029
    crypt = ""
    block_length_plaintext = 2
    block_length_crypttext = 15
    lst_char_pass = alt_char_of_str(password)
    crypt_nums = []
    crypt = ""

    for str in lst_char_pass:
        if len(str)==2:
            a = alphabets_symbols.index(str[0])
            b = alphabets_symbols.index(str[1])
            crypt_nums.append((len(alphabets_symbols)*a)+b)
        else:
            crypt_nums.append(alphabets_symbols.index(str))
    for num in crypt_nums:
        crypt = crypt + alphabets_symbols[((num**e)%n)%len(alphabets_symbols)]
    print(crypt_nums)
    return crypt

#def decrypt(encrypted_password):

p = 7523
q = 5843
#n = p*q
e = 6029
block_length_plaintext = 2
block_length_crypttext = 15
#print((66**block_length_plaintext)<n)
print(encrypt2("abcdefghi"))

def decrypt2(password):
    lst_nums = []
    for char in password:

