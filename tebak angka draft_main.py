#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 06:33:40 2021

@author: sheenaabigail
"""
import random

def main():
    score = 100
    angka = random.randint(1, 20)
    tebakan = 0

    print("**************************************")
    print("PERMAINAN TEBAK ANGKA")
    print("**************************************")
    print('Saya memikirkan sebuah angka dari 1-20')
    print('Silahkan tebak angka yang saya pikirkan')
    print('Input harus berupa ANGKA')
    print(f'Score Anda saat ini adalah {score}')

    while tebakan != angka:
        tebakan = input('\nMasukkan tebakan Anda: ')
        if not tebakan.isdigit():
            score -= 20
            print("Tebakan harus berupa angka.")
            print("Penalty, poin dikurangi 20")
            print(f"Score anda saat ini {score}")
            continue
        tebakan = int(tebakan)
        if tebakan > angka:
            score -= 10
            print('Tebakan Anda terlalu besar, score Anda dikurangi 10')
            print(f"Score anda saat ini {score}")
        elif tebakan < angka:
            score -= 10
            print('Tebakan Anda terlalu kecil, score Anda dikurangi 10')
            print(f"Score anda saat ini {score}")
            
    print('Selamat! Tebakan Anda benar')
    print(f'Score Anda: {score}')
        

if __name__ == "__main__":
    main()
            
