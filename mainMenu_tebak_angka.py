# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 03:56:34 2021

@author: HP
"""
import random

def mainMenu():
    print('''
    ------------------------------
              MAIN MENU 
              
    Input 1-4 
    1. Play 
    2. Register
    3. High Score
    4. Exit
    ''')
    
    selection = str(input("Enter choice : "))
    if selection == "1" : 
        play()
        input('Enter any key to continue')
        mainMenu()
    elif selection == "2" : 
        print(selection)
    elif selection == "3" : 
        print(selection) 
    elif selection == "4" : 
        print("Thank you for playing!" )
    else :
        print("Invalid choice. Enter 1-4 ")
        mainMenu()
        
def play():
    score = 100
    angka = random.randint(1, 20)
    tebakan = 0

    print('''
          **************************************
                   PERMAINAN TEBAK ANGKA
          **************************************
          Saya memikirkan sebuah angka dari 1-20
          Silahkan tebak angka yang saya pikirkan
          Input harus berupa ANGKA''')
    print(f'''Score Anda saat ini adalah {score}''')

    while tebakan != angka:
        tebakan = input('\nMasukkan tebakan Anda: ')
        if not tebakan.isdigit():
            score -= 20
            print("Tebakan harus berupa angka.")
            print("Penalty, poin dikurangi 20")
            print(f"Score anda saat ini {score}")
            if score <= 0:
                break
            continue
        tebakan = int(tebakan)
        if tebakan > angka:
            score -= 10
            print('Tebakan Anda terlalu besar, score Anda dikurangi 10')
            print(f"Score anda saat ini {score}")
            if score <= 0 : 
                break
        elif tebakan < angka:
            score -= 10
            print('Tebakan Anda terlalu kecil, score Anda dikurangi 10')
            print(f"Score anda saat ini {score}")
            if score <= 0 : 
                break
            
    print('-'*25)
    if score <= 0 : 
        print('Score Anda sudah habis' )
        print('Silahkan coba kembali' )
    if score != 0 :     
        print('Selamat! Tebakan Anda benar')
        print(f'Score Anda: {score}')
    
    
mainMenu()

