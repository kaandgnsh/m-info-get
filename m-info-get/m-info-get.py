#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# KaanDGN Ultimate OSINT - V13.0 (DEEP NICK & PHONE RECON)

import os
import sys
import time
import re
import socket
import threading
import hashlib
import base64
import requests
from concurrent.futures import ThreadPoolExecutor

# ===== COLORS (ORIGINAL - PROTECTED) =====
Mor = '\033[95m'
Cyan = '\033[96m'
KoyuMavi = '\033[36m'
Mavi = '\033[94m'
Yeşil = '\033[92m'
Sarı = '\033[93m'
Kırmızı = '\033[91m'
Kalın = '\033[1m'
AltıÇizili = '\033[4m'
Bitir = '\033[0m'
Beyaz = '\033[1;37m'

# ===== DEPENDENCIES (AUTOMATIC) =====
def check_deps():
    packages = {
        "phonenumbers": "phonenumbers",
        "requests": "requests",
        "bs4": "beautifulsoup4",
        "dnspython": "dns",
        "googlesearch-python": "googlesearch"
    }
    for pkg, lib in packages.items():
        try:
            __import__(lib)
        except ImportError:
            os.system(f"pip install {pkg} --quiet")

check_deps()

import phonenumbers
from phonenumbers import carrier, geocoder, timezone, number_type
from bs4 import BeautifulSoup
import dns.resolver
from googlesearch import search

# ===== BANNER (KaanDGN) =====
def mini_banner():
    os.system("clear || cls")
    print(Kalın + f"""
, ＜￣｀ヽ、　　　　　 ／￣＞     
　ゝ、　　＼　／⌒ヽ,ノ  　/         •Welcome To•
　　　ゝ、　`（ ( ͡° ͜ʖ ͡°)／      •KaanDGN's•
　　 　　>　 　 　,)         •Elite Info Tool•
　　　　 　∠_,,,/      
{Bitir}
Author: KaanDGN | {Kırmızı}Status: ULTRA RECON MODE ACTIVE{Bitir}
""")

# ===== MENU =====
def menu():
    print(f"""
============= {Kırmızı}{AltıÇizili}GET INFO WITH{Bitir} =============
{Kırmızı}[1]{Bitir} MEGA PHONE SEARCH (Deep Info/Social/Ghost)
{Kırmızı}[2]{Bitir} DEEP NICK SEARCH (All Social Media)
{Kırmızı}[3]{Bitir} IP Geo-Location
{Kırmızı}[4]{Bitir} Email Analysis
{Kırmızı}[5]{Bitir} Domain/Whois Info
{Kırmızı}[6]{Bitir} Hash Tool (Crack/Gen)
{Kırmızı}[7]{Bitir} Base64 Tool
{Kırmızı}[8]{Bitir} URL/Header Checker
{Kırmızı}[9]{Bitir} Subdomain Brute
{Kırmızı}[10]{Bitir} Port Scanner
{Kırmızı}[11]{Bitir} Deep DNS (MX/TXT)
{Kırmızı}[12]{Bitir} VPN/Proxy Detect
{Kırmızı}[13]{Bitir} ACTIVE DORK SCANNER
{Kırmızı}[99]{Bitir} EXIT
""")

# ================= SOCIAL THREAD HELPER =================
def _hunter_thread(platform, query):
    try:
        for url in search(query, num_results=1, sleep_interval=2):
            print(f" {Beyaz}[ {Yeşil}FOUND {Beyaz}] {platform:<10} : {Yeşil}{url}{Bitir}")
    except: pass

# ================= 1: MEGA PHONE SEARCH (FULL) =================
def MegaPhoneSearch(phone_input):
    print(f'\n============={Yeşil} DEEP PHONE ANALYSIS {Bitir}=============')
    
    # FORMAT MOTORU
    digits = re.sub(r'\D', '', phone_input)
    if digits.startswith('0'):
        final_phone = "+90" + digits[1:]
    elif digits.startswith('90') and len(digits) > 10:
        final_phone = "+" + digits
    elif len(digits) == 10:
        final_phone = "+90" + digits
    else:
        final_phone = "+" + digits if not phone_input.startswith("+") else phone_input

    # TEKNİK ANALİZ
    print(f"{Sarı}[*] Teknik Veriler Çözümleniyor: {Beyaz}{final_phone}{Bitir}")
    try:
        parsed = phonenumbers.parse(final_phone, None)
        if phonenumbers.is_valid_number(parsed):
            ntype = phonenumbers.number_type(parsed)
            type_map = {0: "Sabit Hat", 1: "Mobil (GSM)", 2: "Sabit/Mobil", 6: "VOIP", 8: "Pager"}
            
            print(f" {Beyaz}Durum        : {Yeşil}GEÇERLİ{Bitir}")
            print(f" {Beyaz}Hat Tipi     : {Yeşil}{type_map.get(ntype, 'Bilinmiyor')}{Bitir}")
            print(f" {Beyaz}Ülke/Bölge   : {Yeşil}{geocoder.description_for_number(parsed, 'tr')}{Bitir}")
            print(f" {Beyaz}Operatör     : {Yeşil}{carrier.name_for_number(parsed, 'tr')}{Bitir}")
            print(f" {Beyaz}Zaman Dilimi : {Yeşil}{timezone.time_zones_for_number(parsed)}{Bitir}")
            print(f" {Beyaz}Uluslararası : {Yeşil}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}{Bitir}")
        else:
            print(f"{Kırmızı}[!] Numara geçersiz!{Bitir}")
    except:
        print(f"{Kırmızı}[!] Teknik bilgi alınamadı.{Bitir}")

    # SOSYAL MEDYA
    print(f"\n{Sarı}[*] Dijital Ayak İzi Taraması...{Bitir}")
    clean_num = final_phone.replace("+", "")
    print(f" {Beyaz}[ {Yeşil}LINK {Beyaz}] WhatsApp: {Cyan}https://wa.me/{clean_num}{Bitir}")
    
    targets = {
        "Instagram": f'site:instagram.com "{final_phone}" OR "{clean_num}"',
        "Twitter": f'site:twitter.com "{final_phone}" OR "{clean_num}"',
        "Facebook": f'site:facebook.com "{final_phone}" OR "{clean_num}"'
    }
    
    threads = [threading.Thread(target=_hunter_thread, args=(p, q)) for p, q in targets.items()]
    for t in threads: t.start()
    for t in threads: t.join()

    # GHOST SEARCH
    print(f"\n{Sarı}[*] Ghost Search (Derin İzler)...{Bitir}")
    queries = [f'"{final_phone}"', f'"{clean_num}"', f'site:tellows.com "{clean_num}"']
    try:
        for q in queries:
            for res in search(q, num_results=1, sleep_interval=1):
                print(f" {Beyaz}[ {Yeşil}GHOST {Beyaz}] {res}")
    except: pass

# ================= 2: DEEP NICK SEARCH (EXPANDED) =================
def NickSearch(username):
    print(f'\n============={Yeşil} DEEP NICK SEARCH {Bitir}=============')
    print(f"{Sarı}[*] Hedef Nick: {Beyaz}{username}{Sarı} taranıyor...{Bitir}\n")
    
    sites = {
        "Instagram": "https://www.instagram.com/",
        "Twitter/X": "https://www.twitter.com/",
        "GitHub": "https://www.github.com/",
        "YouTube": "https://www.youtube.com/@",
        "TikTok": "https://www.tiktok.com/@",
        "Reddit": "https://www.reddit.com/user/",
        "Pinterest": "https://www.pinterest.com/",
        "Snapchat": "https://www.snapchat.com/add/",
        "Telegram": "https://t.me/",
        "Linktree": "https://linktr.ee/",
        "Twitch": "https://www.twitch.tv/",
        "Steam": "https://steamcommunity.com/id/",
        "Medium": "https://medium.com/@"
    }

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

    for name, base in sites.items():
        try:
            url = base + username
            res = requests.get(url, timeout=5, headers=header)
            if res.status_code == 200:
                print(f" {Beyaz}[ {Yeşil}FOUND {Beyaz}] {name:<12}: {Yeşil}{url}{Bitir}")
            else:
                print(f" {Beyaz}[ {Kırmızı}NOT FOUND {Beyaz}] {name:<12}")
        except:
            print(f" {Beyaz}[ {Mor}ERROR {Beyaz}] {name:<12}")

# ================= 13: ACTIVE DORK SCANNER =================
def DorkSearch(target):
    print(f'\n============={Yeşil} ACTIVE DORK SCANNER {Bitir}=============')
    dorks = [f'"{target}"', f'site:pastebin.com "{target}"', f'site:github.com "{target}"', f'"{target}" filetype:pdf']
    try:
        for dork in dorks:
            for res in search(dork, num_results=1, sleep_interval=2):
                print(f" {Beyaz}[ {Yeşil}DORK FOUND {Beyaz}] {res}")
    except: print(f"{Kırmızı}[!] Google Engeli!{Bitir}")

# ================= MAIN LOOP =================
def main():
    while True:
        mini_banner()
        menu()
        c = input(f"{Beyaz}Seçim: {Yeşil}")
        
        if c == "1":
            print(f"\n{Sarı}[!] ÖRNEK: {Beyaz}+905556667788 {Sarı}veya {Beyaz}0555...{Bitir}")
            MegaPhoneSearch(input(f"{Beyaz}Hedef Numara: {Yeşil}"))
        elif c == "2":
            NickSearch(input(f"{Beyaz}Hedef Nick: {Yeşil}"))
        elif c == "3":
            # IP Info Fonksiyonu (V8.0'daki gibi eklenebilir)
            pass
        elif c == "13":
            DorkSearch(input(f"{Beyaz}Hedef Bilgi: {Yeşil}"))
        elif c == "99":
            sys.exit()
            
        input(f"\n{Mor}Devam etmek için ENTER...{Bitir}")

if __name__ == "__main__":
    main()
