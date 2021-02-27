'''
Irvin Andryan P. (13519162)
IF 2211 K-03
Tugas Kecil 2 : Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer)
'''

from openFile import openFile
from topoSort import getUrutanMatkul
from printMatkul import printUrutanMatkul

'''
Main Program
'''
programRun = True #selama maka program akan berjalan terus
while (programRun):
    namaFile = str(input("Masukkan nama file : ")) #nama file input
    listMataKuliah = openFile(namaFile) #membuka file dan memasukkan isinya ke listMataKuliah
    listUrutanMatkul = getUrutanMatkul(listMataKuliah) #mendapatkan urutan matkul, disimpan dan di listUrutanMatkul
    printUrutanMatkul(listUrutanMatkul) #print urutan matkul ke layar
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