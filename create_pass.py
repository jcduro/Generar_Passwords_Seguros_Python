import tkinter as tk
import random
import string

def generar():
    try:
        longitud = int(largo.get())
    except:
        resultado.set("Longitud inválida")
        return
    opciones = ''
    if var_mayus.get():
        opciones += string.ascii_uppercase
    if var_minus.get():
        opciones += string.ascii_lowercase
    if var_num.get():
        opciones += string.digits
    if var_simbolos.get():
        opciones += string.punctuation
    if not opciones:
        resultado.set("¡Debes marcar al menos una opción!")
        return
    password = ''.join(random.choice(opciones) for _ in range(longitud))
    resultado.set(password)
    ventana.clipboard_clear()
    ventana.clipboard_append(password)

ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("390x270")
ventana.resizable(0,0)
ventana.config(bg='#f6f7fb')  # Fondo claro para mejor visibilidad

largo = tk.StringVar(value='12')
resultado = tk.StringVar(value='')

tk.Label(
    ventana, text="Elige largo y tipos de caracteres:",
    font=("Arial",13,"bold"), bg='#f6f7fb', fg='#24292f', pady=5
).grid(row=0, column=0, columnspan=2, sticky="w", padx=15)

# Opciones de selección (Checkbuttons)
var_mayus = tk.BooleanVar(value=True)
var_minus = tk.BooleanVar(value=True)
var_num = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

frame = tk.Frame(ventana, bg="#eaeaea")  # Fondo claro opciones
frame.grid(row=1, column=0, columnspan=2, padx=13, pady=0, sticky="we")

tk.Checkbutton(
    frame, text="Mayúsculas (A-Z)", variable=var_mayus, bg='#eaeaea', font=("Arial",12)
).grid(row=0, column=0, sticky="w", pady=2)
tk.Checkbutton(
    frame, text="Minúsculas (a-z)", variable=var_minus, bg='#eaeaea', font=("Arial",12)
).grid(row=1, column=0, sticky="w", pady=2)
tk.Checkbutton(
    frame, text="Números (0-9)", variable=var_num, bg='#eaeaea', font=("Arial",12)
).grid(row=0, column=1, sticky="w", padx=15, pady=2)
tk.Checkbutton(
    frame, text="Símbolos (#$%&)", variable=var_simbolos, bg='#eaeaea', font=("Arial",12)
).grid(row=1, column=1, sticky="w", padx=15, pady=2)

tk.Label(
    ventana, text="Longitud:", font=("Arial",12), bg='#f6f7fb', fg='#24292f'
).grid(row=2, column=0, sticky="e", pady=7, padx=5)
tk.Entry(
    ventana, textvariable=largo, font=("Arial",12), width=5, justify='center'
).grid(row=2, column=1, sticky="w", pady=7)

tk.Button(
    ventana, text="Generar Contraseña", font=("Arial",12,"bold"),
    command=generar, bg="#186de6", fg="white", width=25
).grid(row=3, column=0, columnspan=2, pady=12)

tk.Entry(
    ventana, textvariable=resultado, font=("Arial",16), width=33, bd=3, justify='center'
).grid(row=4, column=0, columnspan=2, pady=4, padx=5)

tk.Label(
    ventana, text="📋 La contraseña se copia automáticamente al portapapeles",
    bg='#f6f7fb', fg='#24292f', font=("Arial",10)
).grid(row=5, column=0, columnspan=2,pady=5)

ventana.mainloop()
