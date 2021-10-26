from db import DataBase


class Users:

    def __init__(self, id_user=0, name="", email="", tel=""):
        # self.info = {}
        self.id_user = id_user
        self.name = name
        self.email = email
        self.tel = tel

    def insertUser(self):

        sql = DataBase()
        try:

            c = sql.connection.cursor()

            c.execute("insert into users (name, email, tel) values ('" + self.name + "', '" +
                      self.tel + "', '" + self.email + "' )")

            sql.connection.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário."

    def updateUser(self):
        sql = DataBase()
        try:
            c = sql.connection.cursor()

            # c.execute("update users set name = '" + self.name + "', email = '" + self.email +
            # "', tel = '" + self.tel + "' where iduser = '" + str(self.id_user) + "' ")

            c.execute("update users set name = '" + self.name + "', tel = '" + self.tel + "', email = '" + self.email +
                "' where iduser = " + str(self.id_user) + " ")

            sql.connection.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

        sql = DataBase()
        try:
            c = sql.connection.cursor()

            c.execute("delete from users where iduser = '" + str(self.id_user) + "' ")

            sql.connection.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, iduser):
        sql = DataBase()
        try:
            c = sql.connection.cursor()

            c.execute("select * from users where iduser = '" + iduser + "' ")

            for linha in c:
                self.id_user = linha[0]
                self.name = linha[1]
                self.tel = linha[2]
                self.email = linha[3]

            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"


# teste = Users()
# teste.insertUser()
