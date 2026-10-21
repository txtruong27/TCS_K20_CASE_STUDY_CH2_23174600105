# Y 17: Nhap bon gia tri va in kieu du lieu ban dau
ma_may = input("Nhap ma may: ")
cong_suat_w = input("Nhap cong suat W: ")
so_phut = input("Nhap so phut su dung: ")
don_gia_kwh = input("Nhap don gia dien/kWh: ")

print(type(ma_may))
print(type(cong_suat_w))
print(type(so_phut))
print(type(don_gia_kwh))

# Y 18: Chuyen doi kieu du lieu
cong_suat_w = float(cong_suat_w)
so_phut = int(so_phut)
don_gia_kwh = float(don_gia_kwh)

# Y 19: Tinh dien nang va chi phi
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Dien nang:", dien_nang_kwh)
print("Chi phi:", chi_phi)