lst = []
n = int(input("Nhap so luong phan tu muon them vao danh sach: "))
for i in range(n):
    j = int(input("Nhap gia tri cua danh sach: "))
    lst.append(j)
print(f"Danh sach da nhap vao la: {lst}")
k = int(input("Nhap so k:"))
def Bai03(lst, k):
    if len(lst) == 0:
        return []
    k = k % len(lst)
    return lst[k:] + lst[:k]

result = Bai03(lst, k)
print("Day moi la: ", result)