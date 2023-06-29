import tkinter as tk
from tkinter import Label, Entry, Button, messagebox, Radiobutton, StringVar


def validar_entrada(P):
    # P es el valor que el usuario está intentando ingresar.
    # Esta función retorna True si la entrada es un número entre 0 y 3 o una cadena vacía,
    # de lo contrario retorna False.
    if P.isdigit():
        valor = int(P)
        return valor >= 0 and valor <= 3
    return P == ""

def invertir_puntaje(puntaje):
    # Invierte el puntaje 
    return 3 - puntaje

def obtener_puntajes():
    rasgo_invertir = {1, 6, 7, 10, 13, 16, 19}
    estado_invertir = {1, 2, 5, 8, 10, 11, 15, 16, 19, 20}

    suma_rasgo = 0
    for i, entry in enumerate(rasgo_entries, start=1):
        puntaje = int(entry.get())
        if i in rasgo_invertir:
            puntaje = invertir_puntaje(puntaje)
        suma_rasgo += puntaje

    suma_estado = 0
    for i, entry in enumerate(estado_entries, start=1):
        puntaje = int(entry.get())
        if i in estado_invertir:
            puntaje = invertir_puntaje(puntaje)
        suma_estado += puntaje

    genero_seleccionado = genero.get()

    # Baremos para Ansiedad Rasgo y Estado
    if genero_seleccionado == "Varón":
        categorias_rasgo = [("Alta", (26, 60)), ("Sobre promedio", (20, 25)), ("Promedio", (14, 19)), ("Tiende al promedio", (0, 13))]
        categorias_estado = [("Alta", (29, 60)), ("Sobre promedio", (20, 28)), ("Promedio", (14, 19)), ("Tiende al promedio", (0, 13))]
    else:
        categorias_rasgo = [("Alta", (33, 60)), ("Sobre promedio", (26, 32)), ("Promedio", (24, 25)), ("Tiende al promedio", (0, 23))]
        categorias_estado = [("Alta", (32, 60)), ("Sobre promedio", (23, 31)), ("Promedio", (20, 22)), ("Tiende al promedio", (0, 19))]

    resultado_rasgo = next((categoria for categoria, (minimo, maximo) in categorias_rasgo if minimo <= suma_rasgo <= maximo), "Desconocido")
    resultado_estado = next((categoria for categoria, (minimo, maximo) in categorias_estado if minimo <= suma_estado <= maximo), "Desconocido")

    # Mostrar los resultados
    messagebox.showinfo("Resultados", f"Ansiedad Rasgo: {suma_rasgo} ({resultado_rasgo})\nAnsiedad Estado: {suma_estado} ({resultado_estado})\nGénero: {genero_seleccionado}")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Corrección Cuestionario STAI")
#ventana.geometry("1200x400")  # Cambiar el tamaño de la ventana

# Registra la función de validación
vcmd = ventana.register(validar_entrada)

# Crear etiquetas y campos de entrada para Ansiedad Rasgo
Label(ventana, text="Ansiedad Rasgo", font=("Arial", 12), bg="blue", fg="white").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)
rasgo_entries = []
for i in range(1, 21):
    Label(ventana, text=f"Ítem {i}:", anchor=tk.E).grid(row=i, column=0, padx=5, pady=5)
    entry = Entry(ventana, validate="key", validatecommand=(vcmd, '%P'))
    entry.grid(row=i, column=1, padx=5, pady=5)
    rasgo_entries.append(entry)

# Crear etiquetas y campos de entrada para Ansiedad Estado
Label(ventana, text="Ansiedad Estado", font=("Arial", 12), bg="green", fg="white").grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)
estado_entries = []
for i in range(1, 21):
    Label(ventana, text=f"Ítem {i}:", anchor=tk.E).grid(row=i, column=2, padx=5, pady=5)
    entry = Entry(ventana, validate="key", validatecommand=(vcmd, '%P'))
    entry.grid(row=i, column=3, padx=5, pady=5)
    estado_entries.append(entry)

# Sección de selección de género
Label(ventana, text="Género del evaluado:", font=("Arial", 10)).grid(row=21, column=0, columnspan=2, pady=10)
genero = StringVar(value="Varón")
Radiobutton(ventana, text="Varón", variable=genero, value="Varón").grid(row=21, column=2)
Radiobutton(ventana, text="Mujer", variable=genero, value="Mujer").grid(row=21, column=3)

# Crear botón para obtener los puntajes
Button(ventana, text="Obtener Puntajes", command=obtener_puntajes, font=("Arial", 12), bg="pink", fg="white").grid(row=10, column=5, columnspan=4, pady=10)

# Iniciar la GUI
ventana.mainloop()