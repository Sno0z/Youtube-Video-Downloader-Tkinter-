from tkinter import *
from pytube import YouTube

# creation of the window
fenetre = Tk()
fenetre.title("Youtube Video Downloader")
fenetre.geometry("720x480")
fenetre.minsize(720, 480)
fenetre.maxsize(720, 480)
fenetre.config(background="#e80a0a")

# creation of the button's functions

def get_link():
    value=saisir.get()
    yt = YouTube(value)
    yt_title = yt.title
    print("You can download it...", yt_title)
    consigne_text.config(text=yt_title, font=("Ubuntu", 18))

def download():
    Téléchargement = "Downloading"
    consigne_text.config(text=Téléchargement, font=("Ubuntu", 18))
    value=saisir.get()
    yt = YouTube(value)
    yt_title = yt.title
    end_téléchargement = "Download Complete !"
    ys = yt.streams.get_highest_resolution()
    yt = ys.download()
    consigne_text.config(text=end_téléchargement, font=("Ubuntu", 18))

# window parameter

title = Label(fenetre, text="YOUTUBE VIDEO DOWNLOADER", font=("Couriel 24 underline bold"), bg="#e80a0a", fg="#f5f5f5")
title.pack()

logo = PhotoImage(file="youtube_logo.png")
label_logo = Label(image=logo, bg="#e80a0a")
label_logo.pack(anchor ='center')

consigne_text = Label(fenetre, text="Enter URL : ", font=("Ubuntu", 18), bg="#e80a0a", fg="#ffffff")
consigne_text.pack(anchor ='center')


saisir=StringVar() 
saisie=Entry(textvariable=saisir,justify=CENTER, bd=1, width=40)
saisie.pack() 
valid_button = Button(fenetre, text="Submit", font=("Ubuntu", 14), fg= "#e80a0a", bg="#ffffff", command=get_link)
valid_button.pack(anchor ='center')


download_button = Button(fenetre, text="Download", font=("Ubuntu", 14), fg="#e80a0a", bg="#ffffff", command=download)
download_button.pack(side = BOTTOM)


fenetre.mainloop()
