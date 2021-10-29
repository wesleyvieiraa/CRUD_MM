from tkinter import *
import tkinter.font as tkFont

from Users import Users
from ValidateEmail import ValidateEmail
from ValidateTel import ValidateTel
from ValidateAddress import ValidateAddress


class App:
    def __init__(self, interface=None):
        self.canvas = Frame(interface, bg="#F5E3AB")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.container_header = Frame(self.canvas, bg="#fec200", height="200")
        self.container_header.pack(fill="x", side=TOP)

        self.logo_xicoria = Label(self.container_header, bd=0)
        self.logo_xicoria.la = PhotoImage(file="Images/logo_xicoria.png")
        self.logo_xicoria["image"] = self.logo_xicoria.la
        self.logo_xicoria.place(x=200, y=0)

        self.container_main = Frame(self.canvas)
        self.container_main.pack(fill="y", expand=True)

        font = tkFont.Font(family="open-sans", size=11)

        self.text_personal = Label(self.container_main, text="Informações pessoais:", width=40)
        self.text_personal["font"] = ("open-sans", "15", "bold")
        self.text_personal.grid(row=0, column=0, sticky="we")

        self.text_id = Label(self.container_main,
                             text="ID de Usuário:",
                             font=font)
        self.text_id.place(x=50, y=55)

        self.id = Entry(self.container_main, width="5", justify="center")
        self.id.place(x=200, y=60)

        self.button_search = Button(self.container_main,
                                    bg="#f0f0f0",
                                    bd="0",
                                    command=self.search_user)
        self.button_search.la = PhotoImage(file="Images/button_search.png")
        self.button_search["image"] = self.button_search.la
        self.button_search.place(x=250, y=55)

        self.text_name = Label(self.container_main,
                               text="*Nome Completo:",
                               font=font)
        self.text_name.place(x=50, y=90)

        self.name = Entry(self.container_main, width="40")
        self.name.place(x=200, y=95)

        self.text_email = Label(self.container_main,
                                text="*E-mail:",
                                font=font)
        self.text_email.place(x=50, y=120)

        self.email = Entry(self.container_main, width="40")
        self.email.place(x=200, y=125)

        self.text_tel = Label(self.container_main,
                              text="*Telefone:",
                              font=font)
        self.text_tel.place(x=50, y=150)

        self.tel = Entry(self.container_main, width="15")
        self.tel.place(x=200, y=155)

        self.text_warning_tel = Label(self.container_main, text="Insira apenas o DDD e número sem espaço")
        self.text_warning_tel["font"] = ("open-sans", "8")
        self.text_warning_tel.place(x=300, y=150)

        self.text_address = Label(self.container_main, text="Endereço:", width=40)
        self.text_address["font"] = ("open-sans", "15", "bold")
        self.text_address.grid(row=0, column=1, sticky="we")

        self.text_postal_code = Label(self.container_main,
                                      text="CEP:",
                                      font=font)
        self.text_postal_code.place(x=550, y=55)

        self.postal_code = Entry(self.container_main, width="9")
        self.postal_code.place(x=620, y=60)

        self.button_search_cep = Button(self.container_main,
                                        bg="#f0f0f0",
                                        bd="0",
                                        command=self.search_address)
        self.button_search_cep.la = PhotoImage(file="Images/button_search.png")
        self.button_search_cep["image"] = self.button_search_cep.la
        self.button_search_cep.place(x=700, y=55)

        self.text_state = Label(self.container_main,
                                text="Estado:",
                                font=font)
        self.text_state.place(x=802, y=55)

        self.state = Entry(self.container_main, width="3", justify="center")
        self.state.place(x=872, y=60)

        self.text_city = Label(self.container_main,
                               text="Cidade:",
                               font=font)
        self.text_city.place(x=550, y=90)

        self.city = Entry(self.container_main, width="45")
        self.city.place(x=620, y=95)

        self.text_district = Label(self.container_main,
                                   text="Bairro:",
                                   font=font)
        self.text_district.place(x=550, y=120)

        self.district = Entry(self.container_main, width="45")
        self.district.place(x=620, y=125)

        self.text_street = Label(self.container_main,
                                 text="Logradouro:",
                                 font=font)
        self.text_street.place(x=550, y=150)

        self.street = Entry(self.container_main, width="40")
        self.street.place(x=650, y=155)

        self.text_number = Label(self.container_main,
                                 text="Número:",
                                 font=font)
        self.text_number.place(x=550, y=180)

        self.number = Entry(self.container_main, width="6")
        self.number.place(x=650, y=185)

        self.text_residence_type = Label(self.container_main,
                                         text="Tipo:",
                                         font=font)
        self.text_residence_type.place(x=702, y=180)

        self.residence_type = Entry(self.container_main, width="23")
        self.residence_type.place(x=753, y=185)

        self.answer = Label(self.container_main, width="30", fg="red", justify="center")
        self.answer.place(x=400, y=220)

        self.button_insert = Button(self.container_main,
                                    bg="#f0f0f0",
                                    bd="0",
                                    command=self.insert_user)
        self.button_insert.la = PhotoImage(file="Images/button_insert.png")
        self.button_insert["image"] = self.button_insert.la
        self.button_insert.place(x=370, y=250)

        self.button_update = Button(self.container_main,
                                    bg="#f0f0f0",
                                    bd="0",
                                    command=self.update_user)
        self.button_update.la = PhotoImage(file="Images/button_update.png")
        self.button_update["image"] = self.button_update.la
        self.button_update.place(x=460, y=250)

        self.button_delete = Button(self.container_main,
                                    bg="#f0f0f0",
                                    bd="0",
                                    command=self.delete_user)
        self.button_delete.la = PhotoImage(file="Images/button_delete.png")
        self.button_delete["image"] = self.button_delete.la
        self.button_delete.place(x=554, y=250)

        self.container_footer = Frame(self.canvas, bg="#fec200", height="100")
        self.container_footer.pack(fill="x", side=BOTTOM)

        self.logo_mm = Label(self.container_footer, bd=0)
        self.logo_mm.la = PhotoImage(file="Images/logo_mm.png")
        self.logo_mm["image"] = self.logo_mm.la
        self.logo_mm.pack()

    def insert_user(self):
        email = self.email.get()
        tel = self.tel.get()
        postal_code = self.postal_code.get()
        email_object = ValidateEmail()
        tel_object = ValidateTel()
        postal_code_object = ValidateAddress()

        if email_object.validate_email(email) \
                and tel_object.validate_tel(tel) \
                and postal_code_object.access_via_cep(postal_code):
            self.answer["text"] = ""
            user = Users()
            user.name = self.name.get()
            user.email = email_object.validate_email(email)
            user.tel = tel_object.validate_tel(tel)
            user.postal_code = self.postal_code.get()
            user.state = self.state.get()
            user.city = self.city.get()
            user.district = self.district.get()
            user.street = self.street.get()
            user.number = self.number.get()
            user.residence_type = self.residence_type.get()
            self.answer["text"] = user.insert_user()
            self.delete_fields()
        else:
            self.answer["text"] = "E-mail e/ou telefone inválido"

    def update_user(self):
        email = self.email.get()
        email_object = ValidateEmail()
        tel = self.tel.get()
        tel_object = ValidateTel()
        postal_code = self.postal_code.get()
        postal_code_object = ValidateAddress()

        if email_object.validate_email(email) \
                and tel_object.validate_tel(tel) \
                and postal_code_object.access_via_cep(postal_code):
            user = Users()
            user.id_user = self.id.get()
            user.name = self.name.get()
            user.email = email_object.validate_email(email)
            user.tel = tel_object.validate_tel(tel)
            user.postal_code = self.postal_code.get()
            user.state = self.state.get()
            user.city = self.city.get()
            user.district = self.district.get()
            user.street = self.street.get()
            user.number = self.number.get()
            user.residence_type = self.residence_type.get()
            self.answer["text"] = user.update_user()
            self.delete_fields()
        else:
            self.answer["text"] = "E-mail e/ou telefone inválido"

    def delete_user(self):
        user = Users()

        user.id_user = self.id.get()

        if user.id_user != "":
            self.answer["text"] = ""
            self.answer["text"] = user.delete_user()
            self.delete_fields()
        else:
            self.answer["text"] = "Insira um id de usuário válido"

    def search_user(self):
        user = Users()
        id_user = self.id.get()

        if id_user == "":
            self.answer["text"] = "Insira um id de usuário"
        else:
            self.answer["text"] = user.select_user(id_user)
            self.delete_fields()

            self.id.insert(INSERT, user.id_user)
            self.name.insert(INSERT, user.name)
            self.email.insert(INSERT, user.email)
            self.tel.insert(INSERT, user.tel)
            self.postal_code.insert(INSERT, user.postal_code)
            self.state.insert(INSERT, user.state)
            self.city.insert(INSERT, user.city)
            self.district.insert(INSERT, user.district)
            self.street.insert(INSERT, user.street)
            self.number.insert(INSERT, user.number)
            self.residence_type.insert(INSERT, user.residence_type)

    def delete_fields(self):
        self.id.delete(0, END)
        self.name.delete(0, END)
        self.email.delete(0, END)
        self.tel.delete(0, END)
        self.postal_code.delete(0, END)
        self.state.delete(0, END)
        self.city.delete(0, END)
        self.district.delete(0, END)
        self.street.delete(0, END)
        self.number.delete(0, END)
        self.residence_type.delete(0, END)

    def search_address(self):
        postal_code = self.postal_code.get()
        postal_code_object = ValidateAddress()

        if postal_code_object.access_via_cep(postal_code):
            self.answer["text"] = ""
            uf, city, district, street = postal_code_object.access_via_cep(postal_code)

            self.state.insert(INSERT, uf)
            self.city.insert(INSERT, city)
            self.district.insert(INSERT, district)
            self.street.insert(INSERT, street)

            self.number.focus_set()
        else:
            self.state.delete(0, END)
            self.city.delete(0, END)
            self.district.delete(0, END)
            self.street.delete(0, END)
            self.answer["text"] = "CEP inválido"


interface = Tk()
interface.iconbitmap("Images/ico_mm.ico")
interface.title("Usuários MM")
interface.geometry("1300x700")
App(interface)
interface.mainloop()
