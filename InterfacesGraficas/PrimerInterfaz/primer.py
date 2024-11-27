#creando primer interfaz grafica gracias a la libreria tkinter
#en caso de no tener instalada esta libreria en la terminal poner
#pip intall tkinter
import tkinter as tk


ventana = tk.Tk()

ventana.title("mi primer ventana")

ventana.geometry("500x300")

etiqueta  = tk.Label(ventana,text="esto es un texto")

etiqueta.pack(pady=100)

ventana.mainloop()