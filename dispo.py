# dispo.py
import flet as ft

def create_dispo_view(page,navigate_to):
    
    def on_config_button_click(e):
        navigate_to("config")
    
    def volverHome(e):
        navigate_to("home")

    
    page.clean()
    
    page.add(
        ft.Dropdown(
            label="Dispositivo 1",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
        ),
        ft.Dropdown(
            label="Zona",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
           
        ),
        ft.Divider(thickness=3),
        ft.Dropdown(
            label="Dispositivo 2",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
        ),
        ft.Dropdown(
            label="Zona",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
           
        ),
        ft.Divider(thickness=3),ft.Dropdown(
            label="Dispositivo 3",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
        ),
        ft.Dropdown(
            label="Zona",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
           
        ),
        ft.Divider(thickness=3),ft.Dropdown(
            label="Dispositivo 4",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
        ),
        ft.Dropdown(
            label="Zona",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
           
        ),
        ft.Divider(thickness=3)
    )

    btn = ft.ElevatedButton("Ir a config", on_click=on_config_button_click)
    volver = ft.ElevatedButton("Volver", on_click=volverHome)

    page.add(btn,volver)
