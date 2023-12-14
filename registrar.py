from flet import *
import mysql.connector
import threading

def create_registrar_view(page,navigate_to):


    

    # Establece la conexión a la base de datos
    db_connection = mysql.connector.connect(
        host="basedatos.clovqg3umnlu.us-east-2.rds.amazonaws.com",
        user="admin",
        password="Administrador1.",
        database="HOSADB"
    )

    def insertar_usuario(id_usuario, nombre_usuario, rut, correo, contrasena, apodo_usuario, direccion, id_region, id_comuna):
        cursor = db_connection.cursor()
        query = "INSERT INTO HOSADB.BackOffice_usuarios(idUsuario, nombreUsuario, rut, correo, contraseña, apodoUsuario, direccion, idRegion_id, idComuna_id) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (id_usuario, nombre_usuario, rut, correo, contrasena, apodo_usuario, direccion, id_region, id_comuna)

        cursor.execute(query, values)
        db_connection.commit()
        cursor.close()

    def button_clicked(e):
        id_usuario = tb1.value
        nombre_usuario = tb2.value
        rut = tb3.value
        correo = tb4.value
        contrasena = tb5.value
        apodo_usuario = tb6.value
        direccion = tb7.value
        id_region = tb8.value
        id_comuna = tb9.value

        # Verifica que los campos no estén vacíos antes de realizar la inserción
        if not id_usuario or not nombre_usuario or not rut or not correo or not contrasena or not apodo_usuario or not direccion or not id_region or not id_comuna:
            t.value = "Por favor, completa todos los campos."
        else:
            # Inserta el usuario en la base de datos
            insertar_usuario(id_usuario, nombre_usuario, rut, correo, contrasena, apodo_usuario, direccion, id_region, id_comuna)

            # Actualiza el texto en la interfaz
            t.value = ({nombre_usuario},"Registro Exitoso")
            page.clean()
            navigate_to("login")

        page.update()

    def salirApp(e):
        page.clean()
        navigate_to("login")

    def delay(view_name, delay):
        page.clean()
        def navigate():
            page.clean()
            navigate_to(view_name)
        timer = threading.Timer(delay, navigate)
        timer.start()

    # Define los elementos de la interfaz gráfica
    # tb1 = TextField(label="ID Usuario", hint_text="ID Usuario")
    tb2 = TextField(label="Nombre", hint_text="Nombre Completo")
    tb3 = TextField(label="Rut", hint_text="Rol Único Tributario")
    tb4 = TextField(label="Correo", hint_text="Correo Electronico", icon=icons.MAIL)
    tb5 = TextField(label="Contraseña", hint_text="Contraseña", password=True, can_reveal_password=True)
    tb6 = TextField(label="Usuario Ingreso", hint_text="Nombre Usuario en Plataforma")
    tb7 = TextField(label="Dirección", hint_text="Dirección")
    tb8 = TextField(label="Región", hint_text="Región")
    tb9 = TextField(label="Comuna", hint_text="ID Comuna")
    t = Text(color="#D04332")
    registrar = ElevatedButton(text="Registrar", on_click=button_clicked)
    salir = ElevatedButton(text="Salir", on_click=salirApp)
   

    scroll_col= Column(
        scroll=ScrollMode.AUTO,
        controls=[
            Column(height=50),
            tb2,
            tb3,
            tb4,
            tb5,
            tb6,
            tb7,
            tb8,
            tb9,
            t,
            registrar,
            salir,
        ]
    )
  
    # Encerrar la columna en un Container con una altura fija
    scroll_container = Container(
        content=scroll_col,
        height=800,
        expand=1,
    )

    # Agrega los elementos a la página
    page.add(scroll_container)


