from flet import *
import mysql.connector

# Establece la conexión a la base de datos
db_connection = mysql.connector.connect(
    host="basedatos.clovqg3umnlu.us-east-2.rds.amazonaws.com",
    user="admin",
    password="Administrador1.",
    database="HOSADB"
)

# Define tb_user_id en un ámbito más amplio
tb_user_id = TextField(label="Nombre de Usuario", hint_text="Ingrese el nombre de usuario")

# Define tb1, tb2, ..., tb9 en un ámbito más amplio
tb1 = TextField(label="Nombre Usuario", hint_text="Nombre Usuario")
tb2 = TextField(label="Rut", hint_text="Rut")
tb3 = TextField(label="Correo", hint_text="Correo")
tb4 = TextField(label="Contraseña", hint_text="Contraseña")
tb5 = TextField(label="Apodo Usuario", hint_text="Apodo Usuario")
tb6 = TextField(label="Dirección", hint_text="Dirección")
tb7 = TextField(label="Id Plan", hint_text="Id Plan")
tb8 = TextField(label="Id Región", hint_text="Id Región")
tb9 = TextField(label="Id Dispositivo", hint_text="Id Dispositivo")

def seleccionar_usuario():
    try:
        # Abre la conexión a la base de datos
        if db_connection.is_connected():
            cursor = db_connection.cursor()

            # Obtiene el nombre de usuario ingresado por el usuario
            user_id = tb_user_id.value

            # Modifica la consulta para seleccionar el usuario por nombreUsuario
            query = "SELECT * FROM HOSADB.BackOffice_usuarios WHERE nombreUsuario = %s"
            cursor.execute(query, (user_id,))

            # Recupera los resultados de la consulta
            result = cursor.fetchone()

            # Cierra el cursor y la conexión
            cursor.close()

            # Muestra los resultados en la interfaz
            if result:
                tb1.value = result[1]  # NombreUsuario
                tb2.value = result[2]  # Rut
                tb3.value = result[3]  # Correo
                tb4.value = result[4]  # Contraseña
                tb5.value = result[5]  # ApodoUsuario
                tb6.value = result[6]  # Direccion
                tb7.value = result[7]  # IdPlan
                tb8.value = result[8]  # IdRegion
                tb9.value = result[9]  # IdDispositivo
                print("Usuario seleccionado correctamente.")
            else:
                print("Usuario no encontrado.")

    except Exception as ex:
        # Usa Print para mostrar el error en la consola
        print(f"Error: {ex}")

def actualizar_usuario():
    try:
        # Obtiene el nombre de usuario ingresado por el usuario
        user_id = tb_user_id.value

        # Abre la conexión a la base de datos
        if db_connection.is_connected():
            cursor = db_connection.cursor()

            # Utiliza la sintaxis correcta para la instrucción UPDATE
            query = "UPDATE HOSADB.BackOffice_usuarios SET nombreUsuario = %s, rut = %s, correo = %s, contraseña = %s, apodoUsuario = %s, direccion = %s, idPlan_id = %s, idRegion_id = %s WHERE nombreUsuario = %s"
            values = (tb1.value, tb2.value, tb3.value, tb4.value, tb5.value, tb6.value, tb7.value, tb8.value, user_id)

            cursor.execute(query, values)

            # Realiza el commit para aplicar los cambios en la base de datos
            db_connection.commit()

            # Cierra el cursor y la conexión
            cursor.close()

            print("Datos editados y guardados")
        else:
            print("La conexión a la base de datos está cerrada")
    except Exception as ex:
        print(f"Error: {ex}")

def eliminar_usuario():
    try:
        # Obtiene el nombre de usuario ingresado por el usuario
        user_id = tb_user_id.value

        # Abre la conexión a la base de datos
        if db_connection.is_connected():
            cursor = db_connection.cursor()

            # Utiliza la sintaxis correcta para la instrucción DELETE
            query = "DELETE FROM HOSADB.BackOffice_usuarios WHERE nombreUsuario = %s"
            cursor.execute(query, (user_id,))

            # Realiza el commit para aplicar los cambios en la base de datos
            db_connection.commit()

            # Cierra el cursor y la conexión
            cursor.close()

            print("Usuario eliminado correctamente.")
        else:
            print("La conexión a la base de datos está cerrada")
    except Exception as ex:
        print(f"Error: {ex}")

def main(page: Page):
    def seleccionar_button_clicked(e):
        seleccionar_usuario()
        page.update()

    def actualizar_button_clicked(e):
        actualizar_usuario()
        page.update()

    def eliminar_button_clicked(e):
        eliminar_usuario()
        page.update()

    # Define los elementos de la interfaz gráfica
    seleccionar_b = ElevatedButton(text="Seleccionar Usuario", on_click=seleccionar_button_clicked)
    actualizar_b = ElevatedButton(text="Actualizar", on_click=actualizar_button_clicked)
    eliminar_b = ElevatedButton(text="Eliminar", on_click=eliminar_button_clicked)

    # Agrega los elementos a la página
    page.add(tb_user_id, seleccionar_b, tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, actualizar_b, eliminar_b)

# Ejecuta la aplicación con la función main como objetivo
app(target=main)
