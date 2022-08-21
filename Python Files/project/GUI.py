from tkinter import *

# from tkinter import *
from pytube import YouTube

win = Tk()
win.geometry("420x320")
win.title("Youtube video Downloader")

# logo = PhotoImage(file="logo.jpg")
# win.iconphoto(False,logo)

Label(win,text='video downloader',font=('Arial 20 bold'),bg="lightgreen").pack(padx=5,pady=50)

v_link = StringVar()
Label(win,text='Enter the link: ',font=("Arial",20,"bold")).place(x=120,y=110)
Entry_link = Entry(win,width=34,font=20,textvariable=v_link,bd=4).place(x=20,y=150)

def v_download():
    v_url = YouTube(str(v_link.get()))
    videos = v_url.streams.first()
    videos.download()
    Label(win,text="Download completed...",font=("Arial",18,"bold"),bg="lightyellow",fg="black").place(x=100,y=250)
    Label(win,text="Check out your download video in the folder.....").place(x=100,y=300)
    
    
    
Button(win,text="Download",font=("Arial",20,"bold"),bg="lightgrey",command=v_download).place(x=140,y=200)

win.mainloop()
