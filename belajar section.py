import random

def ab(a):
    for pos_tujuan in range(len(a)-1,0,-1):
        pos_asal = pos_tujuan
        for i in range(pos_tujuan+1):
            if a[pos_asal] > a[i]:
                pos_asal = i
        a[pos_tujuan], a[pos_asal] = a[pos_asal], a[pos_tujuan]
data=[random.randint(0,100) for i in range(10)]
print("Data sebelum di urutkan",data)
ab(data)
print("Data setelah di urutkan",data)


# def data(a):
#     for pos_tujuan in range(len(a)-1,0,-1):
#         pos_asal = pos_tujuan
#         print("pos asal",pos_asal)
#         print("pos tujuan",pos_tujuan)
#         print("pos asal akan jadi pos tujuan",pos_asal)
#         for i in range(pos_tujuan+1):
#             print("keberadaan saat ini",i)
#             if a[pos_asal] > a[i]:
#                 pos_asal = i
#                 print("pos asal di dalam",pos_asal)
#         a[pos_tujuan], a[pos_asal] = a[pos_asal], a[pos_tujuan]

# angka = [132.634,123,6,132,43463,23,12,1234,432,7435]
# print("data sebelum di urutkan",angka)
# data(angka)

# print(angka)

# def pilih(x):
#     for pos_tujuan in range(len(x)-1,0,1):
#         pos_max=pos_tujuan
#         print("pos_max" ,pos_max)
#         print("pos_tujuan" ,pos_tujuan)
#         print("mencari nilai terkecil \n")

#         for j in range (1,pos_tujuan+1):
#             print("variabel j" ,j)
#             print("data x [j]" , x[j])

#             if x[pos_max] >x[j]:
#                 pos_max =j
#                 print("pos max in if",pos_max)
#             print("akhir mencari nilai terkecil")
#             x[pos_max], x[pos_tujuan],= x[pos_tujuan], x[pos_max]

