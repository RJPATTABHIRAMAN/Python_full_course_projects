import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

char_list = list(chars)
key = char_list.copy()
random.shuffle(key)
# print(key)
# print(char_list)
msg = input("Enter you massage :")
Encr = ""
for m in msg:
    index = char_list.index(m)
    Encr+=key[index]
print(f"You original value {msg} ")
print(f"Your encripted value {Encr}")

