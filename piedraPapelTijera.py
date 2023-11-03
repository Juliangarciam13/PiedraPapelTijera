import random
import tkinter as tk

def elegir_opcion(humano):
    OPCIONES_VALIDAS = ['piedra', 'papel', 'tijera']
    maquina = random.choice(OPCIONES_VALIDAS)
    resultado = ''
    if maquina == humano:
        resultado = 'Quedamos empatados'
    elif humano == 'piedra' and maquina == 'tijera' or humano == 'tijera' and maquina == 'papel' or humano == 'papel' and maquina == 'piedra':
        resultado = f'Me ganaste humano. Yo saqué {maquina}'
    else:
        resultado = f'¡JA! Te gané, humano! Yo saqué {maquina}'
    etiqueta_resultado.config(text=resultado)

ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")

etiqueta_resultado = tk.Label(ventana, text="¡Elige una opción!", font=('Helvetica', 14))
etiqueta_resultado.pack(pady=20)

boton_piedra = tk.Button(ventana, text="Piedra", command=lambda: elegir_opcion('piedra'))
boton_piedra.pack(side=tk.LEFT, padx=(20, 10))

boton_papel = tk.Button(ventana, text="Papel", command=lambda: elegir_opcion('papel'))
boton_papel.pack(side=tk.LEFT, padx=10)

boton_tijera = tk.Button(ventana, text="Tijera", command=lambda: elegir_opcion('tijera'))
boton_tijera.pack(side=tk.LEFT, padx=(10, 20))

ventana.mainloop()