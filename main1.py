import customtkinter






Janela = customtkinter.CTk()
Janela.geometry('600x140+100+100')
Janela.resizable(False, False)
Janela.title('Meu gerador de Senhas fronte end © Dev Joel 2024')


Epassword = customtkinter.CTkEntry(Janela, width=575)
Epassword.place(x=10, y=10)


Grandes = customtkinter.CTkCheckBox(Janela, text='Grandes')
Grandes.place(x=10, y=55)

Pequenas = customtkinter.CTkCheckBox(Janela, text='Pequenas')
Pequenas.place(x=105, y=55)

Numeros = customtkinter.CTkCheckBox(Janela, text='Numeros')
Numeros.place(x=200, y=55)

Simbolos = customtkinter.CTkCheckBox(Janela, text='Simbolos')
Simbolos.place(x=295, y=55)

aumentar = customtkinter.CTkButton(Janela, text='+', width=10)
aumentar.place(x=395, y=55)

ENumero = customtkinter.CTkEntry(Janela, width=40)
ENumero.place(x=420, y=55)

Deminuir = customtkinter.CTkButton(Janela, text='-', width=10)
Deminuir.place(x=465, y=55)

Gerar = customtkinter.CTkButton(Janela, text='Gerar', width=75)
Gerar.place(x=10, y=95)

Copiar = customtkinter.CTkButton(Janela, text='Copiar', width=75)
Copiar.place(x=100, y=95)

Limpar = customtkinter.CTkButton(Janela, text='Limpar', width=75)
Limpar.place(x=190, y=95)

Sair = customtkinter.CTkButton(Janela, text='Sair', width=75)
Sair.place(x=280, y=95)


Janela.mainloop()