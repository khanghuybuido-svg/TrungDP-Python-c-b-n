#c1
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

if a % b == 0:
    print("Số a chia hết cho số b")
else:
    print("Số a không chia hết cho số b")
#c2
tuoi_hs= int(input("Nhập tuổi học sinh: "))

if tuoi_hs >= 6:
    print("Học sinh đủ tuổi vào học lớp 1")
else:
    print("Học sinh chưa đủ tuổi vào học lớp 1")
#c3
s1 = int(input("Nhập số thứ nhất: "))
s2 = int(input("Nhập số thứ hai: "))
s3 = int(input("Nhập số thứ ba: "))
if s1 > s2:
    if s1 > s3:
        print("Số thứ nhất lớn nhất")
    else :
        print("Số thứ ba lớn nhất")
else:
    if s2 > s3:
        print("Số thứ hai lớn nhất")
    else:
        print("Số thứ ba lớn nhất")
#c4
khang = float(input("Nhập chiều cao của Khang: "))
kha = float(input("Nhập chiều cao của Kha: "))
if khang > kha:
    print("Bạn Khang cao hơn Kha")
elif kha > khang:
    print("Bạn Kha cao hơn Khang")
else:
    print("Hai bạn cao bằng nhau")
#c5
diem_hs = float(input("Nhập điểm thi của học sinh: "))
if diem_hs >= 9:
    print("Xếp loại A")
elif diem_hs >= 7:
    print("Xếp loại B")
elif diem_hs >= 5:
    print("Xếp loại C")
else:
    print("Xếp loại D")
#c6
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))
bmi = weight / (height ** 2)
print("Chỉ số BMI của bạn là:",bmi)
if bmi < 18.5:
    print("Phân loại: Underweight")
elif 18.5 <= bmi < 25.0:
    print("Phân loại: Normal")
elif 25.0 <= bmi < 30.0:
    print("Phân loại: Overweight")
else:
    print("Phân loại: Obese")
#c7
nam = int(input("Nhập một năm bất kỳ: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0 and nam % 100 ==0):
    print(f"Năm {nam} là năm nhuận")
else:
    print(f"Năm {nam} không phải là năm nhuận")