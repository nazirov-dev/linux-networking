- Task - 10.1.1
    
    `haad:xavfsizlik` nom bilan user yaratilsin va uni host name `server01` bo’lsin. Va unda `19` ta `interfeys` bulishi kerak  
    
    `br-5720f05dd68a` bu interfeysga  [`172.16.50.1`](http://172.16.50.1/) ipni berish kerak, va maskasida [`255.255.255.0`](http://255.255.255.0/) ip bo’lishi kerak
    
- Task - 10.3.1
    
    5.`haad:xavfsizlik` useriga ulanish amalga oshiriladi va uni ichida yana boshqa ip(misol uchun `172.16.50.10` ) ga `curl http://172.16.50.10/` quydagicha zapros junatishi kerak ammo o’quvchi ip manzil `ip route add` qilib qo’shmasa zapros junata olmasiligi kerak yaniy serverdan so’rov chiqmasin. `172.16.50.10` quydagi ip dagi serverga [`server.py`](http://server.py/) joylashtirib quydagicha ishga tushirib qo’yish kerak (80 porti bo’sh bo’lishi kerak)
    
     
    
    ```python
    sudo python3 server.py
    ```
    
- Task - 10.5.1
    
    1.`haadyone:xavfsizlik` nomi bilan user yaratilsin ssh orqali ulanishda `2222` portdan foydalanilsin va `haadyone` ni home qismiga quydagicha fayl yaratilsin `SSH{Oddiy_Bo'lmagan_Kirish}`
    
    ```python
    haadyone@host:~$ ls
    SSH{Oddiy_Bo'lmagan_Kirish}
    ```
    
    1. `john:password` (2222-portda ssh orqali ulaniladi) `check_tmp.py`(bu fayl flag yaratadi shu uchun buni root home qismiga qo’ysa ham yaxshi bo’ladi) fayli har 1daqiqada ishga tushib turishi kerak (`sudo python3 check_tmp.py`)  
- Task - 10.6.6
    
    1.`haady:xavfsizli` ulaniladi va [555.py](http://555.py) (sudo python3 555.py)   [555.py](http://555.py) nc orqali ulansa flag beradigan fayl buni ham root qismiga qo’shib qo’yilsa yaxshi bo’lardi
    
    1. [4444.py](http://4444.py)  (sudo python3 4444.py) ishga tushurishi kerak va flag beradigan fayl buni ham root qismiga qo’shib qo’yilsa yaxshi bo’lardi
        1. nc/ papka yaratilsin va ichida [`456.py](http://456.py/) [567.py](http://567.py/)` quyilsin va (sudo python3 456.py)(sudo python3 567.py) qilib ishlatilsin  
- Task - 10.7.3
    1. `server_555.py` fayli urnatilsin va  (`sudo python3 server_555.py`) ishga tushirilsin
    2. `server_4444.py` fayli urnatilsin va  (`sudo python3 server_4444.py`) ishga tushirilsin
    
    3-4. [`456.py](http://456.py/) [567.py](http://567.py/)` faylar joylansin va quydagicha ishga tushirib quyilsin `(sudo python3 456.py)(sudo python3 567.py)`  
    
- Task - 10.8.1
    1. `wget_server.py` bu fayl rootga qo’yilsin va quydagicha ishga tushirilsin (`sudo python3 wget_server.py`) 80-porti boshqa narsa ilab turmasin bu 80-portdan foydalanadi bunga kerakli fayl `wget_server`  quydagicha joylanishi shart bo’lmasa ctf xato ishlaydi `/root/wget_server/`
    2. proxy_server.py proxy server  client_server.py  clent uchun server va flag qaytaradi 
(sudo python3 proxy_server.py  ) (sudo python3 client_server.py) (80va 3128 portlaridan foydalanadi )
    3. `ssl_server.py` serverga mudati o’tgan ssl o’rnish kerak va tekshirish kerak kod faqat flag qaytaradi sslga tekshimaydi (`sudo python3 ssl_server.py`) 443-portda ishlayri
- Task - 10.10.1
    
    1.`kali:kali` ftp ulanish uchun user, `FTP-flag1.txt`  yaratilsin `FTP{Standart_Kirish}` text yozilsin
    
    1. **anonymous** user orqali ulanish mumkun bo’lsin va `keep/going/further/FTP-flag2.txt`  yaratilsin `FTP{Ular_Hammani_Kiritaveradi}` text yozilsin
    2. `haady:haady` user yaratilsin ftp orqali ulaniladi va uni home papkasi `home/haady` bo’lsin va `flag3` papka yaratilgan bo’lishi kerak. [`checkerftp.py`](http://checkerftp.py/) fayl ni run qilib qo’yish kerak har 1 minutda ishga tushib turishi kerak (`sudo python3  [checkerftp.py](http://checkerftp.py/)` )