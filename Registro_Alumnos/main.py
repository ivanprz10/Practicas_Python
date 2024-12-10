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
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONALIDAD DE BOTON GUARDAR--------------------------------------------------------------------------------------------------------------------------------------------------------------
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
        generar_qr(numero_control,nombre, apellidop, apellidom, sangre, nss, contactoem, carrera)#QR
        generar_codigo_barras(numero_control,nombre)#barras

        messagebox.showinfo("Éxito", f"Alumno {nombre} registrado correctamente")#en caso de tener un registro exitoso se mostrara el mensaje en pantalla
        limpiar_campos()#y ejecutara la funcion para limpiar campos 
    except mysql.connector.Error as err:#metodo de excepcion en caso de error en la ejecucion
        messagebox.showerror("Error de BD", f"Ocurrió un error: {err}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONALIDAD DE BOTON BUSCAR-------------------------------------------------------------------------------------------------------------------------------------------------------
def buscar_alumno():
     # Obtener el número de control del campo de entrada
    numero_control = entry_numero_control.get()

    # Validar que se haya ingresado un número de control
    if not numero_control:
        messagebox.showerror("Error", "Por favor, ingresa el número de control para buscar")
        return

    try:
        # Conectar a la base de datos
        conexion = conectar_db()
        cursor = conexion.cursor()

        # Ejecutar la consulta para buscar al alumno
        cursor.execute("SELECT nombre, apellidop, apellidom, tipo_sangre, nss, contacto_emergencia, carrera FROM Alumnos WHERE numero_control = %s", (numero_control,))
        resultado = cursor.fetchone()

        # Cerrar la conexión
        cursor.close()
        conexion.close()

        # Validar si se encontró un resultado
        if resultado:
            # Mostrar los datos en los campos correspondientes
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, resultado[0])

            entry_apellidop.delete(0, tk.END)
            entry_apellidop.insert(0, resultado[1])

            entry_apellidom.delete(0, tk.END)
            entry_apellidom.insert(0, resultado[2])

            entry_sangre.delete(0, tk.END)
            entry_sangre.insert(0, resultado[3])

            entry_nss.delete(0, tk.END)
            entry_nss.insert(0, resultado[4])

            entry_contactoem.delete(0, tk.END)
            entry_contactoem.insert(0, resultado[5])

            entry_carrera.delete(0, tk.END)
            entry_carrera.insert(0, resultado[6])

            messagebox.showinfo("Éxito", "Alumno encontrado correctamente")
        else:
            # Si no se encuentra el alumno, limpiar los campos y mostrar un mensaje
            limpiar_campos()
            messagebox.showwarning("Sin resultados", "No se encontró un alumno con ese número de control")

    except mysql.connector.Error as err:
        messagebox.showerror("Error de BD", f"Ocurrió un error: {err}")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONALIDAD DE BOTON ELIMINAR-------------------------------------------------------------------------------------------------------------------------------------------------------

def eliminar_alumno():
    # Obtener el número de control del campo de entrada
    numero_control = entry_numero_control.get()

    # Validar que se haya ingresado un número de control
    if not numero_control:
        messagebox.showerror("Error", "Por favor, ingresa el número de control para eliminar")
        return

    try:
        # Conectar a la base de datos
        conexion = conectar_db()
        cursor = conexion.cursor()

        # Ejecutar la consulta para verificar si el alumno existe
        cursor.execute("SELECT * FROM Alumnos WHERE numero_control = %s", (numero_control,))
        resultado = cursor.fetchone()

        # Validar si se encontró el registro
        if resultado:
            # Preguntar al usuario si está seguro de eliminar el registro
            respuesta = messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar al alumno con número de control {numero_control}?")
            
            if respuesta:
                # Ejecutar la consulta para eliminar el registro
                cursor.execute("DELETE FROM Alumnos WHERE numero_control = %s", (numero_control,))
                conexion.commit()

                # Mostrar mensaje de éxito
                messagebox.showinfo("Éxito", f"Alumno con número de control {numero_control} eliminado correctamente")
                limpiar_campos()
        else:
            messagebox.showwarning("Sin resultados", "No se encontró un alumno con ese número de control")
        
        # Cerrar la conexión
        cursor.close()
        conexion.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error de BD", f"Ocurrió un error: {err}")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONALIDAD DE BOTON MODIFICAR-------------------------------------------------------------------------------------------------------------------------------------------------------

def modificar_alumno():
    nombre = entry_nombre.get()
    apellidop = entry_apellidop.get()
    apellidom = entry_apellidom.get()
    numero_control = entry_numero_control.get()
    sangre = entry_sangre.get()
    nss = entry_nss.get()
    contactoem = entry_contactoem.get()
    carrera = entry_carrera.get()

    # Validar que el número de control esté ingresado
    if not numero_control:
        messagebox.showerror("Error", "Por favor, ingresa el número de control para modificar")
        return

    # Validar que todos los campos estén llenos
    if not nombre or not apellidop or not apellidom or not sangre or not nss or not contactoem or not carrera:
        messagebox.showerror("Error", "Todos los campos son obligatorios para modificar")
        return

    try:
        # Conectar a la base de datos
        conexion = conectar_db()
        cursor = conexion.cursor()

        # Verificar si el alumno existe
        cursor.execute("SELECT * FROM Alumnos WHERE numero_control = %s", (numero_control,))
        resultado = cursor.fetchone()

        if resultado:
            # Confirmar que se desea realizar la modificación
            respuesta = messagebox.askyesno(
                "Confirmar", 
                f"¿Estás seguro de modificar los datos del alumno con número de control {numero_control}?"
            )

            if respuesta:
                # Actualizar los datos del alumno
                cursor.execute("""
                    UPDATE Alumnos 
                    SET nombre = %s, apellidop = %s, apellidom = %s, tipo_sangre = %s, 
                        nss = %s, contacto_emergencia = %s, carrera = %s 
                    WHERE numero_control = %s
                """, (nombre, apellidop, apellidom, sangre, nss, contactoem, carrera, numero_control))
                
                conexion.commit()

                # Mensaje de éxito
                messagebox.showinfo("Éxito", f"Datos del alumno con número de control {numero_control} actualizados correctamente")
                limpiar_campos()
        else:
            # Si no se encuentra el alumno, mostrar un mensaje
            messagebox.showwarning("Sin resultados", "No se encontró un alumno con ese número de control")

        # Cerrar la conexión
        cursor.close()
        conexion.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error de BD", f"Ocurrió un error: {err}")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#GENERAR CREDENCIAL EN UNA NUEVA VENTANA----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_credencial():
    numero_control = entry_numero_control.get()

    # Validar que se haya ingresado un número de control
    if not numero_control:
        messagebox.showerror("Error", "Por favor, ingresa el número de control para generar la credencial")
        return

    try:
        conexion = conectar_db()
        cursor = conexion.cursor()

        cursor.execute("SELECT nombre, apellidop, apellidom, carrera FROM Alumnos WHERE numero_control = %s", (numero_control,))
        resultado = cursor.fetchone()

        # Validar si se encontró el registro
        if not resultado:
            messagebox.showwarning("Sin resultados", "No se encontró un alumno con ese número de control")
            return

        nombre, apellidop, apellidom, carrera = resultado
        cursor.close()
        conexion.close()

        # Crear una nueva ventana para mostrar la credencial
        credencial = tk.Toplevel(ventana)
        credencial.title("Credencial del Alumno")
        credencial.geometry("400x600")

        # Título
        tk.Label(credencial, text=f"Credencial de {nombre}", font=("Arial", 16, "bold")).pack(pady=10)

        # Mostrar nombre, apellidos y carrera
        tk.Label(credencial, text=f"Nombre: {nombre} {apellidop} {apellidom}", font=("Arial", 12)).pack(pady=5)
        tk.Label(credencial, text=f"Carrera: {carrera}", font=("Arial", 12)).pack(pady=5)

        # Cargar y mostrar el QR
        qr_image_path = f"{numero_control}_{nombre}_qr.png"
        qr_image = Image.open(qr_image_path).resize((150, 150))
        qr_photo = ImageTk.PhotoImage(qr_image)
        tk.Label(credencial, image=qr_photo).pack(pady=10)
        # Mantener referencia para evitar recolección de basura
        credencial.qr_photo = qr_photo

        # Cargar y mostrar el código de barras
        barras_image_path = f"{numero_control}_{nombre}_barras.png"
        barras_image = Image.open(barras_image_path).resize((300, 100))
        barras_photo = ImageTk.PhotoImage(barras_image)
        tk.Label(credencial, image=barras_photo).pack(pady=10)
        # Mantener referencia para evitar recolección de basura
        credencial.barras_photo = barras_photo

    except mysql.connector.Error as err:
        messagebox.showerror("Error de BD", f"Ocurrió un error: {err}")
 



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#GENERADOR DE QR Y CODIGO DE BARRAS-------------------------------------------------------------------------------------------------------------------------------------------------------
# Función para generar QR
def generar_qr(numero_control,nombre ,apellidop, apellidom, sangre, nss, contactoem, carrera):
    qr = qrcode.make(f"Nombre: {nombre} {apellidop} {apellidom}\nNúmero de Control: {numero_control}\nTipo de sangre: {sangre}\nNumero de seguro social: {nss}\nContacto de Emergencia: {contactoem}\nCarrera : {carrera}")
    qr.save(f"{numero_control}_{nombre}_qr.png")

# Función para generar código de barras
def generar_codigo_barras(numero_control,nombre):
    codigo = Code128(numero_control, writer=ImageWriter())
    codigo.save(f"{numero_control}_{nombre}_barras")

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
    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Interfaz gráfica con Tkinter la libreria TKINTER------------------------------------------------------------------------------------------------------------------------------------

ventana = tk.Tk()
ventana.title("Registro de Alumnos")
ventana.geometry("500x500")
ventana.config(bg="#ADD8E6")  

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


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#BOTONES-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Botón para guardar
btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_alumno)
btn_guardar.grid(row=8, column=0, columnspan=2, pady=20)

# Botón para Buscar en base al numero de control
btn_guardar = tk.Button(ventana, text="Buscar", command=buscar_alumno)
btn_guardar.grid(row=3, column=2, columnspan=2, pady=20)

# Botón para Eliminar en base al numero de control
btn_guardar = tk.Button(ventana, text="Eliminar", command=eliminar_alumno)
btn_guardar.grid(row=8, column=1, columnspan=2, pady=20)

# Botón para MODIFICAR en base al numero de control
btn_guardar = tk.Button(ventana, text="Modificar", command=modificar_alumno)
btn_guardar.grid(row=8, column=2, columnspan=2, pady=20)

# Agregar botón para mostrar credencial
btn_credencial = tk.Button(ventana, text="Mostrar Credencial", command=mostrar_credencial)
btn_credencial.grid(row=3, column=4, columnspan=2, pady=20)




ventana.mainloop()