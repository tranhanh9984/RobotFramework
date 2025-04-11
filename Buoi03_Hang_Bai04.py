lst = []
n = int(input("Nhap so luong phan tu muon them vao danh sach: "))
for i in range(n):
    j = int(input("Nhap gia tri cua danh sach: "))
    lst.append(j)

count = {}
# count này sẽ là tập hợp dang dictionary theo hướng giá trị = key, số lần xuất hiện =  value
# mình cần dict count này để đếm số lượng xuất hiện của từng số trong dãy
for a in lst:
    if a in count: # Nếu số đó đã có phần count, tức là đã được đếm => tăng thêm 1 lần
        count[a] += 1
    else:
        count[a] = 1 # Nếu chưa có trong count thì gán bằng 1

max_appear = max(count.values())
lst2 = []
for b in count:
    if count[b] == max_appear:
        lst2.append(b)
c = max(lst2)
print("So xuat hien nhieu nhat la:", c)
