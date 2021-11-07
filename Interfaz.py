import tkinter as tk
from Class_interpolacion import VentanaInterpolacion
from Class_integral import VentanaIntegrales
from Class_regresion import Regresion
from Class_Ecua import Ecuaciones
from tkinter.messagebox import *

icono = "Src\Icono.ico"
tamaño_default = '500x500'
color_fondo = "#FEF5ED"


def main():
    # Configuracion pestaña
    v_principal = tk.Tk()
    v_principal.iconbitmap(icono)
    v_principal.configure(background=color_fondo)
    v_principal.geometry(tamaño_default)
    v_principal.resizable(width=0, height=0)
    v_principal.title('Calculadora Analisis numerico')
    v_principal.columnconfigure(0, weight=1)
    v_principal.columnconfigure(1, weight=1)
    v_principal.rowconfigure(0, weight=1)
    v_principal.rowconfigure(1, weight=2)
    v_principal.rowconfigure(2, weight=2)

    # GenerarImagenes
    img_titulo = tk.PhotoImage(file="Src\Titiulo_principal.png")
    img_interpolacion = tk.PhotoImage(file="Src\Interpolacion.png")
    img_integracion = tk.PhotoImage(file="Src\integracion.png")
    img_regresion = tk.PhotoImage(file="Src/regresion.png")
    img_diferencial = tk.PhotoImage(file="Src/diferencial.png")

    # Elementos pestaña
    titulo = tk.Button(v_principal, image=img_titulo, border=0, command=creador)
    botton1 = tk.Button(v_principal, image=img_interpolacion, command=interpolacion, border=0)
    botton2 = tk.Button(v_principal, image=img_integracion, command=inte_definidas, border=0)
    botton3 = tk.Button(v_principal, image=img_regresion, command=regresion, border=0)
    botton4 = tk.Button(v_principal, image=img_diferencial, command=ecu_dife_ordi, border=0)

    # impresion de elementos
    titulo.grid(row=0, column=0, columnspan=2)
    botton2.grid(row=1, column=1)
    botton3.grid(row=2, column=0)
    botton1.grid(row=1, column=0)
    botton4.grid(row=2, column=1)

    v_principal.mainloop()


def interpolacion():
    VentanaInterpolacion()


def inte_definidas():
    VentanaIntegrales()


def regresion():
    Regresion()


def ecu_dife_ordi():
    Ecuaciones()


def creador():
    showinfo(message="Santiago Gomez - Github: SantiagoGM19 \nAlejandro Durango - Github: AlejandroDurango ",
             title="Creadores")


main()
