from tkinter import *
import tkinter.messagebox as tmsg
import os
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("ShortWiki")
root.geometry("755x453+350+180")
root.config(bg="white")
data = ""
data1 = StringVar()
data1.set("")
first_var = StringVar()
first_var.set("")
def search():

    url="https://www.wikipedia.org"
    try:
        page=requests.get(url)
        if page.status_code==200:
            print('success')
        else:
            print('error',page.status_code)
            print('please check url address')
    except Exception as e:
        print(e)
        print('net not working or add wrong')

    soup = BeautifulSoup(page.text,'lxml')
    #x=input("enter to search")
    x=first_var.get()
    ff=x.replace(" ","_")
    v="https://en.wikipedia.org/wiki/"
    pp=v+ff
    print(pp)
    try:
        page1=requests.get(pp)
        if page1.status_code==200:
            print('success')
        else:
            print('error',page1.status_code)
            print('please check url address')
    except Exception as e:
        print(e)
        print('net not working or add wrong')
    soup1= BeautifulSoup(page1.text,'lxml')
    cc=soup1.find('p',class_="")
    first_var.set("")
    data = cc.text
    T.insert(END, "\n\n")
    T.insert(END,data)


def back():
    T.delete('1.0', END)


f1 = Frame(root,bg="#c5dde3",relief=SUNKEN,borderwidth=6, width = 300,)
f1.pack(side="top", fill="x")

f2=Frame(root,bg="#c5dde3",borderwidth=6,relief=SUNKEN, width = 300)
f2.pack(side="bottom", fill="x")

def Exit():
    exit()
l2=Button(f1,text="Window",bg="#db9995",font=('Comic Sans MS',10,'bold'))
l2.pack(side="left",padx=5,fill="x")
l2=Button(f1,text="Category",bg="#db9995",font=('Comic Sans MS',10,'bold'))
l2.pack(side="left",padx=5,fill="x")
l2=Button(f1,text="Setting",bg="#db9995",font=('Comic Sans MS',10,'bold'))
l2.pack(side="left",padx=5,fill="x")
l2=Button(f1,text="Configure",bg="#db9995",font=('Comic Sans MS',10,'bold'))
l2.pack(side="left",padx=5)
l2=Button(f2,text="BACK",bg="green",font=('Comic Sans MS',10,'bold'), width = 20,command = back)
l2.pack(side="left",pady=1,fill="x")
l2=Button(f2,text="Confirm",bg="green",font=('Comic Sans MS',10,'bold'), width = 20,command = search)
l2.pack(side="right",pady=1,fill="x")
l2=Button(f2,text="EXIT",bg="#de0f0b",font=('Comic Sans MS',10,'bold'), width = 20, command = exit)
l2.pack(side="bottom",pady=1)
text=Entry(root,borderwidth=2,bg = "#7e93ab",font=('Comic Sans MS',15,'bold'),textvariable=first_var, width = 300)
text.pack(side="top",padx=5,fill = "both")

S = Scrollbar(root)
T = Text(root, height=40, width=30,font=('Courier New',15,'bold'))
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.pack(side = "top", padx = 1, fill = "both")
S.pack(side=RIGHT, fill=Y)

#T.insert(END, data)



root.mainloop()
