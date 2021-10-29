from DB import DataBase


class Users:

    def __init__(self, id_user=0, name="", email="", tel="", postal_code="",
                 state="", city="", district="", street="", number="", residence_type=""):
        self.id_user = id_user
        self.name = name
        self.email = email
        self.tel = tel
        self.postal_code = postal_code
        self.state = state
        self.city = city
        self.district = district
        self.street = street
        self.number = number
        self.residence_type = residence_type

    def insert_user(self):

        sql = DataBase()
        try:

            c = sql.connection.cursor()

            c.execute(
                "insert into users (name, email, tel, postal_code, state, city, district, street,"
                "number, residence_type) values ('" + self.name + "', '" + self.email +
                "', '" + self.tel + "', '" + self.postal_code +
                "', '" + self.state + "', '" + self.city +
                "', '" + self.district + "', '" + self.street +
                "', '" + self.number + "', '" + self.residence_type + "' )")

            sql.connection.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário."

    def update_user(self):
        sql = DataBase()
        try:
            c = sql.connection.cursor()

            c.execute("update users set name = '" + self.name + "', email = '" + self.email +
                      "', tel = '" + self.tel + "', postal_code = '" + self.postal_code +
                      "', state = '" + self.state + "', city = '" + self.city +
                      "', district = '" + self.district + "', street = '" + self.street +
                      "', number = '" + self.number + "', residence_type = '" + self.residence_type +
                      "' where id_user = " + str(self.id_user) + " ")

            sql.connection.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def delete_user(self):

        sql = DataBase()
        try:
            c = sql.connection.cursor()

            c.execute("delete from users where id_user = '" + str(self.id_user) + "' ")

            sql.connection.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def select_user(self, id_user):
        sql = DataBase()
        try:
            c = sql.connection.cursor()

            c.execute("select * from users where id_user = '" + id_user + "' ")

            for linha in c:
                self.id_user = linha[0]
                self.name = linha[1]
                self.email = linha[2]
                self.tel = linha[3]
                self.postal_code = linha[4]
                self.state = linha[5]
                self.city = linha[6]
                self.district = linha[7]
                self.street = linha[8]
                self.number = linha[9]
                self.residence_type = linha[10]

            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
