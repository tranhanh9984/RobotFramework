#Bài 8: Tìm số đảo ngược
name = "Bài tập 08"
print(name)
text = str(input("Xin mời nhập chuỗi: "))
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Số ban đầu là:", text)
print("Số đảo ngược là: ", reversed_text)