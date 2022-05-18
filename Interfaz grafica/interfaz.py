from dis import show_code
from tkinter import *
from tkinter import ttk
import tkinter
from pyparsing import col
import requests
from urllib.request import urlcleanup, urlopen
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
# root.resizable(False, False)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


verInstrumentos = tkinter.Frame(root, bg=color)
agregarInstrumentos = tkinter.Frame(root, bg=color)
editarInstrumentos = tkinter.Frame(root, bg=color)

for frame in (verInstrumentos, agregarInstrumentos, editarInstrumentos):
    frame.grid(row=0, column=0, sticky="nsew")

# ============== VER INSTRUMENTOS (FRAME 1)

def fn_refresh():
    contador=0
    for i in tv.get_children():
        tv.delete(i)
        
    response = urlopen(url)
    data_json = json.loads(response.read())    
    
    for i in data_json:    
        nombre=i["name"]
        id=i["id"]
        country=i["country"]
        created_at=i["created_at"]
        updated_at=i["updated_at"]
        tv.insert("", END, text=id, values=(nombre, country, created_at, updated_at))
        contador=contador+1
        
    verInstrumentos.update()


    

refreshBtn = tkinter.Button(verInstrumentos, text="Refrescar Tabla", command=lambda:fn_refresh())
refreshBtn.grid(row=5, column=2, pady=10)


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


datos = {}



#VARIABLES PARA ALMACENAR DATOS DE LOS INPUTS
idVariable = tkinter.StringVar()
nomVariable = tkinter.StringVar()
paisVariable = tkinter.StringVar()

#FUNCION BOTON POST
def fn_post():
    # print(f'esto es id: {idVariable.get()}, esto es nombre: {nomVariable.get()}, esto es pais: {paisVariable.get()}')
    datos = {'id' : idVariable.get(), 'name':nomVariable.get(),  'country': paisVariable.get()}
    requests.post(url, json=datos)


#CREAR LOS INPUTS
idEntry = ttk.Entry(agregarInstrumentos,textvariable = idVariable)
nombreEntry = ttk.Entry(agregarInstrumentos, textvariable = nomVariable)
paisEntry = ttk.Entry(agregarInstrumentos,textvariable =  paisVariable)


#BOTON DE POST
postBtn = tkinter.Button(agregarInstrumentos, text="Agregar", command=lambda:fn_post())
postBtn.place(x = 400, y = 120)

#CREAR BOTONES DE NAVEGACIÓN
frame2_btn = tkinter.Button(agregarInstrumentos, text="Ver Instrumentos", command=lambda:show_frame(verInstrumentos))
frame2_btn2 = tkinter.Button(agregarInstrumentos, text="Editar Instrumentos", command=lambda:show_frame(editarInstrumentos))
frame2_btn3 = tkinter.Button(agregarInstrumentos, text="Salir", command=root.destroy)


#CREAR LABELS DE LOS INPUTS
idLabel = tkinter.Label(agregarInstrumentos, text= "ID", bg=color, font="COMIC_SANS 12", anchor="center")
nomLabel = tkinter.Label(agregarInstrumentos, text= "NOMBRE", bg=color, font="COMIC_SANS 12", anchor="center")
paisLabel = tkinter.Label(agregarInstrumentos, text= "PAIS", bg=color, font="COMIC_SANS 12", anchor="center")
frame2_title = tkinter.Label(agregarInstrumentos, text="Agregar Instrumentos", bg=color, font="COMIC_SANS 40", anchor="center")


#POSICIONAR LABELS
frame2_title.place(x = 80, y = 0)
idLabel.place(x = 100, y = 90)
nomLabel.place(x = 160, y = 90)
paisLabel.place(x = 270, y = 90)

#POSICIONAR INPUTS
idEntry.place(x = 100, y =  120, width=50)
nombreEntry.place(x = 160, y =  120, width=100)
paisEntry.place(x = 270, y =  120, width=100)


#POSICIONAR BOTONES DE NAVEGACIÓN
frame2_btn.place(x = 180, y = 150)
frame2_btn2.place(x = 180, y = 190)
frame2_btn3.place(x = 220, y = 230)



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















































