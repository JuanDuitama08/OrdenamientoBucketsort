import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, ttk
from wsgiref import validate

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Vista de árbol en Tkinter")
        self.treeview = ttk.Treeview(self, columns=())
        self.treeview.heading("#0", text="Numero de datos de inicio")        


        #Cantidad de datos a elegir
        self.item = self.treeview.insert("", tk.END, text="1000",tags=("mytag",))
        self.item = self.treeview.insert("", tk.END, text="1500",tags=("mytag",))
        self.item = self.treeview.insert("", tk.END, text="2500",tags=("mytag",))   
        self.item = self.treeview.insert("", tk.END, text="5000",tags=("mytag",))
        self.item = self.treeview.insert("", tk.END, text="Otro:",tags=("mytag",))          
        self.treeview.pack()
        self.pack()

        self.treeview.tag_bind("mytag", "<<TreeviewSelect>>",self.item_selected) 
    def item_selected(self, event):
        try:
            # Obtener el ID del primer elemento seleccionado.
            item = self.treeview.selection()[0]
        except IndexError:
            # Si la tupla está vacía, entonces no hay ningún
            # elemento seleccionado.
            messagebox.showwarning(
                message="Debe seleccionar un elemento.",
                title="No hay selección"
            )
        else:
            #Item seleccionado
            self.text = self.treeview.item(item, option="text")
            if self.text == "Otro:":
                self.otroItem = ttk.Entry()
                self.otroItem.pack(after=self.treeview)
                self.pack()
                self.text = self.otroItem.get()
            
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()