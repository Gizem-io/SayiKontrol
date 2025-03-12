from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(200, 10, "Python'da If-Else Kullanimi ve Siniflar", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Sayfa {self.page_no()}", align="C")

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Aciklamalari PDF'e ekleyelim
explanation = """# Python'da If-Else Kullanimi ve Siniflar

Bu PDF, Python'da `if-else` ifadelerinin nasil kullanildigini ve bunu bir sinif yapisiyla nasil birlestirebilecegimizi anlatir.

## 1. Sinif Tanimlama:
Python'da bir sinif tanimlamak icin `class` anahtar kelimesi kullanilir. `__init__` metodu, sinifin baslangic degerlerini (degiskenleri) belirlemek icin kullanilir.

## 2. If-Else Kosullu Ifadeleri:
If-else yapilari, belirli kosullara gore kodun farkli bolumlerinin calismasini saglar.

## 3. Kullanicidan Girdi Alma:
Python'da `input()` fonksiyonu kullanilarak kullanicidan veri alinir ve `int()` ile tam sayiya cevrilir.

Asagida, kullanicidan alinan bir sayinin cift mi, tek mi veya negatif mi oldugunu kontrol eden bir program bulunmaktadir:
"""

pdf.multi_cell(0, 10, explanation)
pdf.ln(5)

# Python kodu aciklamali olarak
code_text = """class SayiKontrol:
    # Sinif baslatildiginda cagrilan metod
    def __init__(self, sayi):
        self.sayi = sayi

    # Sayiyi kontrol eden metod
    def kontrol_et(self):
        if self.sayi < 0:
            return "Negatif sayi girdiniz!"
        elif self.sayi % 2 == 0:
            return f"{self.sayi} bir cift sayidir."
        else:
            return f"{self.sayi} bir tek sayidir."

# Ana program bolumu
if __name__ == "__main__":
    try:
        # Kullanicidan girdi al
        girilen_sayi = int(input("Bir sayi giriniz: "))

        # Sinifin bir ornegini olustur
        sayi_nesnesi = SayiKontrol(girilen_sayi)

        # Sonucu ekrana yazdir
        print(sayi_nesnesi.kontrol_et())

    except ValueError:
        # Eger kullanici sayi yerine harf girerse hata mesaji ver
        print("Lutfen gecerli bir tam sayi giriniz!")
"""

pdf.set_font("Courier", size=10)
pdf.multi_cell(0, 10, code_text)

# PDF dosyasini kaydetme
pdf.output("python_kosullu_ifadeler.pdf")

print("PDF dosyasi basariyla olusturuldu: python_kosullu_ifadeler.pdf")
