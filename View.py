from doctest import master
from email.mime import image
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
from turtle import bgcolor
from Biz import *
import hashlib


class Checkbox(ttk.Checkbutton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable = tk.BooleanVar(self)
        self.configure(variable=self.variable)

    def checked(self):
        return self.variable.get()

    def check(self):
        self.variable.set(True)

    def uncheck(self):
        self.variable.set(False)


class Application(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.style = ttk.Style()
        self.style.configure(
            "MyEntry.TEntr", fieldbackground="#000", foreground="#fff", padding=20)
        self.styleC = ttk.Style()
        self.styleC.configure(
            "MyCombobox.TCombobox", fieldbackground="white", foreground="#000", padding=5)
        self.pack()

        self.stylebtn = ttk.Style()
        self.stylebtn.configure("MyButton.TButton",
                                compound=tk.LEFT,
                                padding=-10,
                                highlightbackground="#E3518D",
                                highlightthickness=4,
                                borderwidth=0,
                                font=('Roboto Cn', 8),
                                relief="raised")

        # En caso de imagenes
        self.imgHead = PhotoImage(file="images/head.png")
        self.imgLatizq = PhotoImage(file="images/lateral.png")
        self.imgbot= PhotoImage(file="images/bot.png")
        self.imgGener = PhotoImage(file="images/generalidades.png")

        # imagenes en botones
        self.btnIntro = PhotoImage(file="images/btnIntro.png")
        self.btnFunc = PhotoImage(file="images/btnFunc.png")
        self.btnGener= PhotoImage(file="images/gener.png")
        self.btnFunci = PhotoImage(file="images/func.png")
        self.btnDemo = PhotoImage(file="images/demo.png")

        self.idbtnct = 1

        self.create_widgets()

    # Control del ciclo de operaciones

    def ShowFramebtnInfo(self, frame1, frame2,btn):
        self.HideFrame(frame1)
        btn.configure(state="disabled") 
        frame2.place(x=200, y=100, width=790, height=160)
    
    def ShowFramebtnesBC(self, frame1,btn1,btn2,btn3,tpc):
        self.tpc = tpc
        if self.idbtnct == 1:
            if tpc == 1:
                btn2.configure(state="disabled")
                btn3.configure(state="disabled")
                self.idbtnct = 0
            elif tpc == 2:
                btn1.configure(state="disabled")
                btn3.configure(state="disabled")
                self.idbtnct = 0
            elif tpc == 3:
                btn1.configure(state="disabled")
                btn2.configure(state="disabled")
                self.idbtnct = 0
            else:
                btn3.configure(state="normal")
                btn2.configure(state="normal")
                btn1.configure(state="normal")
            frame1.place(x=200, y=260, width=790, height=390)
        else:
            btn3.configure(state="normal")
            btn2.configure(state="normal")
            btn1.configure(state="normal")
            self.idbtnct = 1       
            frame1.place(x=200, y=260, width=790, height=390)        
    
    def ShowFramebtnes(self, frame1):
        frame1.place(x=200, y=260, width=790, height=390)
            
    def HideLabel(self, label):
        label.place_forget()
    
    def HideFrame(self, frame1):  # Ocultar los widgets por medio de esta función al hacer clic
        frame1.place_forget()

    def TransitionsLabels(self,label1,label2):
        self.HideLabel(label1)
        label2.place(x=0, y=-40, width=590, height=390)



    def cierre(self, son):
        son.withdraw()

    # validación de check
    def check_clicked(self, checkbox):
        print(self.checkbox.checked())

    def browseFiles(self, msg):
        self.filename = filedialog.askopenfilename(
            initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        msg.configure(text="File Opened: " + self.filename)

    def create_widgets(self):

        # Puliendo el diseño de la master
        self.master.title("Sistema de Ordenamiento Bucket Sort")
        self.master.iconbitmap('images\icon.ico')  # Icono de la ventana


# ------->Frame Principal
        self.fwel = Frame(self.master)
        self.fwel.config(bg="#fff")
        self.fwel.place(x=0, y=0, width=200, height=550) 

        # ----->Titulo
        self.labelc = Label(self.master, image=self.imgHead, bg='#2B0D2F')
        self.labelc.place(x=0, y=0, width=890, height=100)      

        # ----->Bordes menu lateral
        self.labelat = Label(self.fwel, bg='#2B0D2F')
        self.labelat.place(x=0, y=100, width=7, height=550)

        self.labelat1 = Label(self.fwel, bg='#2B0D2F')
        self.labelat1.place(x=0, y=100, width=200, height=7)

        self.labelat2 = Label(self.fwel, bg='#2B0D2F')
        self.labelat2.place(x=195, y=100, width=7, height=550)

        # Menu 1
        self.btnIntrod = tk.Button(self.fwel, image=self.btnIntro, compound=tk.LEFT,
                        highlightbackground="#E3518D",
                        highlightthickness=4,
                        borderwidth=0,
                        font=('Roboto Cn', 8),
                        relief="raised", command=lambda: self.ShowFramebtnInfo(self.fwelms, self.fbtnInfo, self.btnIntrod))
        self.btnIntrod["border"] = "0"
        self.btnIntrod.place(x=10, y=200, width=181, height=45)

        # Menu 2
        self.btnFuncc = Button(self.fwel, image=self.btnFunc, compound=tk.LEFT,
                        highlightbackground="#E3518D",
                        highlightthickness=4,
                        borderwidth=0,
                        font=('Roboto Cn', 8),
                        relief="raised", command=lambda: self.ShowFramebtnInfo(self.fwelms, self.ffun, self.btnFuncc))
        self.btnFuncc["border"] = "0"
        self.btnFuncc.place(x=10, y=400, width=181, height=45)

#Frame de bienvenida
        self.fwelms = Frame(self.master)
        self.fwelms.config(bg="#000000")
        self.fwelms.place(x=200, y=100, width=790, height=550)

        lblin1 = Label(self.fwelms, image=self.imgbot,
                bg="black", fg="white", font=("Retro", 14))
        lblin1.place(x=10, y=10)



# Frame de la ventana introducción

        self.fbtnInfo = Frame(self.master)
        self.fbtnInfo.config(bg="#fff")
        self.HideFrame(self.fbtnInfo)

        #Botones de introducción
        self.btnGeneralidades = Button(self.fbtnInfo, image=self.btnGener, compound=tk.LEFT,
                        highlightbackground="#E3518D",
                        highlightthickness=4,                        
                        font=('Roboto Cn', 8),
                        relief="raised", command=lambda: self.ShowFramebtnes(self.fbtnGener))
        self.btnGeneralidades["border"] = "0"
        self.btnGeneralidades.place(x=30, y=60, width=181, height=45)

        self.btnFuncionalidad = Button(self.fbtnInfo, image=self.btnFunci, compound=tk.LEFT,
                        highlightbackground="#E3518D",
                        highlightthickness=4,                        
                        font=('Roboto Cn', 8),
                        relief="raised", command=lambda: self.ShowFramebtnes( self.fbtnFunci))
        self.btnFuncionalidad["border"] = "0"
        self.btnFuncionalidad.place(x=251, y=60, width=181, height=45)

        self.btnDemos= Button(self.fbtnInfo, image=self.btnDemo, compound=tk.LEFT,
                        highlightbackground="#E3518D",
                        highlightthickness=4,                        
                        font=('Roboto Cn', 8),
                        relief="raised", command=lambda: self.ShowFramebtnes( self.fbtnDemo))
        self.btnDemos["border"] = "0"
        self.btnDemos.place(x=481, y=60, width=181, height=45)

        #Separador
        self.labelhor = Label(self.fbtnInfo, bg='#2B0D2F')
        self.labelhor.place(x=0, y=150, width=800, height=4)
        
        

#Frame de la ventana generalidades
        self.fbtnGener = Frame(self.master)
        self.fbtnGener.config(bg="#fff")
        self.HideFrame(self.fbtnGener)

        #Label con generalidades 
        self.labelGener = Label(self.fbtnGener, image=self.imgGener)
        self.labelGener.place(x=0, y=-40, width=590, height=390)
#Frame de la ventana funcionalidad
        self.fbtnFunci = Frame(self.master)
        self.fbtnFunci.config(bg="#fff")
        self.HideFrame(self.fbtnFunci)

        #Label con Funcionalidad --Tipo presentación
        self.labelGener = Label(self.fbtnFunci, image=self.imgGener)
        self.labelGener.place(x=0, y=-40, width=590, height=390)
#Frame de la ventana demostración
        self.fbtnDemo = Frame(self.master)
        self.fbtnDemo.config(bg="#fff")
        self.HideFrame(self.fbtnDemo)


# Frame de la ventana de funcionalidad

        self.ffun = Frame(self.master)
        self.ffun.config(bg="white")
        self.ffun.place(x=200, y=100, width=790, height=550)
        self.HideFrame(self.ffun)

        self.datRand = Checkbox(self.ffun,
                                text="Datos Aleatorios", command=lambda: self.check_clicked(self.datRand))
        self.datRand.place(x=40, y=70)
        self.datArch = Checkbox(self.ffun,
                                text="Datos en archivo", command=lambda: self.check_clicked(self.datArch))
        self.datArch.place(x=40, y=90)

        self.label_file_explorer = Label(self.ffun,
                                        text="File Explorer using Tkinter",
                                        width=100, height=4,
                                        fg="blue")
        self.label_file_explorer.place(x=40, y=120)

        self.button_explore = Button(self.ffun,
                                    text="Browse Files",
                                    command=lambda: self.browseFiles(self.label_file_explorer))
        self.button_explore.place(x=40, y=200)


def main():
    Interfaz = tk.Tk()
    ancho_ventana = 890
    alto_ventana = 550
    x_ventana = Interfaz.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = Interfaz.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    Interfaz.geometry(posicion)
    Interfaz.resizable(0, 0)
    Interfaz.configure(bg="white")
    eject = Application(Interfaz)
    eject.mainloop()


if __name__ == '__main__':
    main()
