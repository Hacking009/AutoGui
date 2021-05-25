import pyautogui as pg
import time as tm

class Behaviour:
    def __init__(self,*menu):
        if __name__=='__main__':
            print('[Author: AlDev]')
        j=1
        for i in menu:
            print([j],i)
            j+=1
        pass

    def AutoClick(self):
        startCounter = 1
        counter = int(input("Masukan Waktu: "))
        while startCounter<=counter:
            print(startCounter)
            tm.sleep(1)
            startCounter+=1
        pg.click()
        pass

    def AutoType(self):
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
        pass

    def autoKey(self):
        startCounter = 1
        counter = int(input("Masukan Waktu: "))
        key = str(input("Masukan Nama Tombol Keyboard (Contoh: shift):"))
        while startCounter<=counter:
            print(startCounter)
            tm.sleep(1)
            startCounter+=1
        pg.press(key)

bh = Behaviour('Auto click','Auto Type','Auto Key')
ask = str(input('Masukan Pilihan: '))
if ask == '1':
    bh.AutoClick()
elif ask == '2':
    bh.AutoType()
elif ask == '3':
    bh.autoKey()