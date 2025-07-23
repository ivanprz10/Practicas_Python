import mysql.connector
import tkinter as tk
from tkinter import messagebox


def conectar():
    return mysql.connector.connect(
        host="sql.freedb.tech",
        user="freedb_adminroot",
        password="tDb98K7M#Anp$an",
        database="freedb_RegistroAlumnos",
        port=3306
    )
print(conectar())


conn = conectar()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos (
    numeroControl INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidop  VARCHAR(100),
    apellidom  VARCHAR(100),
    nss  VARCHAR(100),
    carrera VARCHAR(100)         
)
""")

print("Tabla creada correctamente.")
conn.close()


def guardar_alumno():
    #cuando demos clic lo primero que realizara recabar los datos de nuestros forms por el ".get"
    nombre = entry_nombre.get()
    apellidop = entry_apellidop.get()
    apellidom = entry_apellidom.get()
    numero_control = entry_numero_control.get()
    nss = entry_nss.get()
    carrera = entry_carrera.get()

    #con esta condicion indicaremos y analizara todos y cada uno de los campos de nuestra GUI
    #en caso de que un campo este vacio nos mandara un mensaje de error todos los campos son obligatorios
    if not nombre or not apellidom or not apellidop or not  nss or not  numero_control or not carrera:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    
    try:#gracias a este metodo de excepciones, detectaremos cualquier anomalia tipo mysql, en caso que suceda un error de tipo conexion
        #nos mandara al "except" mostrando un caja de mensaje con un error
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO alumnos (nombre, apellidop, apellidom, numeroControl, nss,  carrera) VALUES (%s, %s, %s, %s, %s, %s)", 
                       (nombre, apellidop, apellidom, numero_control, nss,  carrera))#realizamos la consulta correspondiente
                                                                                                        #para mandar los datos a nuestra BD
        messagebox.showinfo("correcto", "se ha guardado el registro exitosamente")
        limpiar_campos()
        conexion.commit()
        cursor.close()
        conexion.close()
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
        conexion = conectar()
        cursor = conexion.cursor()

        # Ejecutar la consulta para buscar al alumno
        cursor.execute("SELECT nombre, apellidop, apellidom, nss, carrera FROM alumnos WHERE numeroControl = %s", (numero_control,))
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

            entry_nss.delete(0, tk.END)
            entry_nss.insert(0, resultado[3])

            entry_carrera.delete(0, tk.END)
            entry_carrera.insert(0, resultado[4])

            messagebox.showinfo("Éxito", "Alumno encontrado correctamente")
        else:
            # Si no se encuentra el alumno, limpiar los campos y mostrar un mensaje


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
        conexion = conectar()
        cursor = conexion.cursor()

        # Ejecutar la consulta para verificar si el alumno existe
        cursor.execute("SELECT * FROM alumnos WHERE numeroControl = %s", (numero_control,))
        resultado = cursor.fetchone()

        # Validar si se encontró el registro
        if resultado:
            # Preguntar al usuario si está seguro de eliminar el registro
            respuesta = messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar al alumno con número de control {numero_control}?")
            
            if respuesta:
                # Ejecutar la consulta para eliminar el registro
                cursor.execute("DELETE FROM alumnos WHERE numeroControl = %s", (numero_control,))
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
    nss = entry_nss.get()
    carrera = entry_carrera.get()

    # Validar que el número de control esté ingresado
    if not numero_control:
        messagebox.showerror("Error", "Por favor, ingresa el número de control para modificar")
        return

    # Validar que todos los campos estén llenos
    if not nombre or not apellidop or not apellidom or not  nss or not carrera:
        messagebox.showerror("Error", "Todos los campos son obligatorios para modificar")
        return

    try:
        # Conectar a la base de datos
        conexion = conectar()
        cursor = conexion.cursor()

        # Verificar si el alumno existe
        cursor.execute("SELECT * FROM alumnos WHERE numeroControl = %s", (numero_control,))
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
                    UPDATE alumnos 
                    SET nombre = %s, apellidop = %s, apellidom = %s, 
                        nss = %s, carrera = %s 
                    WHERE numeroControl = %s
                """, (nombre, apellidop, apellidom, nss, carrera, numero_control))
                
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



def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellidop.delete(0, tk.END)
    entry_apellidom.delete(0, tk.END)
    entry_numero_control.delete(0, tk.END)
    entry_nss.delete(0, tk.END)
    entry_carrera.delete(0, tk.END)


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

tk.Label(ventana, text="NSS:").grid(row=5, column=0, padx=10, pady=10)
entry_nss = tk.Entry(ventana)
entry_nss.grid(row=5, column=1, padx=10, pady=10)

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




ventana.mainloop()


