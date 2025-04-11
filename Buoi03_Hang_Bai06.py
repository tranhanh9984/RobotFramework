lst = []
n = int(input("Nhap so luong phan tu muon them vao danh sach: "))
for i in range(n):
    j = int(input("Nhap gia tri cua danh sach: "))
    lst.append(j)
print(f"Danh sach da nhap vao la: {lst}")

def Bai06(nums):
    n = len(nums) + 1 # vì thiếu 1 số nên độ dài dãy số ban đầu giảm đi 1
    tong1 = sum(range(1, n + 1)) # tổng các số từ 1 đến n
    tong2 = sum(nums) # tổng của dãy nhập vào
    a = tong1 - tong2
    return a
print("So bi thieu la: ",Bai06(lst))
