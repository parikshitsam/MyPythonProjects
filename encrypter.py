import random
alphabets_numbers_symbols = """abcdefghijklmnopqrstuvwxyz@1234567890!$%^&*(_+=\|}]{[:;?/><,"""
random_numbers = random.sample(range(len(alphabets_numbers_symbols)), len(alphabets_numbers_symbols))
temp_map = {}
c = 0
for num in random_numbers:
    temp_map[alphabets_numbers_symbols[c]] = alphabets_numbers_symbols[num]
    c+= 1

reverse_temp_map = {}
for key in temp_map:
    reverse_temp_map[temp_map[key]] = key
print((temp_map))
print((reverse_temp_map))
perm_map = {'a': '{', 'b': 'u', 'c': '!', 'd': 'g', 'e': 'p', 'f': '*', 'g': '[', 'h': '1', 'i': 'e', 'j': 't', 'k': '<', 'l': 'v', 'm': '>', 'n': '\\', 'o': 'f', 'p': ']', 'q': '^', 'r': '|', 's': 'j', 't': '9', 'u': ':', 'v': '=', 'w': '6', 'x': 'd', 'y': 'b', 'z': '7', '@': 'q', '1': 'a', '2': 'z', '3': 'k', '4': 'm', '5': ';', '6': 'h', '7': '?', '8': '3', '9': '0', '0': ',', '!': '8', '$': 'o', '%': 'x', '^': 's', '&': '5', '*': '%', '(': '}', '_': '/', '+': 'w', '=': 'y', '\\': '_', '|': '+', '}': 'r', ']': '@', '{': 'l', '[': 'n', ':': 'c', ';': '(', '?': 'i', '/': '2', '>': '4', '<': '$', ',': '&'}
reverse_perm_map = {'{': 'a', 'u': 'b', '!': 'c', 'g': 'd', 'p': 'e', '*': 'f', '[': 'g', '1': 'h', 'e': 'i', 't': 'j', '<': 'k', 'v': 'l', '>': 'm', '\\': 'n', 'f': 'o', ']': 'p', '^': 'q', '|': 'r', 'j': 's', '9': 't', ':': 'u', '=': 'v', '6': 'w', 'd': 'x', 'b': 'y', '7': 'z', 'q': '@', 'a': '1', 'z': '2', 'k': '3', 'm': '4', ';': '5', 'h': '6', '?': '7', '3': '8', '0': '9', ',': '0', '8': '!', 'o': '$', 'x': '%', 's': '^', '5': '&', '%': '*', '}': '(', '/': '_', 'w': '+', 'y': '=', '_': '\\', '+': '|', 'r': '}', '@': ']', 'l': '{', 'n': '[', 'c': ':', '(': ';', 'i': '?', '2': '/', '4': '>', '$': '<', '&': ','}