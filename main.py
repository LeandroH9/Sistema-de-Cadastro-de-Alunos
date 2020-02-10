from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3


class mainwindow():

    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False) #permite ou não maximizar (altura e largura) da aplicação
        self.root.protocol("WM_DELETE_WINDOW")
        
        #titulo e icone da janela
        self.root.iconbitmap('icon.ico') #extensão tem que ser .ico
        self.root.title('Cadastro de Alunos') 
       
        #adicionando imagem
        self.img = ImageTk.PhotoImage(Image.open('logo.png'))
        self.panel = Label(self.root, image=self.img)
        self.panel.grid(row=0, column=0, columnspan=2)

        #adicionando textos (label)
        Label(self.root, text='Cadastro de Alunos', font='Arial 20', foreground='blue4').grid(row=1, columnspan=2, column=0, sticky=W+E, padx=40, pady=0)
        Label(self.root, text='Desenvolvido por Leandro Henrique', font='Arial 8', foreground='gray1').grid(row=2, columnspan=2, column=0, sticky=W+E, padx=40 )
        Label(self.root, text='Faça seu login para continuar', font='Arial 12', foreground='blue4').grid(row=3, columnspan=2, column=0, sticky=W+E, pady=30, padx=40)

        #configurando botão de login
        self.but = Button(self.root, text='LOGIN')
        self.but.configure(width=18, height=2, foreground='white', background='blue4')
        self.but.grid(row=5, column=0, columnspan=2, stick='N')
        
        #criando um menu
        self.menu_bar = Menu(self.root)
        self.menu_bar.add_separator()

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Entrar")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair")

        self.menu_bar.add_cascade(label="File")
        self.menu_bar.add_separator()

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Ajuda")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Sobre")

        self.menu_bar.add_cascade(label="Ajuda")

        self.root.configure(menu=self.menu_bar)
        self.root.mainloop()

        self.root.mainloop()

try:
    mainwindow()
except:
    raise Exception("NÃO PODE SER CRIADO ESTE FORMULARIO")


