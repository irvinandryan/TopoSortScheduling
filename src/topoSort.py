'''
Irvin Andryan P. (13519162)
IF 2211 K-03
Tugas Kecil 2 : Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer)
'''

'''
Fungsi untuk menyelesaikan persoalan urutan mata kuliah dengan topological sort,
fungsi ini memiliki parameter bertipe list yang berisi nama mata kuliah dan nama mata kuliah prasyaratnya
fungsi ini memiliki return value berupa list 2 dimensi yang berisi urutan mata kuliah tiap semesternya, 
contoh return : [[a,b,c], [d,e,f], [g,h,i]] maka a,b,c adalah mata kuliah
yang bisa diambil di semester 1; d,e,f di semester 2; dan g,h,i di semester 3
'''
def getUrutanMatkul(listMataKuliah):
    done = False
    #inisiasi boolean yang akan digunakan sebagai tanda selesainya proses

    urutanMatkul = []
    #inisiasi list yang akan menjadi list 2 dimensi berisi mata kuliah terurut per semester
    #list ini adalah nilai yang akan di-return oleh fungsi ini

    while (not done):
        currentSemester = []
        #inisiasi list yang akan diisi mata kuliah yang diambil di semester
        #yang sedang diproses, nantinya akan di-append ke list 'urutanMatkul'

        for i in range(len(listMataKuliah)):
            if (len(listMataKuliah[i]) == 1):
            #jika hanya ada satu elemen pada listMataKuliah[i], 
            #artinya mata kuliah pada listMataKuliah[i][0] adalah
            #mata kuliah yang tidak ada prasyaratnya lagi (bisa diambil)
                currentSemester.append(listMataKuliah[i][0])
                #tambahkan mata kuliah yang sudah tidak ada prasyaratnya ke list 'currentSemester'

        for i in range(len(currentSemester)):
            for j in range(len(listMataKuliah)):
                if (currentSemester[i] in listMataKuliah[j]):
                    listMataKuliah[j].remove(currentSemester[i])
                    #menghapus mata kuliah yang diambil di semester ini dari listMataKuliah.
                    #dihapus baik sebagai mata kuliah itu sendiri maupun sebagai prasyarat mata kuliah lain.
        			#penghapusan dilakukan di sini (tidak segera setelah mata kuliah semester ini ditemukan) 
                    #untuk mencegah suatu mata kuliah diambil pada semester yang sama dengan mata kuliah prasayaratnya
        
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