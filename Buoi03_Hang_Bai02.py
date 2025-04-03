lst = []
n = int(input("Nhap so luong phan tu muon them vao danh sach: "))
for i in range(n):
    j = int(input("Nhap gia tri cua danh sach: "))
    lst.append(j)
print(f"Danh sach da nhap vao la: {lst}")
def Bai02(lst):
    if len(lst) < 2:
        print("Khong the tinh tong")
        return

    lst.sort(reverse=True)
    a = lst[0] + lst[1]
    print(f"Tong hai so lon nhat la: {a}")

Bai02(lst)