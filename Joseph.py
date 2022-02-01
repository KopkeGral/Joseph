#İmporting libraries and modules
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import datetime as dt
import random
import webbrowser as wb
import os
import time
from tkinter import *
from tkcalendar import DateEntry
from Functions_and_others import *
from googletrans import Translator
translator = Translator()

master = Tk()
master.title("Joseph")
master.geometry("750x450")
master.minsize(750,450)
master.iconbitmap("josephico.ico")

MenuBar = Menu(master)

komutlar = Menu(MenuBar, tearoff=0)
komutlar.add_command(label="Selam", command=selamla)
komutlar.add_command(label="Espri", command=espriypa)
komutlar.add_command(label="Oyunlar", command=games)
komutlar.add_command(label="Sosyal Medya", command=create_window_media)
komutlar.add_command(label="Uygulamalar", command=create_window_apps)
komutlar.add_command(label="Çeviri", command=ceviri)
komutlar.add_command(label="Wikipedia", command=start_wikipedia)
komutlar.add_command(label="Hesap Makinesi", command=calculator)
komutlar.add_separator()
komutlar.add_command(label="Bilgisayar İşlemleri", command=computer_os)
MenuBar.add_cascade(label="Komutlar", menu=komutlar)

kullanıcı = Menu(MenuBar, tearoff=0)
kullanıcı.add_command(label="Not defteri", command=startlist)

MenuBar.add_cascade(label="Kullanıcı İşlemleri", menu=kullanıcı)

master.config(menu=MenuBar)

frame_radio = Frame(master, bg="#d9d9d9")
frame_radio.place(relx=0.05, rely=0.05, relwidth=0.3, relheight=0.8)

frame_search = Frame(master, bg="#d9d9d9")
frame_search.place(relx=0.65, rely=0.05, relwidth=0.3, relheight=0.8)

frame_center = Frame(master)
frame_center.place(relx=0.35, rely=0.05, relwidth=0.3, relheight=0.8)


canvas = Canvas(master, height=450, width=750)
canvas.pack()

zaman = ""
    
entry = Entry(frame_search, bg="gray", border=2)
entry.place(relx=0.05, rely=0.35, relwidth=0.7, relheight=0.05)

tiktaK = Label(canvas, font=("times",15,"bold"))
tiktaK.grid()

tarihim = Label(canvas, font=("times",15,"bold"))
tarihim.grid(pady=10)

Button(frame_radio, text="Selam", font=("times","12","bold"), command=selamla, bg="#00f000").place(rely=0.05, relx=0.5, relwidth=0.8, relheight=0.06, anchor=CENTER)
Button(frame_radio, text="Espri", font=("times","12","bold"), command=espriypa, bg="#00f000").place(rely=0.15, relx=0.5, relwidth=0.8, relheight=0.06, anchor=CENTER)
Button(frame_radio, text="Oyunlar", font=("times","12","bold"), command=games, bg="#00f000").place(rely=0.25, relx=0.5, relwidth=0.8, relheight=0.06, anchor=CENTER)
Button(frame_radio, text="Sosyal Medya", font=("times","12","bold"), command=create_window_media, bg="#00f000").place(rely=0.35, relx=0.5, relwidth=0.8, relheight=0.06, anchor=CENTER)
Button(frame_radio, text="Uygulamalar", font=("times","12","bold"), command=create_window_apps, bg="#00f000").place(rely=0.45, relx=0.5, relwidth=0.8, relheight=0.06, anchor=CENTER)
Button(frame_radio, text="Çeviri", font=("times","12","bold"), command=ceviri, bg="#00f000").place(rely=0.55, relx=0.5, relwidth=0.8, relheight=0.06, anchor=CENTER)
Button(frame_radio, text="Wikipedia", font=("times","12","bold"), command=start_wikipedia, bg="#00f000").place(rely=0.65, relx=0.5, relwidth=0.8, relheight=0.06, anchor=CENTER)
Button(frame_radio, text="Hesap Makinesi", font=("times","12","bold"), command=calculator, bg="#00f000").place(rely=0.75, relx=0.5, relwidth=0.8, relheight=0.06, anchor=CENTER)
Button(frame_radio, text="Bilgisayar İşlemleri", font=("times","12","bold"), command=computer_os, bg="red").place(rely=0.93, relx=0.5, relwidth=0.65, relheight=0.06, anchor=CENTER)

def saat():
    global zaman

    zaman2 = time.strftime("%H:%M:%S")
    zaman = zaman2
    tiktaK.config(text=zaman)
    tiktaK.after(50, saat)

def tarih():
    global bugun
    global bugun_tarih

    bugun = dt.date.today()
    bugun_tarih = bugun.strftime("%d/%m/%Y")
    tarihim.config(text=bugun_tarih)
    tarihim.after(200, tarih)

var = IntVar()

def arakomutu():
    if butonvar.get() == 0:
        messagebox.showerror("Hata","Lütfen bir arama alanı seçiniz.")
    if entry.get() == "":
        messagebox.showerror("Hata","Lütfen bir arama anahtar kelimesini giriniz.")
    if butonvar.get() == 1:
        google_ara(entry.get())
    if butonvar.get() == 2:
        youtube_ara(entry.get())
    if butonvar.get() == 3:
        work(entry.get())
        

butonvar = IntVar()


Radio1 = Radiobutton(frame_search, text="", variable=butonvar, value=1, bg="#d9d9d9", font="Vertana 8")
Radio1.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.07)

Label(frame_search, text="Google Arama", bg="#d9d9d9", font="Vertana 10 bold").place(relx=0.15, rely=0.05)

Radio2 = Radiobutton(frame_search, text="", variable=butonvar, value=2, bg="#d9d9d9", font="Vertana 8")
Radio2.place(relx=0.05, rely=0.15, relwidth=0.1, relheight=0.07)

Label(frame_search, text="Youtube Arama", bg="#d9d9d9", font="Vertana 10 bold").place(relx=0.15, rely=0.15)

Radio3 = Radiobutton(frame_search, text="", variable=butonvar, value=3, bg="#d9d9d9", font="Vertana 8")
Radio3.place(relx=0.05, rely=0.25, relwidth=0.1, relheight=0.07)

Label(frame_search, text="Siteye Git", bg="#d9d9d9", font="Vertana 10 bold").place(relx=0.15, rely=0.25)


Button1 = Button(frame_search, text="Arat", command= arakomutu, bg="yellow")
Button1.place(rely=0.9, relx=0.3, relwidth=0.4, relheight=0.07)



def kapatma():
    if messagebox.askokcancel("Çıkış", "Uygulamadan çıkmak istiyor musunuz?"):
        master.destroy()

master.protocol("WM_DELETE_WINDOW", kapatma)


saat()
tarih()

master.mainloop()