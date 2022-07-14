import re
import time 

class Kayıt : 
    def __init__(self,programad):
        self.programad = programad
        self.dongu = True

    def program(self):
        secim = self.menu()

        if secim =="1":
            print("Kayıt Ekleme Menüsüne Yönlendiriliyor...")
            time.sleep(3)
            self.kayitekle()
            
        if secim =="2":
            print("Kayıt Silme Menüsüne Yönlendiriliyor...")
            time.sleep(3)
            self.kayitcikar()
        
        if secim =="3":
            print("Verilere Erişiliyor...")
            time.sleep(3)
            self.kayitoku()

        if secim == "4":
            self.cikis()
        

    def menu(self):
        def kontrol(secim):
            if re.search("[^1-4]",secim): ## değerlerde 1 ve 4  arasında  harici bir karakter kontrolü
                raise Exception("Lütfen 1 ve 4 arasında geçerli seçim yapınız..." )
            elif len (secim) != 1:  ## secim inputunda  rakam kontrolü
                raise Exception("Lütfen 1 ve 4 arasında geçerli seçim yapınız..." )

        while True:
            try:
                secim = input("""Merhabalar , {} Otomasyon Sistemine Hoşgeldiniz..\n\n
                Lütfen Yapmak İstediğiniz İşlemi Seçiniz..\n\n
                [1]--Kayıt Ekle\n
                [2]--Kayıt Sil\n
                [3]--Kayıt Oku\n
                [4]--Çıkış
                \n\n
                   """.format(self.programad))
                
                kontrol(secim)
                
            except Exception as hata:
                print(hata)
                time.sleep(3)

            else:
                break
       
        return secim
                 

    def kayitekle(self): ## Burada kayıt için şartlarımız var.
        def kontrolAd(Ad):
            if Ad.isalpha() == False:
                raise Exception("Adınız Sadece Alfabetik Karakterlerden Oluşmalı...")
        
        while True:
            try:
                Ad = input("Adınız> ")
                kontrolAd(Ad)
            except Exception as hataAd:
                print(hataAd)
                time.sleep(3)
            else:
                break

        def kontrolSoyad(Soyad):
            if Soyad.isalpha() == False:
                raise Exception("Soyadınız Sadece Alfabetik Karakterlerden Oluşmalı...")
        
        while True:
            try:
                Soyad = input("Soyadınız> ")
                kontrolSoyad(Soyad)
            except Exception as hataSoyad:
                print(hataSoyad)
                time.sleep(3)
            else:
                break

        def kontrolYas(Yas):
            if Yas.isdigit() == False:
                raise Exception("Yaşınız Sadece Rakamlardan Oluşmalı...")
        
        while True:
            try:
                Yas = input("Yasınız> ")
                kontrolYas(Yas)
            except Exception as hataYas:
                print(hataYas)
                time.sleep(3)
            else:
                break

        def kontrolTc(Tc):
            if Tc.isdigit() == False:
                raise Exception("Kimlik Numaranız  Sadece Rakamlardan Oluşmalı...")
            elif len(Tc) != 11:
                 raise Exception("Kimlik Numaranız  11 Karakterden Oluşmalı...")
            
        while True:
            try:
                Tc = input("Kimlik Numarınız > ")
                kontrolTc(Tc)
            except Exception as hataTc:
                print(hataTc)
                time.sleep(3)
            else:
                break
       
       
        def kontrolMail(Mail):
            if not re.search("@" and ".com" ,  Mail):
                raise Exception("Geçerli Bir Mail Adresi Giriniz...")
        
        while True:
            try:
                Mail = input("Mail Adresiniz  > ")
                kontrolMail(Mail)
            except Exception as hataMail:
                print(hataMail)
                time.sleep(3)
            else:
                break

        with open("C:\\Users\\SOF\\Desktop\\örnek\\bilgiler.txt","r",encoding="utf-8")  as Dosya:
            satirsayisi = Dosya.readlines() ## satırları liste biçiminde yapıya oluşturur
        
        if len(satirsayisi)==0:
            Id = 1
        else:
             with open("C:\\Users\\SOF\\Desktop\\örnek\\bilgiler.txt","r",encoding="utf-8")  as Dosya:
                Id = int(Dosya.readlines()[-1].split("-")[0]) + 1 
                #Son satıra erişmek için  readlines -1  kullandık. Split sayesinde rakamı ve datayı ayrıştırdık ve 
                # eğer bir daha id eklerse +1  yazdık. 

        with open("C:\\Users\\SOF\\Desktop\\örnek\\bilgiler.txt","a+",encoding="utf-8")  as Dosya:  #a+ ekleme 
            Dosya.write("{}-{} {} {} {} {}\n".format(Id,Ad,Soyad,Yas,Tc,Mail))
            print("Veriler İşlenmiştir")
        self.menudon()


    def kayitcikar(self):
        sil = input("Lütfen Silmek İstediğiniz Kişinin Id Numarasını Giriniz > ")
        with open("C:\\Users\\SOF\\Desktop\\örnek\\bilgiler.txt","r",encoding="utf-8") as Dosya:
            liste  = []
            liste2 = Dosya.readlines()
            for i  in range(0,len(liste2)):
                liste.append(liste2[i].split("-")[0])
        
        del liste2[liste.index(sil)]

        with open("C:\\Users\\SOF\\Desktop\\örnek\\bilgiler.txt","w+",encoding="utf-8")  as YeniDosya:
            for i in liste2:
                YeniDosya.write(i)
            print("Kayıt Siliniyor...")
            time.sleep(3)
            print("Kayıt Başarıyla Silinmiştir...")
            self.menudon()
                 
                

    def kayitoku(self):
        with open("C:\\Users\\SOF\\Desktop\\örnek\\bilgiler.txt","r",encoding="utf-8") as Dosya:
            for i in Dosya:
                print(i)
            self.menudon()

    def cikis(self):
        print("Otomosyandon Çıkırılıyor...")
        time.sleep(3)
        self.dongu = False
        exit()

    def menudon(self):
        while True:
            x = input("Ana Menüye Dönmek İçin Lütfen 6 ' e Basınız \tÇıkmak için 5 'e Basınız >> ")
            if x == "6":
                print("Ana Menüye Dönülüyor..")
                time.sleep(3)
                self.program() # Menüyü Karşımıza Çıkarıyor 
                break

            elif x == "5":
                self.cikis()
                break
                
            else : 
                print("Lütfen Geçerli Bir Tuşa Basınız >> ")


Sistem = Kayıt("Veri-Kayıt")
while Sistem.dongu:
    Sistem.program()
