# 1. Xóa phần tử trùng lặp nhưng giữ nguyên thứ tự
# Viết một hàm nhận vào một danh sách và trả về danh sách mới với các phần tử trùng lặp bị loại bỏ nhưng vẫn giữ nguyên thứ tự xuất hiện đầu tiên.
# Ví dụ
# python
# Sao chépChỉnh sửa
# Input: [1, 2, 3, 1, 2, 4, 5, 6, 4]
# Output: [1, 2, 3, 4, 5, 6]
mylist=[1,2,3,1,2,4,5]
myset= list(set(mylist))
print(myset)

mylist=[1,2,3,1,2,4,5]
res=[]
for item in mylist:
    if not item in res:
        res.append(item)
print(res)




