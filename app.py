from tkinter import *

from users import Users


class App:
    def __init__(self, interface=None):

        self.logo = Label(interface)
        self.logo.la = PhotoImage(file="logo_xicoria.png")
        self.logo["image"] = self.logo.la
        self.logo.place(x=0, y=0)

        self.insert_data = Label(interface, text="Insira os Dados:")
        self.insert_data["font"] = ("Calibri", "15", "bold")
        self.insert_data.place(x=550, y=0)

        self.text_id = Label(interface, text="ID de Usuário:", font="Calibri")
        self.text_id.place(x=400, y=40)

        self.id = Entry(interface, width="5")
        self.id.place(x=520, y=40)

        self.button_search = Button(interface, text="Buscar", command=self.searchUser, width="10", background="#9932CC")
        self.button_search.place(x=580, y=35)

        self.text_name = Label(interface, text="Nome Completo:", font="Calibri", wraplength=500, justify=LEFT)
        self.text_name.place(x=400, y=70)

        self.name = Entry(interface, width="40")
        self.name.place(x=520, y=70)

        self.text_email = Label(interface, text="E-mail:", font="Calibri", wraplength=500, justify=LEFT)
        self.text_email.place(x=400, y=100)

        self.email = Entry(interface, width="40")
        self.email.place(x=520, y=100)

        self.text_tel = Label(interface, text="Telefone:", font="Calibri", wraplength=500, justify=LEFT)
        self.text_tel.place(x=400, y=130)

        self.tel = Entry(interface, width="15")
        self.tel.place(x=520, y=130)

        self.button_insert = Button(interface, text="Inserir", command=self.insertUser, width="8", background="#9932CC")
        self.button_insert.place(x=520, y=180)

        self.button_update = Button(interface, text="Alterar", command=self.updateUser, width="8", background="#9932CC")
        self.button_update.place(x=586, y=180)

        self.button_delete = Button(interface, text="Excluir", command=self.deleteUser, width="8", background="#9932CC")
        self.button_delete.place(x=652, y=180)

        self.answer = Label(interface)
        self.answer.place(x=520, y=220)

    def insertUser(self):
        user = Users()

        user.name = self.name.get()
        user.email = self.email.get()
        user.tel = self.tel.get()

        self.answer["text"] = user.insertUser()

        self.id.delete(0, END)
        self.name.delete(0, END)
        self.email.delete(0, END)
        self.tel.delete(0, END)

    def updateUser(self):
        user = Users()

        user.id_user = self.id.get()
        user.name = self.name.get()
        user.email = self.email.get()
        user.tel = self.tel.get()

        self.answer["text"] = user.updateUser()

        self.id.delete(0, END)
        self.name.delete(0, END)
        self.email.delete(0, END)
        self.tel.delete(0, END)

    def deleteUser(self):
        user = Users()

        user.id_user = self.id.get()

        self.answer["text"] = user.deleteUser()

        self.id.delete(0, END)
        self.name.delete(0, END)
        self.email.delete(0, END)
        self.tel.delete(0, END)

    def searchUser(self):
        user = Users()

        id_user = self.id.get()

        self.answer["text"] = user.selectUser(id_user)

        self.id.delete(0, END)
        self.id.insert(INSERT, user.id_user)

        self.name.delete(0, END)
        self.name.insert(INSERT, user.name)

        self.email.delete(0, END)
        self.email.insert(INSERT, user.email)

        self.tel.delete(0, END)
        self.tel.insert(INSERT, user.tel)

interface = Tk()
interface.iconbitmap("ico_mm.ico")
interface.title("Usuários MM")
interface.geometry("800x270")
interface.wm_resizable(0, 0)
App(interface)
interface.mainloop()