from dis import show_code
from tkinter import *
from tkinter import ttk
import tkinter
from pyparsing import col
import requests
from urllib.request import urlopen
import json

#DEFINIR VARIABLES
color="#80CEE1"
#CONSUMIR API
url = "http://localhost:8080/instrumentos"
response = urlopen(url)
data_json = json.loads(response.read())

def show_frame(frame):
    frame.tkraise()


root = tkinter.Tk()
root.geometry("600x500")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


verInstrumentos = tkinter.Frame(root, bg=color)
agregarInstrumentos = tkinter.Frame(root, bg=color)
editarInstrumentos = tkinter.Frame(root, bg=color)

for frame in (verInstrumentos, agregarInstrumentos, editarInstrumentos):
    frame.grid(row=0, column=0, sticky="nsew")

# ============== VER INSTRUMENTOS (FRAME 1)

frame1_title = tkinter.Label(verInstrumentos, text="Mostrar Instrumentos", bg=color, font="COMIC_SANS 40", anchor="center")
frame1_title.grid(row=0, column=2)

frame1_btn = tkinter.Button(verInstrumentos, text="Agregar Instrumento", command=lambda:show_frame(agregarInstrumentos),width=20, height=2)
frame1_btn.grid(row=2, column=2, pady=10)

frame1_btn2 = tkinter.Button(verInstrumentos, text="Editar Instrumento", command=lambda:show_frame(editarInstrumentos),width=20, height=2)
frame1_btn2.grid(row=3, column=2, pady=10)

frame1_btn3 = tkinter.Button(verInstrumentos, text="Salir", command=root.destroy, width=20, height=2)
frame1_btn3.grid(row=4, column=2, pady=10)

#CREAR TABLA
tv = ttk.Treeview(verInstrumentos, columns=("id","precio","cantidad_stock"))

tv.column("#0", stretch=True, width=180, anchor=CENTER)
tv.column("id", stretch=True,width=100,anchor=CENTER)
tv.column("precio",stretch=True, width=150,anchor=CENTER)
tv.column("cantidad_stock",stretch=True, width=100,anchor=CENTER)


tv.heading("#0", text="Nombre", anchor="center")
tv.heading("id", text="Id", anchor="center")
tv.heading("precio", text="Precio", anchor="center")
tv.heading("cantidad_stock", text="Cantidad Stock", anchor="center")

contador=0
for data in data_json:    
    nombre=data_json[contador]["nombre"]
    id = data_json[contador]["id"]
    precio = data_json[contador]["precio"]
    stock = data_json[contador]["stock"]
    tv.insert("", END, text=nombre, values=(id, precio, stock))
    contador=contador+1
    
tv.grid(row=1, column=2, padx=20)


# ============== AGREGAR INSTURMENTOS (FRAME 2)

frame2_title = tkinter.Label(agregarInstrumentos, text="Agregar Instrumentos", bg=color)
frame2_title.pack(fill="x")

frame2_btn = tkinter.Button(agregarInstrumentos, text="Ver Instrumentos", command=lambda:show_frame(verInstrumentos))
frame2_btn.pack()

frame2_btn2 = tkinter.Button(agregarInstrumentos, text="Editar Instrumentos", command=lambda:show_frame(editarInstrumentos))
frame2_btn2.pack()

frame2_btn3 = tkinter.Button(agregarInstrumentos, text="Salir", command=root.destroy)
frame2_btn3.pack()



# ============== EDITAR INSTRUMENTOS (FRAME 3)

frame3_title = tkinter.Label(editarInstrumentos, text="Editar Instrumentos", bg=color)
frame3_title.pack(fill="x")

frame3_btn = tkinter.Button(editarInstrumentos, text="Ver Instrumento", command=lambda:show_frame(verInstrumentos))
frame3_btn.pack()

frame3_btn2 = tkinter.Button(editarInstrumentos, text="Agregar Instrumento", command=lambda:show_frame(agregarInstrumentos))
frame3_btn2.pack()

frame3_btn3 = tkinter.Button(editarInstrumentos, text="Salir", command=root.destroy)
frame3_btn3.pack()



show_frame(verInstrumentos)
root.mainloop()















































