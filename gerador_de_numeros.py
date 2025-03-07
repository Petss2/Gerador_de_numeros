import tkinter as tk
import random

#função que sorteia os numeros.
def sortear_numeros():
    lista = list()
    for c in range(0, 6):
        numero = random.randint(1, 60)
        lista.append(numero)


    resultado_label.config(text=f'Números sorteados: {lista}')


#criando a janela
window = tk.Tk()
window.geometry('400x250')
window.title('Sorteio de números')

#adiciona um frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

#adicionando label
resultado_label = tk.Label(frame, text='Clique no botão para sortear números.')
resultado_label.pack(fill='x', expand=True)


#botão para sortear números
button = tk.Button(frame, text='Sortear números', command=sortear_numeros)
button.pack()

#inicia o loop principal da interface gráfica
window.mainloop()

