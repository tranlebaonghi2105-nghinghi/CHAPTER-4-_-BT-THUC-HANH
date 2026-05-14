class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong


# Tạo đối tượng thứ nhất
hcn1 = HinhChuNhat(10, 5)

# Tạo đối tượng thứ hai
hcn2 = HinhChuNhat(7, 3)

# In thông tin hình chữ nhật 1
print("Hình chữ nhật 1")
print("Chiều dài:", hcn1.chieu_dai)
print("Chiều rộng:", hcn1.chieu_rong)
print("Chu vi:", hcn1.tinh_chu_vi())
print("Diện tích:", hcn1.tinh_dien_tich())

print()

# In thông tin hình chữ nhật 2
print("Hình chữ nhật 2")
print("Chiều dài:", hcn2.chieu_dai)
print("Chiều rộng:", hcn2.chieu_rong)
print("Chu vi:", hcn2.tinh_chu_vi())
print("Diện tích:", hcn2.tinh_dien_tich())