#c1
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
ket_qua = a ** b
print("Kết quả của phép tính a^b là:", ket_qua)
#2
import math
ban_kinh = float(input("Nhập bán kính của hình tròn: "))
chu_vi = 2 * math.pi * ban_kinh
dien_tich = math.pi * (ban_kinh ** 2)
print("Chu vi của hình tròn là:", chu_vi)
print("Diện tích của hình tròn là:", dien_tich)
#c3
tu_so_a = float(input("Nhập tử số a: "))
mau_so_b = float(input("Nhập mẫu số b: "))
ket_qua = tu_so_a / mau_so_b
print("Kết quả : ", ket_qua)
#c4
do_c = float(input("Nhập giá trị độ C: "))
do_f = (do_c * 1.8) + 32
print("Giá trị sau khi chuyển sang độ F là:", do_f)
#c5
so_nguyen = int(input("Nhập vào một số nguyên: "))
sang_string = str(so_nguyen)
print("Chuyển sang kiểu string:", sang_string)
sang_float = float(so_nguyen)
print("Chuyển sang kiểu float:", sang_float)
sang_boolean = bool(so_nguyen)
print("Chuyển sang kiểu boolean:", sang_boolean)
#c6
so_ba_chu_so = input("Nhập vào số nguyên 3 chữ số: ")
so = int(so_ba_chu_so)
hang_tram = so // 100
hang_chuc = (so % 100) // 10
hang_don_vi = so % 10
tong_chu_so = hang_tram + hang_chuc + hang_don_vi
print("Tổng các chữ số của", so_ba_chu_so, "là:", tong_chu_so)
#c7
a = input("Nhập giá trị cho biến a: ")
b = input("Nhập giá trị cho biến b: ")
a, b = b, a
print("Giá trị của a và b sau khi hoán đổi : ","a = ",a,"b =",b)
