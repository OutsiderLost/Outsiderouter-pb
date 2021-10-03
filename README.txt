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

Use:

[Before that, make sure you have the necessary components installed: Python selenium, geckodriver for Firefox.]
[The chromedriver is optional, only if you need to modify the script.]

git clone https://github.com/OutsiderLost/Outsiderouter-pb.git

cd Outsiderouter

open Outsiderouter.py
(or)
nano Outsiderouter.py
(change it add the dictionary place)

(run the code)
python3 Outsiderouter.py

(wait for the script to freeze)
(use one of the commands to continue where you left off)
(exampe --> grep -A 99999999 -B 4 "74145678" /root/Desktop/test_dict.txt > /root/Desktop/test_dict02.txt)

(Run the script again) [If necessary, change the path according to the example to the new list. The command always overwrites the given list, so you don't have to do this all the time.]
