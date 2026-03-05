import tkinter as tk
from tkinter import messagebox
import random

numero_ale = random.randint(1, 50)
intentos = 0


def crear_ventana():

    '''
    Esta funcion crea la ventana de juego
    '''

    global ventana, entry, msg_result

    ventana = tk.Tk()
    ventana.title("Adivina el número!!")
    ventana.geometry("450x350")
    ventana.config(bg="#000000")
    ventana.attributes("-alpha", 0.9,"-fullscreen", True)

    name_game = tk.Label(
        ventana,
        text="ADIVINA EL NUMERO!",
        font=("Arial", 30),
        fg="White",
        bg="#000000"
    )
    name_game.pack(pady=30)

    msg = tk.Label(
        ventana,
        text="↓↓ Introduce un número ↓↓",
        fg="White",
        bg="#000000"
    )
    msg.pack(pady=10)

    entry = tk.Entry(
        ventana,
        font=("Arial", 20),
        fg="Green",
        bg="Gray",
        borderwidth=20,
        justify="center"
    )
    entry.pack(pady=10)

    # aqui se muestra el resultado. modificado por la funcion "Adivinar"
    msg_result = tk.Label(
        ventana,
        text="",
        fg="White",
        bg="#000000",
        font=("Arial", 16)
    )
    msg_result.pack(pady=15)

    button = tk.Button(
        ventana,
        text="Adivinar",
        fg="White",
        bg="Gray",
        command=Adivinar
    )
    button.pack()

    btn = tk.Button(
        ventana,
        text="Salir",
        fg="White",
        bg="Gray",
        command=Salir
    )
    btn.pack(pady=10)

    ventana.mainloop()


def Adivinar():
    
    '''
    Esta funcion agarra la entrada del usuario, ve si no es texto y la compara a con el numero aleatorio
    '''
    
    global intentos

    texto = entry.get()
    entry.delete(0, tk.END) 

    if not texto.isdigit():
        msg_result.config(text="Eche pon un número válido", fg="yellow")
        return

    num = int(texto)
    intentos += 1

    #este prin solo es para terminar el juego rapido y asi poder hacer un test
    print("Número secreto:", numero_ale)

    if num == numero_ale:
        msg_result.config(text="Ganaste perrita!!", fg="green")
        messagebox.showinfo("Ganaste", f"¡Ganaste perrita! Lo lograste en {intentos} intentos.")
        reiniciar()

    elif intentos >= 5:
        messagebox.showerror("Perdiste", f"Agotaste tus 5 intentos.\nEl número era {numero_ale}.")
        reiniciar()
        return

    elif num < numero_ale :
        msg_result.config(text=f"El número es mayor! llevas {intentos} intentos, al 5\nperderas", fg="red")

    elif num > numero_ale:
        msg_result.config(text=f"El número es menor!\n llevas {intentos} intentos, al 5\nperderas", fg="red")

    
        


    else:
        msg_result.config(text="El número es menor!", fg="red")


def reiniciar():
    
    '''
    Esta funcion reinicia todo el juego
    '''
    
    global numero_ale, intentos
    numero_ale = random.randint(1, 50)
    intentos = 0
    ventana.destroy()
    crear_ventana()

def Salir():
    
    '''
    Funcion para salir del juego
    '''

    ventana.destroy()


crear_ventana()