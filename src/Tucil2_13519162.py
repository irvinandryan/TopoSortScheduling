'''
Irvin Andryan P. (13519162)
IF 2211 K-03
Tugas Kecil 2 : Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer)
'''
import os
'''
Membuka file input dan memasukkannya ke dalam list 2 dimensi bernama listOfContents
fungsi ini juga sudah menghilangkan tanda titik dan koma yang tidak akan terpakai
hasilnya adalah listOfContents[i][j]
contoh : listOfContents[1][0] = "IF1111"
listOfContents[1][1], listOfContents[1][2], ... adalah mata kuliah prasyarat dari mata kuliah "IF1111"
'''
def openFile(namaFile):
    os.chdir("test")
    with open(namaFile) as inputFile:
        listOfContents = [line.split() for line in inputFile]
    #membuka file dan hasilnya dimasukkan ke dalam list 2 dimensi bernama listOfContents
    #hasil yang dimasukkan sudah terbagi menjadi per baris, contoh : [[baris1], [baris2], [baris3]]

    for i in range(len(listOfContents)): 
        for j in range(len(listOfContents[i])):
            listOfContents[i][j] = listOfContents[i][j].strip(",.")
            #menghapus tanda koma dan titik dari elemen-elemen listOfContents
    os.chdir("..") #mengembalikan working directory ke awal
    return listOfContents


'''
Fungsi untuk menyelesaikan persoalan urutan mata kuliah dengan topological sort,
fungsi ini memiliki parameter bertipe list yang berisi nama mata kuliah dan nama mata kuliah prasyaratnya
fungsi ini memiliki return value berupa list 2 dimensi yang berisi urutan mata kuliah tiap semesternya, 
contoh return : [[a,b,c], [d,e,f], [g,h,i]] maka a,b,c adalah mata kuliah
yang bisa diambil di semester 1; d,e,f di semester 2; dan g,h,i di semester 3
'''
def getUrutanMatkul(listMataKuliah):
    done = False
    #inisiasi boolean "done" yang akan digunakan sebagai tanda selesainya proses

    urutanMatkul = []
    #inisiasi list "urutanMatkul" yang akan menjadi list 2 dimensi berisi mata kuliah terurut per semester
    #list ini adalah nilai yang akan di-return oleh fungsi ini

    while (not done):
        currentSemester = []
        #inisiasi list "currentSemester" yang akan diisi mata kuliah yang diambil di semester
        #yang sedang diproses, nantinya list ini di-append ke list urutanMatkul

        for i in range(len(listMataKuliah)):
            if (len(listMataKuliah[i]) == 1):
            #jika panjang listMataKuliah[i] = 1, maka hanya ada satu elemen
            #pada listMataKuliah[i], yang artinya mata kuliah pada listMataKuliah[i][0] adalah
            #mata kuliah yang prasyaratnya sudah terpenuhi atau tidak punya prasyarat
                currentSemester.append(listMataKuliah[i][0])
                #tambahkan mata kuliah yang sudah tidak ada prasyaratnya ke list currentSemester

        for i in range(len(currentSemester)):
            for j in range(len(listMataKuliah)):
                if (currentSemester[i] in listMataKuliah[j]):
                    listMataKuliah[j].remove(currentSemester[i])
                    #menghapus mata kuliah yang diambil di semester ini dari listMataKuliah.
                    #dihapus baik sebagai mata kuliah itu sendiri maupun sebagai prasyarat mata kuliah lain.
        
        urutanMatkul.append(currentSemester)
        #menambahkan mata kuliah pada listCurrentSemester ke list urutanMatkul
        matkulHabis = True
        #boolean untuk mengecek apakah sudah tidak ada mata kuliah yang belum diambil di listMatakuliah
        for k in range(len(listMataKuliah)):
            if (len(listMataKuliah[k]) != 0):
                matkulHabis = False  #jika ada yang panjangnya > 0 masih ada matkul yang belum diambil
        
        if (matkulHabis == True): #jika sudah tidak ada matkul yang belum diambil, selesai
            done = True
    return urutanMatkul


'''
Prosedur untuk print urutan mata kuliah yang diambil ke layar. contoh hasil :
Semester 1 : C1.
Semester 2 : C3, C5.
Semester 3 : C4.
Semester 4 : C2.
'''
def printUrutanMatkul(listUrutanMatkul):
    for i in range(len(listUrutanMatkul)):
        print("Semester", i+1, ": ", end = '')
        for j in range(len(listUrutanMatkul[i])):
            if (j < len(listUrutanMatkul[i]) - 1):
                print(listUrutanMatkul[i][j], end = ', ')
            else:
                print(listUrutanMatkul[i][j], end = '.')
        print('')


'''
Main Program
'''
programRun = True #selama true, maka program akan berjalan terus
while (programRun):
    namaFile = str(input("Masukkan nama file : ")) #nama file input
    listMataKuliah = openFile(namaFile) #membuka file dan memasukkan isinya ke listMataKuliah
    listUrutanMatkul = getUrutanMatkul(listMataKuliah) #mendapatkan urutan matkul dan memasukkan hasilnya ke listUrutanMatkul
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