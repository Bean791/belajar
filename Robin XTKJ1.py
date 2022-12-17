# import datetime
# # Variabel global untuk menyimpan data Buku
# buku = []

# # fungsi untuk menampilkan semua data
# def show_data():
#     print("Show Data")
#     if len(buku) <= 0:
#         print ("BELUM ADA DATA")
#     else:
#         for indeks in range(len(buku)):
#             print ("[%d] %s" % (indeks, buku[indeks]))
# nama="Robin XTKJ1"
# # fungsi untuk menambah data
# def insert_data():
#     buku_baru = input("Judul Buku: ")
#     buku.append(buku_baru + " " + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")+" "+ "Oleh "+nama)
# # fungsi untuk edit data
# def edit_data():
#     show_data()
#     indeks = input("Inputkan ID buku: ")
#     indeks=int(indeks)
#     if(indeks > len(buku)):
#         print ("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         buku[indeks] = judul_baru+" " + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")+" "+ "Oleh "+nama
# # fungsi untuk menhapus data
# def delete_data():
#     show_data()
#     indeks = input("Inputkan ID buku: ")
#     indeks=int(indeks)
#     if(indeks > len(buku)):
#         print ("ID salah")
#     else:
#         buku.remove(buku[indeks])
# # fungsi untuk menampilkan menu
# # def show_menu():
# #     print ("\n")
# #     print ("----------- MENU ----------")
# #     print ("[1] Show Data")
# #     print ("[2] Insert Data")
# #     print ("[3] Edit Data")
# #     print ("[4] Delete Data")
# #     print ("[5] Exit")
# #     menu = input("PILIH MENU> ")
# #     print ("\n")
# #     menu=int(menu)
# #     if menu == 1:
# #         show_data()
# #     elif menu == 2 :
# #         insert_data()
# #     elif menu == 3:
# #         edit_data()
# #     elif menu == 4:
# #         delete_data()
# #     elif menu == 5:
# #         exit()
# #     else:
# #         print ("Salah pilih!")
# a=True
# while a==True:
#     print ("\n")
#     print ("----------- MENU ----------")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")
#     menu=int(menu)
#     if menu == 1:
#         show_data()
#     elif menu == 2 :
#         insert_data()
#     elif menu == 3:
#         edit_data()
#     elif menu == 4:
#         delete_data()
#     elif menu == 5:
#         exit()
#     else:
#         print ("Salah pilih!")


# # if __name__ == "__main__":
# #     while(True):
# #         show_menu()
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)