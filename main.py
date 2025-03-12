class SayiKontrol:
    def __init__(self, sayi):
        self.sayi = sayi

    def kontrol_et(self):
        if self.sayi < 0:
            print("Negatif sayı girdiniz!")
        elif self.sayi % 2 == 0:
            print(f"{self.sayi} bir çift sayıdır.")
        else:
            print(f"{self.sayi} bir tek sayıdır.")

if __name__ == "__main__":
    try:
        girilen_sayi = int(input("Bir sayı giriniz: "))
        sayi_nesnesi = SayiKontrol(girilen_sayi)
        sayi_nesnesi.kontrol_et()
    except ValueError:
        print("Lütfen geçerli bir tam sayı giriniz!")
