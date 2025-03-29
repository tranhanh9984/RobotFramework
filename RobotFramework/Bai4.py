n = int(input("Nhập năm : "))
if (n % 400 ==0)or((n % 4==0)and(n %100 !=0)):
    print("Năm Nhuận")
else:
    print("Không phải năm nhuận")
