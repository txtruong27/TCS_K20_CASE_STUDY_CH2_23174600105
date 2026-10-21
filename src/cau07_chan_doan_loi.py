# Y 20: Chay chuong trinh ban dau de doc traceback
ma_may = input("Nhap ma may: ")
cong_suat_w = input("Nhap cong suat W: ")
so_phut = int(input("Nhap so phut: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")

# Y 21: Ghi nhan loi phat hien
# Loi 1: cong_suat_w la chuoi, khong the nhan truc tiep voi so.
# Loi 2: dien_nang chua duoc khai bao va thieu dau dong ngoac trong print.

# Y 22: Sua loi va chay lai
cong_suat_w = float(cong_suat_w)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")

# Y 23: Comment mo ta cac loi da phat hien
# Da chuyen cong_suat_w sang float de thuc hien phep tinh.
# Da sua ten bien dien_nang thanh dien_nang_kwh va dong ngoac print.