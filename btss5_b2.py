#c1
luong = float(input("Nhập lương nhân viên (triệu): "))
if luong >= 15:
    thue = luong * 0.3
elif luong >= 7:
    thue = luong * 0.2
else:
    thue = luong * 0.1
luong_rong = luong - thue
print("Lương ròng mà nhân viên nhận được (triệu):",luong_rong)
print("Thuế mà nhân viên đó phải nhận:", thue)
#c2
import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0 and b == 0:
    print("Phương trình vô nghiệm")
elif a == 0:
    x = -c / b
    print("Phương trình có một nghiệm là: x=",x)
else:
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép: x=",x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có hai nghiệm: x1 =",x1 ," x2 =", x2)
#c3
doanh_so = float(input("Nhập tổng doanh số bán hàng (triệu đồng): "))
if doanh_so <= 100:
    hoa_hong = doanh_so * 0.05
elif doanh_so <= 300:
    hoa_hong = doanh_so * 0.1
else:
    hoa_hong = doanh_so * 0.2
print("Số tiền hoa hồng nhận được là (triệu đồng): ", hoa_hong)
#c4
so_phut = float(input("Nhập tổng số phút gọi: "))
phi_thue_bao = 25000
cuoc_goi = 0
if so_phut <= 50:
    cuoc_goi = so_phut * 600
elif so_phut <= 200:
    cuoc_goi = (50 * 600) + (so_phut - 50) * 400
else:
    cuoc_goi = (50 * 600) + (150 * 400) + (so_phut - 200) * 200
cuoc_dt = phi_thue_bao + cuoc_goi
print("Tổng cước điện thoại phải trả là (đồng): ", cuoc_dt)