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
url = "http://localhost:3000/users"
response = urlopen(url)
data_json = json.loads(response.read())

def show_frame(frame):
    frame.tkraise()


root = tkinter.Tk()
root.geometry("750x600")

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
tv = ttk.Treeview(verInstrumentos, columns=("nombre","pais","creado en","modificado en"))

tv.column("#0",stretch=True, width=50,anchor=CENTER)
tv.column("nombre",stretch=True, width=150,anchor=CENTER)
tv.column("pais",stretch=True, width=100,anchor=CENTER)
tv.column("creado en",stretch=True, width=150,anchor=CENTER)
tv.column("modificado en",stretch=True, width=150,anchor=CENTER)

tv.heading("#0", text="Id", anchor="center")
tv.heading("nombre", text="Nombre", anchor="center")
tv.heading("pais", text="Pais", anchor="center")
tv.heading("creado en", text="Fecha Creación", anchor="center")
tv.heading("modificado en", text="Fecha Modificación", anchor="center")

tv.column("#0", anchor="center")

contador=0
for data in data_json:    
    nombre=data_json[contador]["name"]
    id=data_json[contador]["id"]
    country=data_json[contador]["country"]
    created_at=data_json[contador]["created_at"]
    updated_at=data_json[contador]["updated_at"]
    tv.insert("", END, text=id, values=(nombre, country, created_at, updated_at))
    contador=contador+1
    
tv.grid(row=1, column=2, padx=20)


# ============== AGREGAR INSTURMENTOS (FRAME 2)

nombreEntry = ttk.Entry(agregarInstrumentos)
idEntry = ttk.Entry(agregarInstrumentos)
paisEntry = ttk.Entry(agregarInstrumentos)

frame2_title = tkinter.Label(agregarInstrumentos, text="Agregar Instrumentos", bg=color, font="COMIC_SANS 40", anchor="center")
frame2_title.grid(row = 0, column= 2)

nombreEntry.grid(row = 1, column= 2)
idEntry.grid(row = 1, column= 3)
paisEntry.grid(row = 1, column= 4)

frame2_btn = tkinter.Button(agregarInstrumentos, text="Ver Instrumentos", command=lambda:show_frame(verInstrumentos))
frame2_btn.grid(row=2, column=2, pady=10)

frame2_btn2 = tkinter.Button(agregarInstrumentos, text="Editar Instrumentos", command=lambda:show_frame(editarInstrumentos))
frame2_btn2.grid(row=3, column=2, pady=10)

frame2_btn3 = tkinter.Button(agregarInstrumentos, text="Salir", command=root.destroy)
frame2_btn3.grid(row=4, column=2, pady=10)



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















































