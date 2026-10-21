tong_phut = 135
cong_suat_w = 250

# Y 9: Tinh so gio va so phut con lai
so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60

print("So gio tron ven:", so_gio)
print("So phut con lai:", so_phut_con_lai)

# Y 10: Kiem tra thoi gian su dung co lon hon 60 phut
su_dung_lau = tong_phut > 60
print("Su dung lau:", su_dung_lau)

# Y 11: Kiem tra du lieu hop le
du_lieu_hop_le = cong_suat_w > 0 and tong_phut > 0
print("Du lieu hop le:", du_lieu_hop_le)

# Y 12: Kiem tra thu tu thuc hien phep tinh
print(100 + 20 * 3)
print((100 + 20) * 3)