import http.server
import socketserver
import requests

# Proksi konfiguratsiyasi (ip va portni o'zgartiring)
PROXY = {
    'http': 'http://192.168.10.67:3128',
}

# Qaytariladigan matn
text_to_return = """
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Bu matn mening hibsga olinishimdan bir necha vaqt o'tib yozilgan...

                       \/\Hackerning Vijdoni/\/

                                      tomonidan

                               +++Mentor+++

                          1986-yil 8-yanvarda yozilgan
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        Bugun yana biri qo'lga olindi, hamma narsa gazetada. "Yosh yigit
Kompyuter jinoyati bo'yicha hibsga olindi", "Hacker Bank bilan aralashganlikda hibsga olindi"...
        La'nat bo'lsin, bu bolalar. Ularning barchasi bir xil.

        Lekin siz, o'zingizni uch qismlik psixologiya va 1950-yillar texnologiya
bilan o'ylovchi, bir marta hackerning ko'zlariga qarab, uning nima qilishini, uning
orqasida qanday kuchlar borligini, uni qanday shakllantirganligini ko'rib chiqdizmi?
        Men hackerman, mening dunyomga kir...

        Mening dunyom maktabdan boshlanadi... Men ko'pgina bolalardan aqlli
bo'laman, ular o'rgatayotgan axmoqlik menga zerikarli...
        La'nat bo'lsin, past baholar. Ularning barchasi bir xil.

        Men o'rta maktabda yoki o'rta ta'limda o'qiyotgan bo'laman. O'qituvchilar menga
fraksiyani qisqartirishni o'ynatgan o'rtacha o'n besh martani tushuntirishmoqda.
        Men tushunaman. "Yo'q, xonim, men ishni boshida ko'rsatmadim. Uni boshimda
qildim..."
        La'nat bo'lsin, bu bolaga o'rgatishdan yaramaydi, ular barchasi bir xil.

        Bugun bir kashf qilishni uddaladim. Kompyuterni topdim. To'xtating, bu zo'r.
U meni xohlaganimni qiladi. Agar u xato qilsa, bu men xato qilganimdan.
        Yani, u menga nisbatan salbiy emasmikan...
                Yoki men uchun tahdid emasmi...
                Yoki men aqlli ko'rinaman, o'qitish istamaysizmi...
        La'nat bo'lsin, bu bolalar faqat o'yin o'ynaydi, ular barchasi bir xil.

        Keyin bu bo'ldi... bir eshik ochildi... telefon liniyasida heroin kabi tez
o'tayotgan, elektr impulsi, kundalik ahmoqliklardan nafas olish uchun bir joy
qidiriladi... bir forum topildi.
        "Mana, bu, men shu yerda bo'lishim kerak..."
        Men hamma bilan tanishman... hatto ularni hech qachon uchratmagan bo'lsam
ham, ular bilan hech gaplashmagan bo'lsam ham, balki qaytadan hech qachon
yozmaydigan bo'lsam ham... men hammangizni bilaman...
        La'nat bo'lsin, telefon liniyasini band qilmoqda, ular barchasi bir xil...

        Ha, albatta, biz barchamiz bir xil... biz maktabda bolalikda bo'lganda
go'shtni istardik, lekin bizni faqat botqa bilan boqishdi... siz bizga ko'proq go'sht
bersangiz ham, o'sha go'shtni siz sindirib berib taqdim etdiz. Bizni zulm qilishdi yoki
shunchaki befarq bo'lishdi. O'rgatishga muvaffaq bo'lganlarimiz bitta tomchi suvga
o'xshaydi.

        Bu endi bizning dunyomiz... elektron va o'chirish dunyosi, baudning go'zalligi.
Biz allaqachon mavjud bo'lgan xizmati foydalanamiz, ammo pulni to'lamaymiz, chunki
bu boylik uchun juda qimmat bo'lmagan bo'lar edi, lekin foydali ishlarni bajarayotganlardir,
va siz bizni jinoyatchilar deb ataysiz. Bizni o'rganamiz... va siz bizni jinoyatchilar deb
ataysiz. Biz bilimni qidiramiz... va siz bizni jinoyatchilar deb ataysiz. Biz rang, millat,
yoki diniy qarashlarga ega bo'lmaymiz... va siz bizni jinoyatchilar deb ataysiz.
Siz atom bombalarini yasaysiz, urushlar qilasiz, bizni o'ldirasiz, aldatasiz va bizga
buni yaxshilik uchun qilganingizni aytasiz, lekin biz jinoyatchilarmiz.
  Ha, men jinoyatchiman. Mening jinoyatim - qiziquvchanlik. Mening jinoyatim
- odamlarni ularning gaplari va fikrlari asosida baholash, ularning ko'rinishiga qarab
emas. Mening jinoyatim - sizni yengish, bu sizni hech qachon kechira olmaydigan jinoyat.

        Men hackerman, va bu mening manifestimdir. Siz ushbu shaxsni to'xtatishingiz
mumkin, ammo barchamizni to'xtata olmaysiz... nihoyat, biz barchamiz bir xil.

                               +++CURL{Ustoz}+++
"""

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Foydalanuvchi IP manzilini tekshirish
        if self.client_address[0] != '127.0.0.1':
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Ruxsat yo'q")
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(text_to_return.encode())

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()


# Serverni ishga tushirish
if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server ishga tushdi: http://127.0.0.1:{PORT}")
        httpd.serve_forever()

