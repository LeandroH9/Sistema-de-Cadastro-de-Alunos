from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

class signinwindows:

    def __init__(self):
        self.signin_window = Toplevel()
        self.signin_window.title('Login') 
        self.signin_window.resizable(False, False)         
        self.signin_window.iconbitmap('icon.ico')

        Label(self.signin_window, text='Cadastrar', font='Arial').grid(row=0, column=0, sticky=W,pady=10)
        Label(self.signin_window, text='Usuario: ', font='Arial 12').grid(row=1, column=0)
        Label(self.signin_window, text='Senha: ', font='Arial 12').grid(row=2, column=0, pady=(0,20))

        Entry(self.signin_window, font='Arial 10').grid(row=1, column=1)
        Entry(self.signin_window, font='Arial 10').grid(row=2, column=1, pady=(0,20))

        user_add = Button(self.signin_window, text='Cadastrar', font='Arial 18', background='white')
        user_add.grid(row=1, column=2, rowspan=2,padx=20, pady=(0,20))

        view_existing = Button(self.signin_window, text='Visualizar Cadastros', background='white')
        view_existing.grid(row=3, column=0, columnspan=4, rowspan=2, padx=20, pady=(0,20), stick=W+E)

        self.signin_window.mainloop()

class loginwindow:
     def __init__(self):
        self.login_window = Toplevel()
        self.login_window.title('Login') 
        self.login_window.resizable(False, False)         
        self.login_window.iconbitmap('icon.ico')

        Label(self.login_window, text='Login', font='Arial').grid(row=0, column=0, sticky=W,pady=10)
        Label(self.login_window, text='Usuario: ', font='Arial 12').grid(row=1, column=0)
        Label(self.login_window, text='Senha: ', font='Arial 12').grid(row=2, column=0)

        self.butt = Button(self.login_window, text='Entrar', font='Arial 18')
        self.butt.grid(row=1, column=2, rowspan=2,pady=20)

        self.username = Entry(self.login_window, font='Arial 10')
        self.username.grid(row=1, column=1)
        self.password = Entry(self.login_window, font='Arial 10', show='*')
        self.password.grid(row=2, column=1)

        Radiobutton(self.login_window, text='Usuário', value=1).grid(row=3, column=0, pady=15)
        Radiobutton(self.login_window, text='Administrador', value=0).grid(row=3, column=1, pady=15)

        self.login_window.mainloop()


class mainwindow():

    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False) #permite ou não maximizar (altura e largura) da aplicação
        self.root.protocol("WM_DELETE_WINDOW", self.quit_window)
        
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
        self.but = Button(self.root, text='LOGIN', command=self.create_login)
        self.but.configure(width=18, height=2, foreground='white', background='blue4')
        self.but.grid(row=5, column=0, columnspan=2, stick='N')
        
        #criando um menu
        self.menu_bar = Menu(self.root) #cria um objeto Menu
        self.menu_bar.add_separator() #cria um espaçamento no menu

        self.file_menu = Menu(self.menu_bar, tearoff=0)  #tiraroff: tira os tracinhos no menu
        self.file_menu.add_command(label="Entrar", command=self.create_signin)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.quit_window)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_separator() #cria um espaçamento no menu

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Ajuda")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Sobre")

        self.menu_bar.add_cascade(label="Ajuda", menu=self.help_menu)

        self.root.configure(menu=self.menu_bar)
        self.root.mainloop()

        self.root.mainloop()

    def create_login(self):
        try:
            loginwindow()
        except:
            raise Exception('NÃO FOI POSSÍVEL ABRIR ESTE FORMULÁRIO')

    def quit_window(self):
        if messagebox.askokcancel('leandro.henrique@unesp.br', "Deseja realmente sair?"):
            self.root.destroy()

    def create_signin(self):
        try: 
            signinwindows()
        except:
            Exception('NÃO FOI POSSÍVEL ABRIR ESTE FORMULA RIO')   

try:
    mainwindow()
except:
    raise Exception("NÃO PODE SER CRIADO ESTE FORMULARIO")


