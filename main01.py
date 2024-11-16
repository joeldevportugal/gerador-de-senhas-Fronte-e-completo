from tkinter import messagebox
import customtkinter
import random
import string

# Função para gerar senha
def gerar_senha():
    tamanho = int(ENumero.get()) if ENumero.get().isdigit() else 8  # Tamanho padrão é 8 se não especificado
    caracteres = ""

    if Grandes.get():  # Se a opção "Grandes" estiver selecionada
        caracteres += string.ascii_uppercase
    if Pequenas.get():  # Se a opção "Pequenas" estiver selecionada
        caracteres += string.ascii_lowercase
    if Numeros.get():  # Se a opção "Numeros" estiver selecionada
        caracteres += string.digits
    if Simbolos.get():  # Se a opção "Simbolos" estiver selecionada
        caracteres += string.punctuation

    if not caracteres:  # Verifica se pelo menos uma opção foi selecionada
        Epassword.delete(0, customtkinter.END)
        Epassword.insert(0, "Selecione pelo menos uma opção!")
        return

    senha = "".join(random.choices(caracteres, k=tamanho))
    Epassword.delete(0, customtkinter.END)
    Epassword.insert(0, senha)

# Função para copiar a senha gerada
def copiar_senha():
    Janela.clipboard_clear()
    Janela.clipboard_append(Epassword.get())
    Janela.update()
    messagebox.showinfo("Senha","Senha copiada com sucesso!")

# Função para limpar o campo de senha
def limpar_campo():
    Epassword.delete(0, customtkinter.END)
    ENumero.delete(0, customtkinter.END)
    Grandes.deselect()
    Pequenas.deselect()
    Numeros.deselect()
    Simbolos.deselect()
    messagebox.showinfo("Senha","Senha Limpa com sucesso!")

# Função para ajustar o tamanho da senha
def ajustar_tamanho(delta):
    if ENumero.get().isdigit():
        tamanho = int(ENumero.get()) + delta
    else:
        tamanho = 8 + delta  # Valor inicial padrão
    tamanho = max(1, tamanho)  # Garante que o tamanho seja pelo menos 1
    ENumero.delete(0, customtkinter.END)
    ENumero.insert(0, str(tamanho))

def sair ():
    resposta = messagebox.askyesno("Confirmação", "Deseja realmente sair?")
    if resposta:
        Janela.destroy()    

# adicionar as cores 
co0 ="#ffffff" # cor Branca
co1 ="#fff7ed" # amarelo Claro
co2 ="#c0c0c0" # Cinza Claro
co3 ="#000000" # Preto letra

# Configuração da janela
Janela = customtkinter.CTk()
Janela.geometry('600x140+100+100')
Janela.resizable(False, False)
Janela.title('Meu Gerador de Senhas fronte end e back end © Dev Joel 2024 ')
Janela.config(bg=co0)

# Campo para exibir a senha
Epassword = customtkinter.CTkEntry(Janela, width=575, bg_color=co0, fg_color=co1, placeholder_text='Sua Password Gerada Aqui')
Epassword.place(x=10, y=10)

# Checkboxes para seleção de tipos de caracteres
Grandes = customtkinter.CTkCheckBox(Janela, text='Grandes', bg_color=co0)
Grandes.place(x=10, y=55)

Pequenas = customtkinter.CTkCheckBox(Janela, text='Pequenas', bg_color=co0)
Pequenas.place(x=105, y=55)

Numeros = customtkinter.CTkCheckBox(Janela, text='Numeros', bg_color=co0)
Numeros.place(x=200, y=55)

Simbolos = customtkinter.CTkCheckBox(Janela, text='Simbolos', bg_color=co0)
Simbolos.place(x=295, y=55)

# Botões para ajustar o tamanho da senha
aumentar = customtkinter.CTkButton(Janela, text='+', width=10, command=lambda: ajustar_tamanho(1), bg_color=co0, fg_color=co2, text_color=co3)
aumentar.place(x=395, y=55)

ENumero = customtkinter.CTkEntry(Janela, width=40, bg_color=co0)
ENumero.place(x=420, y=55)

Deminuir = customtkinter.CTkButton(Janela, text='-', width=10, command=lambda: ajustar_tamanho(-1), bg_color=co0, fg_color=co2, text_color=co3)
Deminuir.place(x=465, y=55)

# Botões de ação
Gerar = customtkinter.CTkButton(Janela, text='Gerar', width=75, command=gerar_senha, bg_color=co0, fg_color=co2, text_color=co3)
Gerar.place(x=10, y=95)

Copiar = customtkinter.CTkButton(Janela, text='Copiar', width=75, command=copiar_senha, bg_color=co0, fg_color=co2, text_color=co3)
Copiar.place(x=100, y=95)

Limpar = customtkinter.CTkButton(Janela, text='Limpar', width=75, command=limpar_campo, bg_color=co0, fg_color=co2, text_color=co3)
Limpar.place(x=190, y=95)

Sair = customtkinter.CTkButton(Janela, text='Sair', width=75, command=sair, bg_color=co0, fg_color=co2, text_color=co3)
Sair.place(x=280, y=95)

# Iniciar a janela
Janela.mainloop()