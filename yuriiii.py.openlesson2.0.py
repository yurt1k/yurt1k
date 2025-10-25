from PIL import Image
from customtkinter import *
from socket import*


def chat_win():
    win1 = CTk()
    win1.geometry("400x600")
    win1.title("Chatrix")
    win1.configure(fg_color="seashell3")

    entr = CTkEntry(win1, placeholder_text="your text", width=320, height=60, border_width=3, font=("Segoe UI",20,"bold"))
    entr.place(x=1, y=540)

    btn3 = CTkButton(win1 ,text="⚡", fg_color="darkgrey", font=("Segoe UI",50,"bold"),width=95, height=60, text_color="grey",border_width=3, corner_radius=10)
    btn3.place(x=310, y=530)

    text_area = CTkTextbox(win1, width=350, height=400,fg_color="seashell3")
    text_area.place(x=0, y=140)
    text_area.lower()

    if btn.cget("text"):
        btn2 = CTkButton(win1, width=100, height=150, fg_color="transparent", font=("Segoe UI", 15, "bold"), text=entry5.get(),
                         border_width=2, corner_radius=5, hover_color="seashell3", border_color="antiquewhite")
        btn2.place(x=-5, y=-3)

    win1.mainloop()

win = CTk()
win.geometry("400x600")
win.configure(fg_color="seashell3")
win.title("Chatrix")


label = CTkLabel(win, text="Nickname", font=("Segoe UI",25,"bold"),fg_color="grey")
label.place(x=240,y=50)
entry5 = CTkEntry(win, placeholder_text="Nickname", border_width=0,  corner_radius=0, height=22)
entry5.place(x=240, y=83)


label1 = CTkLabel(win, text="Host", font=("Segoe UI",25,"bold"),fg_color="grey")
label1.place(x=270,y=120)
entry1 = CTkEntry(win, placeholder_text="Host", border_width=0,  corner_radius=0, height=22)
entry1.place(x=240, y=150)


label2 = CTkLabel(win, text="Port", font=("Arial",25,"bold"),fg_color="grey")
label2.place(x=273,y=190)
entry2 = CTkEntry(win, placeholder_text="Port", border_width=0,  corner_radius=0, height=22)
entry2.place(x=240, y=220)







btn = CTkButton(win, hover_color="grey", width= 300, height= 200, fg_color="grey",text="Enter!", font=("Segoe UI",35,"bold"), command=chat_win,border_width=4, corner_radius=10)
btn.place(x=50, y=350)




btn6 = CTkButton(win, width=208, height=258, fg_color="grey", border_width=3, text="")
btn6.place(x=10, y=15)


img = Image.open("download.jpg")
image_ctk = CTkImage(light_image=img, size=(200, 250))

label6 = CTkLabel(win, image= image_ctk, text="",)
label6.pack(pady=10)
label6.place(x=14, y=19)


label7 = CTkLabel(win, text="Chatrix", text_color="grey", font=("Segoe UI", 25,"bold") )
label7.place(x=265, y=10)


btn5 = CTkButton(win, width=160, height=210, fg_color="grey", border_width=3, text="", hover_color="grey",  corner_radius=10)
btn5.lower()
btn5.place(x=230, y=47)




win.mainloop()