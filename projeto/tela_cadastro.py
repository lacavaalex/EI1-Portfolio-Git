import tkinter as tk
from tkinter import messagebox
import sys
import subprocess

#metodo para realizar o cadastro
def realizar_cadastro():
    usuario = entry_usuario.get()
    email = entry_email.get()
    senha = entry_senha.get()
    
    if "@" not in email:
        messagebox.showerror("Erro", "E-mail inválido!")
    elif len(senha) < 6:
        messagebox.showwarning("Aviso", "Senha muito curta.")
    else:
        messagebox.showinfo("Sucesso", f"Usuário {usuario} cadastrado!")
        root.destroy()
        #chamada do arquivo de login
        subprocess.run([sys.executable, "tela_login.py"])

# configuracoes da janela
root = tk.Tk()
root.title("Sistema de Validação - Cadastro")
root.geometry("800x600")

tk.Label(root, text="Criar Nova Conta", font=("Arial", 14, "bold")).pack(pady=100)

tk.Label(root, text="Nome de Usuário:").pack()
entry_usuario = tk.Entry(root, width=50)
entry_usuario.pack(pady=5)

tk.Label(root, text="E-mail:").pack()
entry_email = tk.Entry(root, width=50)
entry_email.pack(pady=5)

tk.Label(root, text="Senha:").pack()
entry_senha = tk.Entry(root, width=50, show="*")
entry_senha.pack(pady=5)

btn_cadastrar = tk.Button(root, text="Cadastrar", command=realizar_cadastro, bg="green", fg="white")
btn_cadastrar.pack(pady=20)

root.mainloop()