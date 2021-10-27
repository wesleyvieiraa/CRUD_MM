from tkinter import *

from Users import Users
from ValidateEmail import ValidateEmail
from ValidateTel import ValidateTel


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

        self.button_search = Button(interface, text="Buscar", command=self.search_user, width="10",
                                    background="#9932CC")
        self.button_search.place(x=580, y=35)

        self.text_name = Label(interface, text="*Nome Completo:", font="Calibri", justify=LEFT)
        self.text_name.place(x=392, y=70)

        self.name = Entry(interface, width="40")
        self.name.place(x=520, y=70)

        self.text_email = Label(interface, text="*E-mail:", font="Calibri", justify=LEFT)
        self.text_email.place(x=392, y=100)

        self.email = Entry(interface, width="40")
        self.email.place(x=520, y=100)

        self.text_tel = Label(interface, text="*Telefone:", font="Calibri", justify=LEFT)
        self.text_tel.place(x=392, y=130)

        self.tel = Entry(interface, width="15")
        self.tel.place(x=520, y=130)

        self.text_warning_tel = Label(interface, text="Insira apenas o DDD e número sem espaço")
        self.text_warning_tel["font"] = ("Calibri", "8")
        self.text_warning_tel.place(x=518, y=150)

        self.button_insert = Button(interface, text="Inserir", command=self.insert_user, width="8",
                                    background="#9932CC")
        self.button_insert.place(x=520, y=180)

        self.button_update = Button(interface, text="Alterar", command=self.update_user, width="8",
                                    background="#9932CC")
        self.button_update.place(x=586, y=180)

        self.button_delete = Button(interface, text="Excluir", command=self.delete_user, width="8",
                                    background="#9932CC")
        self.button_delete.place(x=652, y=180)

        self.answer = Label(interface)
        self.answer.place(x=520, y=220)

    def insert_user(self):
        tel = self.tel.get()
        tel_object = ValidateTel(tel)

        email = self.email.get()
        email_object = ValidateEmail(email)

        if email_object.validate_return() == False or tel_object.validate_return() == False:
            self.answer["text"] = "E-mail e/ou telefone inválido"
        else:

            user = Users()

            user.name = self.name.get()
            user.email = email_object.format_email()
            user.tel = tel_object.format_number()

            self.answer["text"] = user.insert_user()

            self.delete_fields()

    def update_user(self):
        tel = self.tel.get()
        tel_object = ValidateTel(tel)

        email = self.email.get()
        email_object = ValidateEmail(email)

        if email_object.validate_return() == False or tel_object.validate_return() == False:
            self.answer["text"] = "E-mail ou telefone inválido"
        else:
            user = Users()

            user.id_user = self.id.get()
            user.name = self.name.get()
            user.email = email_object.format_email()
            user.tel = tel_object.format_number()

            self.answer["text"] = user.update_user()

            self.delete_fields()

    def delete_user(self):
        user = Users()

        user.id_user = self.id.get()

        self.answer["text"] = user.delete_user()

        self.delete_fields()

    def search_user(self):
        user = Users()

        id_user = self.id.get()

        self.answer["text"] = user.select_user(id_user)

        self.delete_fields()

        self.id.insert(INSERT, user.id_user)
        self.name.insert(INSERT, user.name)
        self.email.insert(INSERT, user.email)
        self.tel.insert(INSERT, user.tel)

    def delete_fields(self):
        self.id.delete(0, END)
        self.name.delete(0, END)
        self.email.delete(0, END)
        self.tel.delete(0, END)


interface = Tk()
interface.iconbitmap("ico_mm.ico")
interface.title("Usuários MM")
interface.geometry("800x270")
interface.wm_resizable(0, 0)
App(interface)
interface.mainloop()