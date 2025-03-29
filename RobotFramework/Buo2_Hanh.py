# n = int(input("Nhập vào số N: "))
#
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end = ' ')
#     print("")
#
# from curses.ascii import isdigit
#
#xyz
# from _curses import *

# kiem tra no có daạng số không? ->
# kiemt ra nó cóchiri la ky tu không?

# text =int(input("Nhap vao 1 chuoi:"))
# reversed_text = ""
# isSub = False
# text = str(text)
# for char in text:
#    if "-" == char:
#         isSub = True
#         continue;
#     reversed_text = char + reversed_text
# if isSub == True:
#     reversed_text = "-" +reversed_text
# print(reversed_text)  # Output: "!eegnirtS olleH"
# print("Số đảo ngược là:", reversed_text)


text = int("-avc")
text = abs(text)
text =str(text)[::-1]
print(int(text)*-1)
