'''
Irvin Andryan P. (13519162)
IF 2211 K-03
Tugas Kecil 2 : Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer)
'''

import os

'''
Fungsi untuk membuka file input dan memasukkannya ke dalam list 2 dimensi bernama listOfContents
fungsi ini juga sudah menghilangkan tanda titik dan koma yang tidak akan terpakai
hasilnya adalah listOfContents[i][j]
contoh : listOfContents[1][0] = "IF1111"
listOfContents[1][1], listOfContents[1][2], ... adalah mata kuliah prasyarat dari mata kuliah "IF1111"
'''
def openFile(namaFile):
    os.chdir("..")
    os.chdir("test")
    with open(namaFile) as inputFile:
        listOfContents = [line.split() for line in inputFile]
    #membuka file dan hasilnya dimasukkan ke dalam list 2 dimensi bernama listOfContents
    #hasil yang dimasukkan sudah terbagi menjadi per baris, contoh : [[baris1], [baris2], [baris3]]

    for i in range(len(listOfContents)): 
        for j in range(len(listOfContents[i])):
            listOfContents[i][j] = listOfContents[i][j].strip(",.")
            #menghapus tanda koma dan titik.
    return listOfContents
