#!/usr/bin/env python3
#*- coding: utf-8 -*--
#Coded by Morbius.os

AUTHOR = 'Morbius.os'
GİTHUB = 'https://github.com/morbius-os'
INSTAGRAM= '@morbius.os'

import os
import time
import sys
import requests

def animasyon(yazi):
     for u in yazi + '\n' :
         sys.stdout.write(u)
         sys.stdout.flush()
         time.sleep(10. / 100)

def hızlı_ani(yazi):
     for u in yazi + '\n' :
         sys.stdout.write(u)
         sys.stdout.flush()
         time.sleep(10. / 250)
         
def max_ani(yazi):
     for u in yazi + '\n' :
         sys.stdout.write(u)
         sys.stdout.flush()
         time.sleep(1. / 55550)
         
Mor = '\033[95m'
Cyan = '\033[96m'
KoyuMavi = '\033[1;34m'
Mavi = '\033[94m'
Yeşil = '\033[92m'
Sarı = '\033[93m'
Kırmızı = '\033[91m'
Kalın = '\033[1m'
AltıÇizili = '\033[4m'
Bitir = '\033[0m'
Beyaz ='\033[1;37m'

def mini_banner():
        print(f"""{Kalın}
{Cyan} __  __            _     _             {Sarı}_   _ _     _                    
{Cyan}|  \/  | ___  _ __| |__ (_)_   _ ___  {Sarı}| | | (_) __| | ___ _ __                    
{Cyan}| |\/| |/ _ \| '__| '_ \| | | | / __| {Sarı}| |_| | |/ _` |/ _ \ '__|                
{Cyan}| |  | | (_) | |  | |_) | | |_| \__ \ {Sarı}|  _  | | (_| |  __/ |                    
{Cyan}|_|  |_|\___/|_|  |_.__/|_|\__,_|___/ {Sarı}|_| |_|_|\__,_|\___|_|                    
{Yeşil}
Author: {AUTHOR}
Instagram: {GİTHUB}
Github: {INSTAGRAM}{Bitir}""")
 
animasyon('{}Lütfen Biraz Sonra Çalışacak Olan Programda Herşeyde "Evet" Seçeneğini Seçiniz ve {}Programı ROOT Olarak Başlattığınızdan Emin Olunuz{}'.format(Beyaz,Kırmızı,Beyaz))
time.sleep(5)

try:
    os.system('bash installer.sh')
except:
    animasyon('Bir hata oluştu')
    time.sleep(3)
    
os.system("clear")
mini_banner()

animasyon("""
{}!!ÖNEMLİ!
Tool çalışmaya başladıktan sonra terminali kapatmayın, aksi takdirde tool kapanır!!{}
""".format(Kırmızı,Bitir))

süre = int(input("""Sürekli IP Değişimi İçin Saniye Türünden Süre Giriniz
Çok Sık IP Değiştirmeniz İnternetinizde Sıkıntı Yaratabilir.

{}┌──({}root㉿m-scan{})-[{}m-hider{}]
└─{}# {}m-hider --time """.format(Mavi,Kırmızı,Mavi, Beyaz,Mavi,Kırmızı,Beyaz)))

while süre >= 60:
    print(f'{Yeşil}Bir dakikadan Fazla Yapmanız Önerilmez. Lütfen Daha Az Bir Süre giriniz')
    süre = int(input("""
{}┌──({}root㉿m-scan{})-[{}m-hider{}]
└─{}# {}m-hider --time """.format(Mavi,Kırmızı,Mavi, Beyaz,Mavi,Kırmızı,Beyaz)))

print(f'{Kalın}')
os.system('clear')
cevap = requests.get('https://api.ipify.org/')
main_ip = cevap.text

hızlı_ani('••••••••••••••••••••••••••••••••')
animasyon('Your Main IP:')
print(ip)
hızlı_ani('••••••••••••••••••••••••••••••••')
try:
    os.system('anonsurf start')
except:
    print('Birşeyler Yanlış Gitti...')
    sys.exit()
animasyon('Your New IP:')
cevap = requests.get('https://api.ipify.org/')
ip = cevap.text
print(ip)
hızlı_ani('••••••••••••••••••••••••••••••••')

while True:
    time.sleep(süre) 
    os.system('clear')
        
    mini_banner()
    print("\n")
    hızlı_ani('••••••••••••••••••••••••••••••••')
    animasyon(f'Your Main IP: {main_ip}')
    hızlı_ani('••••••••••••••••••••••••••••••••')
    try:
        os.system('anonsurf restart')
        os.system('clear')
    except:
        print('Birşeyler Yanlış Gitti...')
        sys.exit()
    animasyon('Your New IP:')
    try:
        cevap = requests.get('https://api.ipify.org/')
        ip = cevap.text
    except:
        print(f'{Kırmızı}Bağlantı Hatası, Tool Otomatik Kapandı, Lütfen Tekrar Açınız...')
        sys.exit()
    print(ip)
    hızlı_ani('••••••••••••••••••••••••••••••••')
    time.sleep(süre)