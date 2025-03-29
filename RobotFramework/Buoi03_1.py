n = int(input("Nhap so nguyen N: "))
if n < 10 and n > 0:
    print(f"{n} khong co so dao nguoc")
elif n < 0:
    a = n * -1
    n_nguoc = int(str(a)[::-1])
    print(f"-{n_nguoc}")
else:
    n_nguoc = int(str(n)[::-1])
    # str(n): chuyển từ dạng số int sang chuỗi str
    # [::-1] ~ [star:stop:step]
    # => không có start và stop (nếu không có thì sẽ mặc định start là đầu chuỗi, start là cuối chuỗi)
    # step là -1 nên chuỗi sẽ đảo ngược lại
    print(n_nguoc)

# chưa check được trường hợp số âm