import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Questionário médico")

tk.Label(root, text="Nome:").grid(row=0, column=0)
nome_entry = tk.Entry(root)
nome_entry.grid(row=0, column=1)

tk.Label(root, text="Idade:").grid(row=1, column=0)
idade_entry = tk.Entry(root)
idade_entry.grid(row=1, column=1)

tk.Label(root, text="email:").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Você tem algum problema de saúde?").grid(row=3, column=0, columnspan=2)
resposta1 = tk.StringVar()
tk.Radiobutton(root, text="Sim", variable=resposta1, value="Sim").grid(row=4, column=0)
tk.Radiobutton(root, text="Não", variable=resposta1, value="Não").grid(row=4, column=1)

tk.Label(root, text="Se sim, qual? :").grid(row=6, column=0)
resp_entry = tk.Entry(root)
resp_entry.grid(row=6, column=1)

def enviar_respostas():
    nome = nome_entry.get()
    idade = idade_entry.get()
    resposta = resposta1.get()
    resp = resp_entry.get()
    messagebox.showinfo("Respostas", f"Nome: {nome}\nIdade: {idade}\nTem algum problema?: {resposta}\nProblema: {resp}")

tk.Button(root, text="Enviar", command=enviar_respostas).grid(row=5, column=0, columnspan=2)

root.mainloop()

