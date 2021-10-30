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
            query = "INSERT INTO users (name, email, tel, postal_code, state, city, district, street, number, " \
                    "residence_type) values ('" + self.name + "', '" + self.email + \
                    "', '" + self.tel + "', '" + self.postal_code + \
                    "', '" + self.state + "', '" + self.city + \
                    "', '" + self.district + "', '" + self.street + \
                    "', '" + self.number + "', '" + self.residence_type + "' )"
            sql.dml(query)
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário."

    def update_user(self):
        sql = DataBase()
        try:
            query = "update users set name = '" + self.name + "', email = '" + self.email + "', tel = '" + self.tel + \
                    "', postal_code = '" + self.postal_code + "', state = '" + self.state + \
                    "', city = '" + self.city + "', district = '" + self.district + \
                    "', street = '" + self.street + "', number = '" + self.number + \
                    "', residence_type = '" + self.residence_type + "' where id_user = " + str(self.id_user) + " "
            sql.dml(query)
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def delete_user(self):

        sql = DataBase()
        try:
            query = "delete from users where id_user = '" + str(self.id_user) + "' "
            sql.dml(query)
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def select_user(self, id_user):
        sql = DataBase()
        try:
            query = "select * from users where id_user = '" + id_user + "' "
            cursor = sql.dql(query)

            for row in cursor:
                self.id_user = row[0]
                self.name = row[1]
                self.email = row[2]
                self.tel = row[3]
                self.postal_code = row[4]
                self.state = row[5]
                self.city = row[6]
                self.district = row[7]
                self.street = row[8]
                self.number = row[9]
                self.residence_type = row[10]
            return "Usuário buscado com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
