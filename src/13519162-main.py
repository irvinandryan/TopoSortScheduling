'''
Irvin Andryan P. (13519162)
IF 2211 K-03
Tugas Kecil 2 : Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer)
'''
from importlib import import_module
openFile = import_module("13519162-openFile")
topoSort = import_module("13519162-topoSort")
printMatkul = import_module("13519162-printMatkul")

'''
Main Program
'''
programRun = True #selama true program akan berjalan terus
while (programRun):
    namaFile = str(input("Masukkan nama file : ")) #nama file input
    listMataKuliah = openFile.openFile(namaFile) #membuka file dan memasukkan isinya ke listMataKuliah
    listUrutanMatkul = topoSort.getUrutanMatkul(listMataKuliah) #mendapatkan urutan matkul, dan disimpan di listUrutanMatkul
    printMatkul.printUrutanMatkul(listUrutanMatkul) #print urutan matkul ke layar
    print('')
    print("Apakah ingin memasukkan file baru?")
    fileBaru = str(input("Masukkan pilihan [Y / N] : "))
    while(fileBaru != 'N' and fileBaru != 'n' and fileBaru != 'Y' and fileBaru != 'y'):
        print("Masukkan salah!")
        fileBaru = str(input("Masukkan pilihan [Y / N] : "))
        
    if (fileBaru == 'N' or fileBaru == 'n'):
        programRun = False #program selesai
    else:
        continue #program terus berjalan