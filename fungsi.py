import datetime 
import random
import tkinter
from tkinter import *
from tkinter.messagebox import showinfo
v=Tk()
bk="Black"
fr="#00FFDD"

v.title("Sapa ku")
v.geometry("300x300")
v.resizable(width=False, height=False)
v.geometry

a=["Baik","Petaka","Kurang baik","Sangat baik","Stabil","berhati hati"]

def sapa (nama, kelas, absen):
    
    """Sapa ku """
    showinfo("Sapa ku", "Nama saya "+nama+"\nKelas saya "+kelas+"\nAbsen saya "+absen+"\n"+random.choice(a))
    print("Hallo :"+nama)
    print("Dari Kelas :"+kelas)
    print("Degan Absen ke :"+absen)
    print("Masuk pada, "+str(datetime.date.today()))
    print("Keberuntunga mu sedang "+random.choice(a))
    
isi1= Text(v, width=30, height=1)
isi1.insert(END, "Nama :")
isi1.grid(row=0, column=0)
isi2=Text(v, width=30, height=1)
isi2.insert(END, "Kelas :")
isi2.grid(row=1, column=0)

isi3=Text(v, width=30, height=1)
isi3.insert(END, "Absen :")
isi3.grid(row=2, column=0)
Button(v, text="Sapa", command=lambda:sapa(nama=isi1.get("1.0",END),kelas=isi2.get("1.0",END),absen=isi3.get("1.0",END))).grid(row=3, column=0)
nama = input("Masukkan nama anda: ")
kelas = input("Masukkan kelas anda: ")
absen= input("Masukkan absen anda: ")
sapa(absen,nama,kelas)
print(sapa.__doc__)
v.mainloop()


