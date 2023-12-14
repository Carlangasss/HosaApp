# home.py
import logging
import flet as ft
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER
import mysql.connector

#Conección con la api TUYA
ACCESS_ID = "xje5t5vu8cqcvvhadw78"
ACCESS_KEY = "68b3b2f2e6984ba4bf06be90a7ad78fa"
API_ENDPOINT = "https://openapi.tuyaus.com"

# TUYA_LOGGER.setLevel(logging.DEBUG)
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()



#Dispositivos Id
LUZ_1 ="ebb63196d8a8ff3e05buvw"

response = openapi.get('/v1.0/devices/{}'.format(LUZ_1))
data = response

def create_home_view(page, navigate_to):
    
    #configuración página
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    def on_dispo_button_click(e):
        page.clean()
        navigate_to("dispo")

    def salirApp(e):
        page.clean()
        navigate_to("login")

    columnMenu = ft.Column(
        spacing=15,
        controls=[
            ft.TextButton("MenuDispo",on_click=on_dispo_button_click, icon=ft.icons.PERM_DEVICE_INFO_OUTLINED, width=300, height=80),
            ft.TextButton("Zonas",on_click=on_dispo_button_click, icon=ft.icons.OTHER_HOUSES_OUTLINED, width=300, height=80),
            ft.TextButton("Reportes",on_click=on_dispo_button_click, icon=ft.icons.FACT_CHECK_OUTLINED, width=300, height=80),
            ft.TextButton("HOSA",on_click=on_dispo_button_click, icon=ft.icons.OFFLINE_BOLT_OUTLINED, width=300, height=80),
            ft.TextButton("Configuracion",on_click=on_dispo_button_click, icon=ft.icons.SETTINGS_OUTLINED, width=300, height=80),
            # ft.TextButton("usuarios",on_click=on_dispo_button_click, icon=ft.icons.SUPERVISED_USER_CIRCLE_OUTLINED, width=300, height=80),
            ft.TextButton("Deslogearse",on_click=salirApp, icon=ft.icons.LOGOUT_OUTLINED, width=300, height=80)
        ],
    )

    page.clean()
    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=20),
            ft.Row(
                width=100,
                height=80,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text("Menu",size=24,text_align=ft.TextAlign.CENTER),
                ]
            ),
            ft.Divider(thickness=1),
            ft.Container(height=5),
            columnMenu
        ],
    )
   
    page.appbar = ft.AppBar(
        leading_width=50,
        center_title=True,
        title=ft.Text("HOSA",size=40,italic=True),
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    
    #Contenido

    flag = True

    def estadoLuz(e):
        nonlocal flag
        flag = not flag
        commands = {'commands': [{'code': 'switch_led', 'value': flag}]}
        openapi.post('/v1.0/iot-03/devices/{}/commands'.format(LUZ_1), commands)
        page.update()

    items = [] 
    items.append(ft.Icon(name=ft.icons.LIGHTBULB, color=ft.colors.AMBER, size=25))
    items.append(ft.Text(data['result']['name'],size=15, color="#0F1111"))

    row = ft.Row(controls=items,spacing=20)

    tablaDispo = ft.Container(
        content= row,
        margin=10,
        padding=20,
        width=400,
        height=80,
        border_radius=10,
        ink=True,
        bgcolor="#C1EDEE",
        on_click=estadoLuz,
    )

    
    page.add(tablaDispo)
