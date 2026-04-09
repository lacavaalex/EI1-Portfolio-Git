import tkinter as tk
from tkinter import messagebox

#metodo de validacao do login
def validar_login():
    email = entry_email.get()
    senha = entry_senha.get()
    
    if "@" in email and len(senha) >= 6:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showwarning("Erro", "E-mail ou senha inválidos.")

#configuracao da janela principal
root = tk.Tk()
root.title("Sistema de Validação - Login")
root.geometry("800x600")

tk.Label(root, text="Login", font=("Arial", 16, "bold")).pack(pady=100)

#campos de senha e email
tk.Label(root, text="E-mail:").pack()
entry_email = tk.Entry(root, width=50)
entry_email.pack(pady=5)

tk.Label(root, text="Senha:").pack()
entry_senha = tk.Entry(root, width=50, show="*")
entry_senha.pack(pady=5)

#botao de login
btn_login = tk.Button(root, text="Entrar", command=validar_login, bg="blue", fg="white")
btn_login.pack(pady=20)

root.mainloop()