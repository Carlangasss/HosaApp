# login.py
import flet as ft
import mysql.connector

def create_login_view(page, navigate_to):
    page.bgcolor = "#EEEEEE"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    img = ft.Image(
        src = 'hosaLogo.jpg',
        width = 220,
        height = 220,
        fit = ft.ImageFit.CONTAIN,
    )
    page.add(img)

    def registrar(e):
        page.clean()
        navigate_to("registrar")

    def iniciarSecion(e):
        cn = mysql.connector.connect(host='basedatos.clovqg3umnlu.us-east-2.rds.amazonaws.com', user='admin', passwd='Administrador1.', db='HOSADB')
        cur = cn.cursor()
        cur.execute("SELECT apodoUsuario, contraseña FROM HOSADB.BackOffice_usuarios;")
        rows = cur.fetchall()

        usuario_ingresado = usuario.value.strip()
        contraseña_ingresada = contraseña.value.strip()

        mensaje = ""

        if usuario_ingresado == "" or contraseña_ingresada == "":
            mensaje = "Campos Incompletos"
        else:
            inicio_sesion_exitoso = False
            for row in rows:
                usuario_db = row[0].strip()
                contraseña_db = row[1].strip()

                if usuario_ingresado == usuario_db and contraseña_ingresada == contraseña_db:
                    inicio_sesion_exitoso = True
                    page.clean()
                    navigate_to("home")
                    break
                elif usuario_ingresado == usuario_db:
                    mensaje = "Contraseña Incorrecta"
                    break
                else:
                    mensaje = "Usuario Incorrecto"

            if inicio_sesion_exitoso:
                mensaje = "Inicio de sesión exitoso"

        err.value = mensaje
        cn.close()
        page.update()

    err = ft.Text(color="#D04332")
    usuario = ft.TextField(label="Usuario")
    contraseña = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    inse = ft.ElevatedButton(text="Iniciar Sesión", on_click=iniciarSecion)
    container = ft.Container(height=20)
    mensajeRegis = ft.Text("No tienes cuenta HOSA?", size="13", color="#E38C0E")
    regi = ft.TextButton("Registrarse", on_click=registrar)
    page.add(usuario, contraseña, err, inse,container, mensajeRegis, regi)
