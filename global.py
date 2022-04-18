import random
total = 0
# Variabel global
# Definisi fungsi
def sum( arg1, arg2 ):
    """Menambahkan variabel dan mengembalikan hasilnya."""
    total = arg1 + arg2;
    # total di sini adalah variabel lokal
    print ("Di dalam fungsi nilai total : ", total)
    return total
def asal():
    a=sum(arg1=random.randint(1,1000), arg2=random.randint(1,100))
    if a > 500:
        print("Hasil lebih dari 500")
    elif a < 500:
        print("Hasil kurang dari 500")
    elif a == 500:
        print("Hasil sama dengan 500")
    
# Pemanggilan fungsi sum
asal()
print ("Di luar fungsi, nilai total : ", total )