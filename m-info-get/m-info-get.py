#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# kaandgnsh Ultimate OSINT Tool (FULL MERGED VERSION - SAFE/PASSIVE)

import os
import sys
import time
import json
import re
import socket
import hashlib
import base64

# ===== COLORS (UNCHANGED STYLE) =====
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

# ===== PHONE LIB =====
try:
    import phonenumbers
    from phonenumbers import carrier, geocoder, timezone
except:
    os.system("pip install phonenumbers")
    import phonenumbers
    from phonenumbers import carrier, geocoder, timezone

try:
    import requests
except:
    os.system("pip install requests")
    import requests


# ===== BANNER (YOUR ORIGINAL STYLE PRESERVED) =====
def mini_banner():
    print(Kalın + f"""
, ＜￣｀ヽ、　　　　　 ／￣＞     
　ゝ、　　＼　／⌒ヽ,ノ  　/         •Welcome To•
　　　ゝ、　`（ ( ͡° ͜ʖ ͡°)／      •KaanDGN's•
　　 　　>　 　 　,)         •Info Get Tool•
　　　　 　∠_,,,/      
{Bitir}
Author: kaandgnsh
""")


# ===== MENU =====
def menu():
    print(f"""
============= {Kırmızı}{AltıÇizili}GET INFO WITH{Bitir} =============
{Kırmızı}[1]{Bitir} Phone
{Kırmızı}[2]{Bitir} Nick
{Kırmızı}[3]{Bitir} IP
{Kırmızı}[4]{Bitir} Email
{Kırmızı}[5]{Bitir} Domain
{Kırmızı}[6]{Bitir} Hash
{Kırmızı}[7]{Bitir} Base64
{Kırmızı}[8]{Bitir} URL
{Kırmızı}[9]{Bitir} Subdomain
{Kırmızı}[99]{Bitir} EXIT
""")


# ================= PHONE (YOUR FULL VERSION INCLUDED) =================
def PhoneGiveİnfo(phone):
    try:
        parsed_number = phonenumbers.parse(phone, None)

        region_code = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "tr")

        is_valid_number = phonenumbers.is_valid_number(parsed_number)
        is_possible_number = phonenumbers.is_possible_number(parsed_number)

        formatted_number = phonenumbers.format_number(
            parsed_number,
            phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )

        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(
            parsed_number,
            None,
            with_formatting=True
        )

        number_type = phonenumbers.number_type(parsed_number)

        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)

        print(f'============={Yeşil} PHONE İNFORMATİON {Bitir}=============')

        print(f"\n {Beyaz}Location             :{Yeşil} {location}")
        print(f" {Beyaz}region Code          :{Yeşil} {region_code}")
        print(f" {Beyaz}Timezone             :{Yeşil} {timezoneF}")
        print(f" {Beyaz}Operator             :{Yeşil} {jenis_provider}")
        print(f" {Beyaz}Valid number         :{Yeşil} {is_valid_number}")
        print(f" {Beyaz}Possible number      :{Yeşil} {is_possible_number}")
        print(f" {Beyaz}International format :{Yeşil} {formatted_number}")
        print(f" {Beyaz}Mobile format        :{Yeşil} {formatted_number_for_mobile}")
        print(f" {Beyaz}Original number      :{Yeşil} {parsed_number.national_number}")
        print(f" {Beyaz}E.164 format         :{Yeşil} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
        print(f" {Beyaz}Country code         :{Yeşil} {parsed_number.country_code}")
        print(f" {Beyaz}Local number         :{Yeşil} {parsed_number.national_number}")

        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            print(f" {Beyaz}Type                 :{Yeşil} Mobile")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f" {Beyaz}Type                 :{Yeşil} Fixed line")
        else:
            print(f" {Beyaz}Type                 :{Yeşil} Other")

    except:
        print(f"{Kırmızı}Phone error{Bitir}")


# ================= NICK (YOUR TRACK SYSTEM INCLUDED) =================
def TrackUserName(username):
    results = {}

    social_media = [
        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
        {"url": "https://www.twitter.com/{}", "name": "Twitter"},
        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
        {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
        {"url": "https://www.github.com/{}", "name": "GitHub"},
        {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
        {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
        {"url": "https://www.youtube.com/{}", "name": "Youtube"},
        {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
        {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
        {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
        {"url": "https://www.behance.net/{}", "name": "Behance"},
        {"url": "https://www.medium.com/@{}", "name": "Medium"},
        {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
        {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
        {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
        {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
        {"url": "https://www.ello.co/{}", "name": "Ello"},
        {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
        {"url": "https://www.telegram.me/{}", "name": "Telegram"},
        {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
    ]

    for site in social_media:
        try:
            url = site["url"].format(username)
            r = requests.get(url, timeout=4)

            if r.status_code == 200:
                results[site["name"]] = url
            else:
                results[site["name"]] = "Not Found"
        except:
            results[site["name"]] = "Error"

    return results


def NickGiveInfo():
    username = input(f"\n {Beyaz}Nick'i Yazınız : {Yeşil}")

    print(f"\n {Beyaz}========== {Yeşil} USERNAME İNFO {Beyaz}==========")

    results = TrackUserName(username)

    for site, url in results.items():
        print(f" {Beyaz}[ {Yeşil}+ {Beyaz}] {site} : {Yeşil}{url}")


# ================= IP =================
def ip_info(ip):
    print(f"{Yeşil}\n[IP INFO]{Bitir}")

    if not re.match(r'^\d{1,3}(\.\d{1,3}){3}$', ip):
        print(f"{Kırmızı}Geçersiz IP{Bitir}")
        return

    print(f"{Beyaz}IP : {Yeşil}{ip}")


# ================= EMAIL =================
def email_info(email):
    print(f"{Yeşil}\n[EMAIL]{Bitir}")
    if "@" not in email:
        print(f"{Kırmızı}Geçersiz{Bitir}")
        return

    domain = email.split("@")[1]
    print(f"{Beyaz}Domain : {Yeşil}{domain}")

    try:
        print(f"{Beyaz}IP     : {Yeşil}{socket.gethostbyname(domain)}")
    except:
        pass


# ================= DOMAIN =================
def domain_info(domain):
    print(f"{Yeşil}\n[DOMAIN]{Bitir}")
    try:
        print(f"{Beyaz}IP : {Yeşil}{socket.gethostbyname(domain)}")
    except:
        print(f"{Kırmızı}Hata{Bitir}")


# ================= HASH =================
def hash_tool(text):
    print(f"{Yeşil}\n[HASH]{Bitir}")
    print(f"{Beyaz}MD5  : {Yeşil}{hashlib.md5(text.encode()).hexdigest()}")
    print(f"{Beyaz}SHA1 : {Yeşil}{hashlib.sha1(text.encode()).hexdigest()}")


# ================= BASE64 =================
def base64_tool(text):
    print(f"{Yeşil}\n[BASE64]{Bitir}")
    e = base64.b64encode(text.encode()).decode()
    print(f"{Beyaz}ENC : {Yeşil}{e}")


# ================= URL =================
def url_info(url):
    print(f"{Yeşil}\n[URL]{Bitir}")
    print(f"{Beyaz}HTTPS : {Yeşil}{url.startswith('https')}")


# ================= SUBDOMAIN =================
def subdomain(domain):
    print(f"{Yeşil}\n[SUBDOMAIN]{Bitir}")

    subs = ["www", "mail", "ftp", "api"]

    for s in subs:
        try:
            socket.gethostbyname(f"{s}.{domain}")
            print(f"{Yeşil}FOUND: {s}.{domain}")
        except:
            pass


# ================= MAIN =================
def main():
    while True:
        os.system("clear")
        mini_banner()
        menu()

        c = input(f"{Beyaz}Seçim: {Yeşil}")

        if c == "1":
            print("Örnek: +905551234567")
            PhoneGiveİnfo(input("Numara: "))

        elif c == "2":
            NickGiveInfo()

        elif c == "3":
            ip_info(input("IP: "))

        elif c == "4":
            email_info(input("Email: "))

        elif c == "5":
            domain_info(input("Domain: "))

        elif c == "6":
            hash_tool(input("Text: "))

        elif c == "7":
            base64_tool(input("Text: "))

        elif c == "8":
            url_info(input("URL: "))

        elif c == "9":
            subdomain(input("Domain: "))

        elif c == "99":
            sys.exit()

        input("\nENTER...")


if __name__ == "__main__":
    main()