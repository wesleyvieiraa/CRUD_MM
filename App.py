from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk
import tkinter as Tkinter
from Users import Users
from Validators import Validate
from DB import DataBase


class App:
    def __init__(self, app=None):
        self.canvas = Frame(app, bg="#F5E3AB")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.container_header = Frame(self.canvas, bg="#FEC200", height=200)
        self.container_header.pack(fill="x", side=TOP)

        self.logo_xicoria = Label(self.container_header, bd=0)
        self.logo_xicoria.la = PhotoImage(file="Images/logo_xicoria.png")
        self.logo_xicoria["image"] = self.logo_xicoria.la
        self.logo_xicoria.place(x=200, y=0)

        self.container_main = Frame(self.canvas, height=250, width=1045, bg="#EBF4FC")
        self.container_main.pack(after=self.container_header, side=TOP)

        font = tkFont.Font(family="open-sans", size=11)

        self.text_id = Label(self.container_main,
                             text="ID de Usuário:",
                             font=font,
                             bg="#EBF4FC")
        self.text_id.place(x=50, y=25)

        self.id = Entry(self.container_main, width=5, justify="center")
        self.id.place(x=200, y=30)

        self.button_search = Button(self.container_main,
                                    bg="#EBF4FC",
                                    bd="0",
                                    command=self.search_user_in_fields)
        self.button_search.la = PhotoImage(file="Images/button_search.png")
        self.button_search["image"] = self.button_search.la
        self.button_search.place(x=250, y=25)

        self.text_name = Label(self.container_main,
                               text="*Nome Completo:",
                               font=font,
                               bg="#EBF4FC")
        self.text_name.place(x=50, y=60)

        self.name = Entry(self.container_main, width=40)
        self.name.place(x=200, y=65)

        self.text_email = Label(self.container_main,
                                text="*E-mail:",
                                font=font,
                                bg="#EBF4FC")
        self.text_email.place(x=50, y=90)

        self.email = Entry(self.container_main, width=40)
        self.email.place(x=200, y=95)

        self.text_tel = Label(self.container_main,
                              text="*Telefone:",
                              font=font,
                              bg="#EBF4FC")
        self.text_tel.place(x=50, y=120)

        self.tel = Entry(self.container_main, width=15)
        self.tel.place(x=200, y=125)

        self.text_warning_tel = Label(self.container_main,
                                      text="Insira apenas o DDD e número sem espaço",
                                      bg="#EBF4FC")
        self.text_warning_tel["font"] = ("open-sans", "8")
        self.text_warning_tel.place(x=300, y=120)

        self.text_postal_code = Label(self.container_main,
                                      text="*CEP:",
                                      font=font,
                                      bg="#EBF4FC")
        self.text_postal_code.place(x=630, y=25)

        self.postal_code = Entry(self.container_main, width=9)
        self.postal_code.place(x=700, y=30)

        self.button_search_cep = Button(self.container_main,
                                        bg="#EBF4FC",
                                        bd="0",
                                        command=self.search_address)
        self.button_search_cep.la = PhotoImage(file="Images/button_search.png")
        self.button_search_cep["image"] = self.button_search_cep.la
        self.button_search_cep.place(x=780, y=25)

        self.text_state = Label(self.container_main,
                                text="Estado:",
                                font=font,
                                bg="#EBF4FC")
        self.text_state.place(x=882, y=25)

        self.state = Entry(self.container_main, width=3, justify="center")
        self.state.place(x=952, y=30)

        self.text_city = Label(self.container_main,
                               text="Cidade:",
                               font=font,
                               bg="#EBF4FC")
        self.text_city.place(x=630, y=60)

        self.city = Entry(self.container_main, width=45)
        self.city.place(x=700, y=65)

        self.text_district = Label(self.container_main,
                                   text="Bairro:",
                                   font=font,
                                   bg="#EBF4FC")
        self.text_district.place(x=630, y=90)

        self.district = Entry(self.container_main, width=45)
        self.district.place(x=700, y=95)

        self.text_street = Label(self.container_main,
                                 text="Logradouro:",
                                 font=font,
                                 bg="#EBF4FC")
        self.text_street.place(x=630, y=120)

        self.street = Entry(self.container_main, width=40)
        self.street.place(x=730, y=125)

        self.text_number = Label(self.container_main,
                                 text="Número:",
                                 font=font,
                                 bg="#EBF4FC")
        self.text_number.place(x=630, y=150)

        self.number = Entry(self.container_main, width=6)
        self.number.place(x=730, y=155)

        self.text_residence_type = Label(self.container_main,
                                         text="Tipo:",
                                         font=font,
                                         bg="#EBF4FC")
        self.text_residence_type.place(x=782, y=150)

        self.residence_type = Entry(self.container_main, width=23)
        self.residence_type.place(x=833, y=155)

        self.button_insert = Button(self.container_main,
                                    bg="#EBF4FC",
                                    bd="0",
                                    command=self.insert_user)
        self.button_insert.la = PhotoImage(file="Images/button_insert.png")
        self.button_insert["image"] = self.button_insert.la
        self.button_insert.place(x=444, y=180)

        self.button_update = Button(self.container_main,
                                    bg="#EBF4FC",
                                    bd="0",
                                    command=self.update_user)
        self.button_update.la = PhotoImage(file="Images/button_update.png")
        self.button_update["image"] = self.button_update.la
        self.button_update.place(x=540, y=180)

        self.button_delete = Button(self.container_main,
                                    bg="#EBF4FC",
                                    bd="0",
                                    command=self.delete_user)
        self.button_delete.la = PhotoImage(file="Images/button_delete.png")
        self.button_delete["image"] = self.button_delete.la
        self.button_delete.place(x=640, y=180)

        self.container_footer = Frame(self.canvas, bg="#FEC200", height=100)
        self.container_footer.pack(fill="x", side=BOTTOM)

        self.logo_mm = Label(self.container_footer, bd=0)
        self.logo_mm.la = PhotoImage(file="Images/logo_mm.png")
        self.logo_mm["image"] = self.logo_mm.la
        self.logo_mm.pack()

        self.container2_main = Frame(self.canvas, height=50, width=1045, bg="#EBF4FC")
        self.container2_main.pack()

        self.text_search_name = Label(self.container2_main,
                                      text="Procurar Nome:",
                                      font=font,
                                      bg="#EBF4FC")
        self.text_search_name.place(x=50, y=10)

        self.search = Entry(self.container2_main, width=40)
        self.search.place(x=170, y=10, height=25)

        self.button_search_tree = Button(self.container2_main,
                                         bg="#EBF4FC",
                                         bd="0",
                                         command=self.search_user_in_tree)
        self.button_search_tree.la = PhotoImage(file="Images/button_search_tree.png")
        self.button_search_tree["image"] = self.button_search_tree.la
        self.button_search_tree.place(x=440, y=10)

        self.button_select = Button(self.container2_main,
                                    bg="#EBF4FC",
                                    bd="0",
                                    command=self.select_user)
        self.button_select.la = PhotoImage(file="Images/button_select.png")
        self.button_select["image"] = self.button_select.la
        self.button_select.place(x=550, y=10)

        self.button_show = Button(self.container2_main,
                                  bg="#EBF4FC",
                                  bd="0",
                                  command=self.populate)
        self.button_show.la = PhotoImage(file="Images/button_show.png")
        self.button_show["image"] = self.button_show.la
        self.button_show.place(x=665, y=10)

        self.container3_main = Frame(self.canvas, bg="#EBF4FC")
        self.container3_main.pack(fill="y", expand=True)

        self.tree = ttk.Treeview(self.container3_main, columns=(
            "ID", "Nome", "E-mail", "Telefone", "CEP", "Estado", "Cidade", "Bairro", "Logradouro", "Número", "Tipo"),
                                 show="headings")

        self.scrollbar = ttk.Scrollbar(self.container3_main, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side='right', fill="y")

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.column("ID", minwidth=50, width=35, anchor=Tkinter.CENTER)
        self.tree.column("Nome", minwidth=0, width=150, anchor=Tkinter.CENTER)
        self.tree.column("E-mail", minwidth=0, width=180, anchor=Tkinter.CENTER)
        self.tree.column("Telefone", minwidth=0, width=80, anchor=Tkinter.CENTER)
        self.tree.column("CEP", minwidth=0, width=70, anchor=Tkinter.CENTER)
        self.tree.column("Estado", minwidth=0, width=30, anchor=Tkinter.CENTER)
        self.tree.column("Cidade", minwidth=0, width=100, anchor=Tkinter.CENTER)
        self.tree.column("Bairro", minwidth=0, width=80, anchor=Tkinter.CENTER)
        self.tree.column("Logradouro", minwidth=0, width=165, anchor=Tkinter.CENTER)
        self.tree.column("Número", minwidth=0, width=35, anchor=Tkinter.CENTER)
        self.tree.column("Tipo", minwidth=0, width=100, anchor=Tkinter.CENTER)

        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("E-mail", text="E-mail")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("CEP", text="CEP")
        self.tree.heading("Estado", text="UF")
        self.tree.heading("Cidade", text="Cidade")
        self.tree.heading("Bairro", text="Bairro")
        self.tree.heading("Logradouro", text="Logradouro")
        self.tree.heading("Número", text="N°")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.pack(fill="y", expand=True)

        self.populate()

    def insert_user(self):
        email = self.email.get()
        tel = self.tel.get()
        validator_object = Validate()

        if self.validator() == True:
            user = Users()
            user.name = self.name.get()
            user.email = validator_object.validate_email(email)
            user.email = validator_object.validate_email(email)
            user.tel = validator_object.validate_tel(tel)
            user.postal_code = self.postal_code.get()
            user.state = self.state.get()
            user.city = self.city.get()
            user.district = self.district.get()
            user.street = self.street.get()
            user.number = self.number.get()
            user.residence_type = self.residence_type.get()
            messagebox.showinfo(title="Aviso", message=user.insert_user())
            self.delete_fields()
            self.populate()
            self.id.focus()
        else:
            messagebox.showinfo(title="Aviso", message=self.validator())

    def update_user(self):
        email = self.email.get()
        tel = self.tel.get()
        validator_object = Validate()

        if self.validator() == True:
            user = Users()
            user.id_user = self.id.get()
            user.name = self.name.get()
            user.email = validator_object.validate_email(email)
            user.tel = validator_object.validate_tel(tel)
            user.postal_code = self.postal_code.get()
            user.state = self.state.get()
            user.city = self.city.get()
            user.district = self.district.get()
            user.street = self.street.get()
            user.number = self.number.get()
            user.residence_type = self.residence_type.get()
            messagebox.showinfo(title="Aviso", message=user.update_user())
            self.delete_fields()
            self.populate()
        else:
            messagebox.showinfo(title="Aviso", message=self.validator())

    def delete_user(self):
        user = Users()

        try:
            selected_item = self.tree.selection()[0]
            values = self.tree.item(selected_item, "values")
            user.id_user = values[0]
            try:
                messagebox.showinfo(title="Aviso", message=user.delete_user())
                self.id.focus()
            except:
                messagebox.showinfo(title="ERRO", message="Erro ao deletar")
                return
            self.tree.delete(selected_item)
            self.populate()
        except:
            user.id_user = self.id.get()
            if user.id_user != "":
                messagebox.showinfo(title="Aviso", message=user.delete_user())
                self.id.focus()
                self.delete_fields()
                self.populate()
            else:
                messagebox.showinfo(title="Aviso", message="Insira um ID ou selecione um usuário válido")

    def search_user_in_fields(self):
        user = Users()
        id_user = self.id.get()

        if id_user.isnumeric() and not id_user == "":
            self.delete_fields()
            messagebox.showinfo(title="Aviso", message=user.select_user(id_user))
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
            self.id.focus()
        else:
            messagebox.showinfo(title="Aviso", message="ID inválido")

    def search_user_in_tree(self):
        self.tree.delete(*self.tree.get_children())
        query = "SELECT * FROM users WHERE name LIKE '%" + self.search.get() + "%'"
        sql = DataBase()
        row = sql.dql(query)
        for i in row:
            self.tree.insert("", "end", values=i)

    def select_user(self):
        user = Users()
        try:
            self.delete_fields()
            selected_item = self.tree.selection()[0]
            values = self.tree.item(selected_item, "values")
            id_user = values[0]
            user.select_user(id_user)
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
            for item in self.tree.selection():
                self.tree.selection_remove(item)
            self.name.focus()
        except:
            return messagebox.showinfo(title="Aviso", message="Selecione um usuário")

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
        validator_object = Validate()
        self.state.delete(0, END)
        self.city.delete(0, END)
        self.district.delete(0, END)
        self.street.delete(0, END)

        try:
            validator_object.access_via_cep(postal_code)
            uf, city, district, street = validator_object.access_via_cep(postal_code)

            self.state.insert(INSERT, uf)
            self.city.insert(INSERT, city)
            self.district.insert(INSERT, district)
            self.street.insert(INSERT, street)

            self.number.focus()
        except:
            messagebox.showinfo(title="Aviso", message="CEP inválido")

    def validator(self):
        email = self.email.get()
        tel = self.tel.get()
        postal_code = self.postal_code.get()
        validator_object = Validate()

        if not validator_object.validate_email(email):
            return "E-mail inválido"
        elif not validator_object.validate_tel(tel):
            return "Telefone inváldo"
        elif not validator_object.access_via_cep(postal_code):
            return "CEP inválido"
        else:
            return True

    def populate(self):
        self.tree.delete(*self.tree.get_children())
        query = "SELECT * FROM users order by id_user"
        sql = DataBase()
        cursor = sql.dql(query)
        for i in cursor:
            self.tree.insert("", "end", values=i)


root = Tk()
root.iconbitmap("Images/ico_mm.ico")
root.title("Usuários MM")
root.state('zoomed')
App(root)
root.mainloop()
