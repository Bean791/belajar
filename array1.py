# panggil berdasakan index
# var=[34,12,56]
# print(var[1])
hasil=[
    "Suram",
    "Musibah",
    "Baik",
    "Cukup Beruntung",
    "Keberuntungan yang tertunda",
    "Masalah Besar",
    "Sangat Beruntung",
    "Tenang",
    "Masalah Baru",
    "Kedamaian"
]
print("Selamat Datang Di No keberuntungan anda")
nilai=int(input("Masukan No Anda! (antara 1-10)"))
if nilai == 1:
    H=hasil[0]
    print("Keberuntungan Anda Hari ini adalah",H)
elif nilai==2:
    H=hasil[1]
    print("Keberuntungan Anda Hari ini adalah",H)
elif nilai== 3:
    H=hasil[2]
    print("Keberuntungan Anda Hari ini adalah",H)
elif nilai==4:
    H=hasil[3]
    print("Keberuntungan Anda Hari ini adalah",H)
elif nilai==5:
    H=hasil[4]
    print("Keberuntungan Anda Hari ini adalah",H)
elif nilai==6:
    H=hasil[5]
    print("Keberuntungan Anda Hari ini adalah",H)
elif nilai==7:
    H=hasil[6]
    print("Keberuntungan Anda Hari ini adalah",H)
elif nilai==8:
    H=hasil[7]
    print("Keberuntungan Anda Hari ini adalah",H)
elif nilai==9:
    H=hasil[8]
    print("Keberuntungan Anda Hari ini adalah",H)
elif nilai==10:
    H=hasil[9]
    print("Keberuntungan Anda Hari ini adalah",H)
else:
    print("Tolong Masukan antara 1-10 Trima kasih!")    
    
