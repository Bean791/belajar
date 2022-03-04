def a(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j]>x[j+1]:
                temp = x[j]
                x[j]=x[j+1]
                x[j+1]=temp
def b(v):
    for w in range(len(v)-1,9,+1):
        for q in range(w):
            if v[q]>v[q+1]:
                temp1 = v[q]
                v[q]=v[q+1]
                v[q+1]=temp1
angka = [543,25,534,345,12,23,12,1234,432,7435]
angka1 = [543,25,534,345,12,23,12,1234,432,7435]
print("Hallo Selamat datang di urut mengurut angka dengan algoritma Bubble Sort")
print("Silakan kirim \n1. untuk sebelum di urut \n2. untuk setelah di urut dari beasr ke kecil \n3. untuk setelah di urut dari kecil ke besar \n4. untuk keluar")
i=0
while i < 3:
    pilih=int(input("masukan pilihan anda "))
    if pilih==1:
        print("data sebelum di ururtkan")
        print(angka)
    elif pilih==2:
        print("data setelah di urutkan dengan metode algoritma bubble sort kecil ke besar")
        a(angka)
        print(angka)
    elif pilih==3:
        print("data setelah di urutkan dengan metode algoritma bubble sort besar ke kecil")
        b(angka1)
        print(angka1)
    else:
        print("Terimakasih telah menggunakan program ini")
        break
    i+=1