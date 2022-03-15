import random
def ai(par):
    print("algoritma insertion sort")
    for i in range(1,len(par)):
        a=par[i]
        print("nilai a ",a)
        b=i-1
        print("nilai b ",b," nilai a",a, "nilai par[b]",par[b])
        while b>=0 and a<par[b]:
            print("par[b+1]",par[b+1])
            par[b+1]=par[b]
            b-=1
            print("nilai j-=1",b)
        par[b+1]=a
        print("hasil: ",par)
    return par
        
        
isi=[random.randint(0,100) for i in range(10)]

print("data sebelum di urutkan",isi)

print("data setelah di urutkan", ai(isi))


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         print("key",key)
#         j = i-1
#         print("nilai j :", j, "nilai key :", key,"< nilai arr[j] :", arr[j])
#         while j >=0 and key < arr[j] :
#             print("nilai arr[j+1]", arr[j+1])
#             arr[j+1] = arr[j]
#             j -= 1
#             print("nilai j-=1", j)
#         arr[j+1] = key
#         print("data:", arr)
#     return arr

# angka = [44,55,22,33,66,1002,47,59]
# print ("data sebelum di urutkan",angka)

# print (" Data setelah di urutkan", insertion_sort(angka))
