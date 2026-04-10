import tkinter as tk

def fechar_sistema():
    root.destroy()

#configuracoes da janela
root = tk.Tk()
root.title("Portal do Aluno - CIn/UFPE")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Bem-vindo ao Sistema!", font=("Helvetica", 24, "bold"), bg="#f0f0f0").pack(pady=50)

#simulacao de dashboard
info_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
info_frame.pack(pady=20, padx=50, fill="both", expand=True)

tk.Label(info_frame, text="Status da Atividade: Finalizada", font=("Arial", 12), bg="white").pack(pady=20)
tk.Label(info_frame, text="Desenvolvedor: Alex Lacava", font=("Arial", 12, "italic"), bg="white").pack(pady=10)

#botao de sair
btn_sair = tk.Button(root, text="Sair do Sistema", command=fechar_sistema, bg="red", fg="white", width=20)
btn_sair.pack(pady=50)

root.mainloop()