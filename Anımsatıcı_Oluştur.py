import os
from openpyxl import *

try:
    wb = load_workbook("Anımsatıcılar.xlsx")
    sheet = wb.active

    zaman = input("Saat:Dakika şeklinde giriş yapınız: ")
    slot = int(input("Zamanlayıcı kaçıncı slota yerleştirilsin? (1-10): "))
    if slot > 10:
        slot = 10
    hour_sheet = "A{}".format(slot)
    minute_sheet = "B{}".format(slot)
    zaman = zaman.split(":")
    saat = zaman[0]
    dakika = zaman[1]
    saat = int(saat)
    dakika = int(dakika)
    if saat > 24:
        raise SyntaxError("Saat 24'den büyük olamaz.")
    if dakika > 59:
        raise SyntaxError("Dakika 60'dan büyük olamaz.")

    

    sheet[hour_sheet] = saat
    sheet[minute_sheet] = dakika

    os.remove("Anımsatıcılar.xlsx")
    wb.save("Anımsatıcılar.xlsx")

    
except ValueError:
    print("Bir hata oluştu...")
    exit()
except IndexError:
    print("Bir hata oluştu...")
    exit()