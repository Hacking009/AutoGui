import pyautogui as pg
import time as tm

class Behaviour:
    def __init__(self,*menu):
        if __name__=='__main__':
            print('[Author: AlDev]')
        index=1
        for i in menu:
            print([index],i)
            index+=1
        pass

    def AutoClick(self):
        try:
            startCounter = 1
            counter = int(input("Masukan Waktu: "))
            while startCounter<=counter:
                print(startCounter)
                tm.sleep(1)
                startCounter+=1
            pg.click()
        except:
            print("Ada Kesalahan")
        pass

    def AutoType(self):
        try:
            startCounter = 1
            counter = int(input("Masukan Waktu: "))
            message = str(input("Masukan Text: "))
            countMessage = int(input("Masukan Jumlah Pesan: "))
            align = str(input("Vertical/Horizontal(v/h)?"))
            while startCounter<=counter:
                print(startCounter)
                tm.sleep(1)
                startCounter+=1
            if align == 'v':
                for i in range(countMessage):
                    pg.write(message+"\n")
            elif align == 'h':
                for i in range(countMessage):
                    pg.write(message+" ")
        except:
            print("Ada Kesalahan")
        pass

    def autoKey(self):
        try:
            startCounter = 1
            counter = int(input("Masukan Waktu: "))
            key = str(input("Masukan Nama Tombol Keyboard (Contoh: shift):"))
            while startCounter<=counter:
                print(startCounter)
                tm.sleep(1)
                startCounter+=1
            pg.press(key)
        except:
            print("Ada Kesalahan")
        pass

    def mouseMove(self):
        try:
            startCounter = 1
            counter = int(input("Masukan Waktu: "))
            x = int(input("Masukan Kordinat (x): "))
            y = int(input("Masukan Kordinat (y): "))
            klik = str(input("Aktifkan Klik?(y/n): "))
            while startCounter<=counter:
                print(startCounter)
                tm.sleep(1)
                startCounter+=1
            if klik == 'y':
                pg.moveTo(x,y)
                pg.click()
            elif klik == 'n':
                pg.moveTo(x,y)
            else:
                print("Kesalahan Input")
        except:
            print("Ada Kesalahan")
        pass

    def moveApp(self):
        pg.hotkey('alt','tab')

    def Exit(self):
        while True:
            ask = str(input("Apakah VsCode Anda Full Screen? (y/n)"))
            if ask == 'y':
                pg.moveTo(1350,0)
                pg.click()
                break
            elif ask == 'n':
                pg.moveTo(760,10)
                pg.click()
                break
        pass

#instance Object
bh = Behaviour('Auto click','Auto Type','Auto Key','Mouse Auto Move','Move Aplication','Exit')
ask = str(input('Masukan Pilihan: '))
if ask == '1':
    bh.AutoClick()
elif ask == '2':
    bh.AutoType()
elif ask == '3':
    bh.autoKey()
elif ask == '4':
    bh.mouseMove()
elif ask == '5':
    bh.moveApp()
elif ask == '6':
    bh.Exit()
else:
    print("Salah Input :(")
