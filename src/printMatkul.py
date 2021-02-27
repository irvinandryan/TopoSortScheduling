'''
Irvin Andryan P. (13519162)
IF 2211 K-03
Tugas Kecil 2 : Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer)
'''

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