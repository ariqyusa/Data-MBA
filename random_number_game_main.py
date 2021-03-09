import random as rd
import getpass as gp
import time
import os
from prettytable import PrettyTable as pt

#Membuat file data user
if not (os.path.isfile("user_data.txt")):
    new_file = open("user_data.txt", "w+")
    new_file.write("id;pass\n")
    new_file.close()

# Highscore data
if not os.path.isfile("user_score.txt"):
    new_file2 = open("user_score.txt", "w+")
    new_file.close()
    


#utk judul
print("*" * 40)
print("SELAMAT DATANG DI GAME TEBAK ANGKA!")
print("*" * 40)

def menu_utama():
    #DAFTARMENU
    print("\nMenu")
    print("1. Main")
    print("2. Daftar")
    print("3. High Score")
    print("4. Keluar") 
    opsi = input("Pilihan Anda : ")

    #MENU
    if opsi == "1":
        login()
        time.sleep(3)
        tebak_angka()
        menu_utama()
    elif opsi == "2":
        daftar()
        menu_utama()
    elif opsi == "3":
        high_score()
        menu_utama()
    elif opsi == "4":
        while True:
            opsi_kembali = input("Apakah Anda ingin keluar dari aplikasi (Y/N)")
            if opsi_kembali.upper() == 'Y':
                print('TERIMA KASIH SUDAH MEMAINKAN GAME INI')
                return
            elif opsi_kembali.upper() == 'N':
                print('Anda akan diarahkan ke menu utama...')
                time.sleep(1)
                menu_utama()
            else :
                print ("Perintah tidak dapat diproses. Pastikan untuk hanya mengetikan huruf \"Y\" atau \"N\" dengan benar")
    else:
        print("Pilihan Tidak Tersedia")
        menu_utama()

#INPUTUSERNAME DAN PASS
def input_user(var1):
    #fungsi utk daftar, cek username ada apa gak
    if var1 == "daftar":
        input_user.user = input("Masukkan Username : ")
        cek_user("daftar")
        
    #fungsi utk login, cek username dan pass sama apa gak sama yg di txt
    elif var1 == "login":
        input_user.user = input("Masukkan Username : ")
        input_user.password = gp.getpass(prompt = "Masukkan Password : ")
        cek_user("login")

#CEK USERNAME
def cek_user(var2):
    #open txt user_data
    user_save = open("user_data.txt","r")
    user_save1 = user_save.read()
    
    #membuat data di user_data jadi list
    user_list = user_save1.split("\n")
    
    #fungsi cek user utk daftar, klo user udh ada suruh input ulang
    if var2 == "daftar":
        user_list1 = [datauser.split("#$",1)[0] for datauser in user_list]
        a = input_user.user in user_list1
        if a == True:
            print("USERNAME SUDAH ADA")
            menu_utama()
            
  
    elif var2 == "login":
        a = input_user.user+"#$"+input_user.password
        b = a in user_list
        if b == False:
            print("USER TIDAK DITEMUKAN ATAU PASSWORD SALAH")
            menu_utama()
    user_save.close()

#REGISTRASI USER BARU 
def daftar():
    #jalanin fungsi input_user utk daftar
    input_user("daftar")
    pass_ = gp.getpass(prompt = "Masukkan Password : ")
    
    #bikin variabel buat masukin data yg didaftarkan ke txt
    userpass = "{}#${}\n".format(input_user.user,pass_)
    
    #buka file txt user_data
    exp_txt = open("user_data.txt","a")
    
    #masukin variabel userpass ke file user_data
    exp_txt.write(userpass)
    exp_txt.close()
    print("PENDAFTARAN BERHASIL")

#LOGIN
def login():
    input_user("login")
    print("LOGIN BERHASIL")
    print("PERMAINAN SEGERA DIMULAI ...\n")

#MAEN TEBAK ANGKA NEH
def tebak_angka():
    print("*" * 40)
    print("PERMAINAN TEBAK ANGKA")
    print("*" * 40)
    print("\nCoba tebak angka dari 1 - 20")
    print("tebak Angka yang Saya pikirkan")
    print("Input HARUS berupa Angka ya")
    
    #generate random number antara 1-20
    a = rd.randint(1,21) 
    
    #INISIASI SKOR AWAL
    score = 100
    
    #inisiasi nilai tebakan awal, disimpan di variabel b
    b=0
    
    #INISIASI TEBAKAN BENER
    tebakan_bnr = False

    #LOOPING, KALAU SKOR BELOM 0 DAN TEBAKAN BELOM BENER, BAKAL MAIN TERUS
    while score > 0 and b != a:
        try:
            print("Score Anda saat ini ", score,"\n")
            b = int(input("Masukkan tebakkan Anda : "))
            
            #KALO TEBAKAN BENER
            if b == a:
                tebakan_bnr = True
            
            #KALO TEBAKAN LEBIH GEDE
            elif b > a:
                score -= 10
                print("\nKebesaran euy, score  dikurangi 10")
            
            #KALO TEBAKAN LEBIH KECIL
            else:
                score -= 10
                print("\nUps kekecilan euy, score dikurangi 10")
        
        #KALO MASUKIN SELAIN ANGKA
        except ValueError:
            score -= 20
            print("Tebakkan harus berupa Angka")
            print("Penalty, poin dikurangi 20")
    
    #KALO TEBAKAN BENER, SKOR AKHIR MUNCUL
    if tebakan_bnr:
        print("Congrats ! Tebakan nya Benar !")
        print("Score Anda ",score)
        time.sleep(3)
        
    #kalau score udah 0, game selesai
    else:
        print("Anda kurang beruntung! Akan diarahkan ke Menu Utama....")
        time.sleep(3)
        
    #NYIMPEN UER DAN SKORNYA
    save_score = "{}#${}\n".format(input_user.user,score)
    
    #BUKA FILE USER_SCORE
    hiscore_save = open("user_score.txt","a")
    
    #masukin username sama skor ke file user_score
    hiscore_save.write(save_score)
    hiscore_save.close
    
#NAMPILIN HIGH SCORE
def high_score():
    print("\nHIGH SCORE")
    #buka file user_score
    hiscore_list = open("user_score.txt","r")
    
    #membaca file user_score
    a = hiscore_list.read()
    
    #mengubah isi file user_score menjadi list, disimpan di variabel a1
    a1 = a.split("\n")
    
    #menghapus isi file user_score yang mengandung spasi atau blank
    a1.remove("")
    
    #mengambil data username
    a2 = [i.split("#$",1)[0] for i in a1]
    list_user = set(a2)
    
    #mengambil data score
    a3 = [i.split("#$",1)[1] for i in a1]
    
    #BUAT DICTIONARY
    #kenapa dictionary, biar bisa memetakan score2 milik username siapa
    dic = {}
    
    #proses memetakan score2 yg ada ke username
    for x,y in zip(a2,a3):
        dic.setdefault(x,[]).append(y)
        
   
        list_user = list()
    #proses mengambil data username utk dimasukkan ke list_user
    for i in dic.keys():
        list_user.append(i)
        

    list_score = list()
    #AMBIL DATA SOCRE DIMASUKIN KE LIST_SCORE
    for i in dic.values():
        for j in range(0,len(i)):
            i[j] = int(i[j])
        list_score.append(max(i))
        
    #membuat tabel high score
    hiscore_table = pt()
    
    #NAMBAH KOLOM USERNAME SAMA ISI USERNAME
    hiscore_table.add_column("Username", list_user)
    
    #NAMBAH KOLOM SKOR SAMA ISI KOLOM
    hiscore_table.add_column("Score", list_score)
    
    #URUTKAN TABEL DARI SKOR PALING TINGGI
    hiscore_table.sortby = "Score"
    hiscore_table.reversesort = True
    
    #TOP 10 HIGH SCORE
    print(hiscore_table.get_string(start=0,end=10))
    hiscore_list.close()
    
menu_utama()
