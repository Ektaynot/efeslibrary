import os.path
import os
import glob
date=os.system("date")
liste=(glob.glob("*.txt"))
istek=input("Kitap Takipçisine Hoşgeldiniz\nSeçilebilecek Durumlar\nKitap Bulma(1)\nKitap Ekle(2)\nKitap Sil(3)\nKitap Listesi(4)\nKitap Düzenleme(5)\nKitap Listesi(6)\nÇıkış(q)\nSeçiminiz:")
print(date)
while istek != "q":
    if istek == "1":
        sn=input("Lütfen istediğiniz kitabın numarasını giriniz:")
        b=os.path.exists(sn+".txt")
        b = str(b)
        if b == "False":
            print ("kitap bulunamadı")
            raise SystemExit
        elif b == "True":
            oku=open(sn+".txt","r")
            print(oku.readline())
            raise SystemExit
    elif istek == "2":
        gkn=input("Lütfen kitap numarasını girin:")
        kd = open((gkn+".txt"),"w+")
        gki=input("Lütfen kitap ismini girin:")
        gky=input("Lütfen kitabın yazarını yazın:")
        tkb=(gki+" "+gky)
        ke = open(gkn+".txt", "a")
        ke.write(tkb)
        ke.close()
        raise SystemExit
    elif istek == "3":
        gb=input("Lütfen silmek istediğiniz kitabın numarasını giriniz")
        os.remove((gb+".txt"))
        raise SystemExit
    elif istek == "5":
        gkn=input("Lütfen Düzenlemek İstediğiniz Kitabın Numarasını Yazınız:")
        kd=open(gkn+".txt","a+") 
        b=os.path.exists(gkn+".txt")
        b = str(b)
        if b == "False":
            print ("Değiştirmek istediğiniz kitap bulunamadı.")
            raise SystemExit
        elif b == "True":
            oku=open(gkn+".txt","r")
            print(oku.readline())
            secim=input("Kitabın içeriğiniz silip yeniden yazmak ister misiniz?(evet veya hayır)")
            if secim == "evet":
                f = open(gkn+'.txt', 'r+')
                f.truncate(0)
                gki=input("Lütfen kitap ismini girin:")
                gky=input("Lütfen kitabın yazarını yazın:")
                f.write(gki+" "+gky)   
            raise SystemExit
        kd.write()       
        raise SystemExit
    elif istek == "6":
        a = 1
        nan=input("kaça kadar arama yapmak istersiniz:")
        while a < int(nan):
            b=os.path.exists(str(a)+".txt")
            b = str(b)
            while b == "True":
                oku=open(str(a)+".txt","r")
                print(str(a)+":"+oku.readline())
                break
            a=(a+1)
        raise SystemExit
