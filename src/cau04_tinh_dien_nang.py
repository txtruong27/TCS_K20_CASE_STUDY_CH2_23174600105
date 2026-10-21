# Y 13: Tinh dien nang tieu thu va chi phi dien
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# Y 14: In gia tri va kieu du lieu cua hai ket qua
print("Dien nang:", dien_nang_kwh)
print(type(dien_nang_kwh))

print("Chi phi:", chi_phi)
print(type(chi_phi))

# Y 15: Du doan ket qua truoc khi chay
# Dien nang: 0.375 kWh
# Chi phi: 1125.0 VND

# Y 16: Thay so_phut bang 60 va tinh lai
so_phut = 60