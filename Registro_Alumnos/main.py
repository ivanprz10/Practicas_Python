#INTERFAZ GRAFICA HACIENDO USO DE LIBRERIAS COMO TKINTER, MYSQL.CONNECTOR, BARCODE, QRCODE, PIL
#Este proyecto trata de obtener los datos de los alumnos de una universidad como nombre, apellidos,
#numero de control, tipo de sangre, numero de seguro social, contacto de emergencia, y carrera
#una vez recabado esta informacion y siendo guardada exitosamente, nos generara codigos qr y 
#codigos de barras en base a el numero de control del alumno
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image, ImageTk


def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Examen0202",
        database="registro_alumnos"
    )

# Esta funcion se ejecutara cuando demos clic en el boton guardar, esta accion realizara el guardado de 
#alumnos asi como generar los codigos de barras y los codigos qr en formato jpg
def guardar_alumno():
    #cuando demos clic lo primero que realizara recabar los datos de nuestros forms por el ".get"
    nombre = entry_nombre.get()
    apellidop = entry_apellidop.get()
    apellidom = entry_apellidom.get()
    numero_control = entry_numero_control.get()
    sangre = entry_sangre.get()
    nss = entry_nss.get()
    contactoem = entry_contactoem.get()
    carrera = entry_carrera.get()

    #con esta condicion indicaremos y analizara todos y cada uno de los campos de nuestra GUI
    #en caso de que un campo este vacio nos mandara un mensaje de error todos los campos son obligatorios
    if not nombre or not apellidom or not apellidop or not sangre or not nss or not contactoem or not numero_control or not carrera:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    
    try:#gracias a este metodo de excepciones, detectaremos cualquier anomalia tipo mysql, en caso que suceda un error de tipo conexion
        #nos mandara al "except" mostrando un caja de mensaje con un error
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Alumnos (nombre, apellidop, apellidom, numero_control, tipo_sangre, nss, contacto_emergencia, carrera) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                       (nombre, apellidop, apellidom, numero_control, sangre, nss, contactoem, carrera))#realizamos la consulta correspondiente
                                                                                                        #para mandar los datos a nuestra BD
        conexion.commit()
        cursor.close()
        conexion.close()
        
        # Mandamos a llamar a nuestras funciones para generar codigo qr y barras de alumno
        generar_qr(numero_control)#QR
        generar_codigo_barras(numero_control)#barras

        messagebox.showinfo("Éxito", f"Alumno {nombre} registrado correctamente")#en caso de tener un registro exitoso se mostrara el mensaje en pantalla
        limpiar_campos()#y ejecutara la funcion para limpiar campos 
    except mysql.connector.Error as err:#metodo de excepcion en caso de error en la ejecucion
        messagebox.showerror("Error de BD", f"Ocurrió un error: {err}")

# Función para generar QR
def generar_qr(numero_control):
    qr = qrcode.make(f"Número de Control: {numero_control}")
    qr.save(f"{numero_control}_qr.png")

# Función para generar código de barras
def generar_codigo_barras(numero_control):
    codigo = Code128(numero_control, writer=ImageWriter())
    codigo.save(f"{numero_control}_barcode")

# Función para limpiar campos es decir limpiar
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellidop.delete(0, tk.END)
    entry_apellidom.delete(0, tk.END)
    entry_numero_control.delete(0, tk.END)
    entry_sangre.delete(0, tk.END)
    entry_nss.delete(0, tk.END)
    entry_contactoem.delete(0, tk.END)
    entry_carrera.delete(0, tk.END)
    

# Interfaz gráfica con Tkinter la libreria TKINTER
ventana = tk.Tk()
ventana.title("Registro de Alumnos")
ventana.geometry("700x500")

# Etiquetas y entradas
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Apellido.P:").grid(row=1, column=0, padx=10, pady=10)
entry_apellidop = tk.Entry(ventana)
entry_apellidop.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Apellido.M:").grid(row=2, column=0, padx=10, pady=10)
entry_apellidom = tk.Entry(ventana)
entry_apellidom.grid(row=2, column=1, padx=10, pady=10)

tk.Label(ventana, text="Numero de control:").grid(row=3, column=0, padx=10, pady=10)
entry_numero_control = tk.Entry(ventana)
entry_numero_control.grid(row=3, column=1, padx=10, pady=10)

tk.Label(ventana, text="tipo de sangre:").grid(row=4, column=0, padx=10, pady=10)
entry_sangre = tk.Entry(ventana)
entry_sangre.grid(row=4, column=1, padx=10, pady=10)

tk.Label(ventana, text="NSS:").grid(row=5, column=0, padx=10, pady=10)
entry_nss = tk.Entry(ventana)
entry_nss.grid(row=5, column=1, padx=10, pady=10)

tk.Label(ventana, text="Contacto emergencia:").grid(row=6, column=0, padx=10, pady=10)
entry_contactoem = tk.Entry(ventana)
entry_contactoem.grid(row=6, column=1, padx=10, pady=10)

tk.Label(ventana, text="Carrera:").grid(row=7, column=0, padx=10, pady=10)
entry_carrera = tk.Entry(ventana)
entry_carrera.grid(row=7, column=1, padx=10, pady=10)

# Botón para guardar
btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_alumno)
btn_guardar.grid(row=8, column=0, columnspan=2, pady=20)
# Botón para guardar
btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_alumno)
btn_guardar.grid(row=8, column=1, columnspan=2, pady=20)


ventana.mainloop()
