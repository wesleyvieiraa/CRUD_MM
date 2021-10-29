import requests


class ValidateAddress:

    def __init__(self, postal_code):
        self.postal_code = str(postal_code)

    def validate_return(self):
        if self.valid_postal_code(self.postal_code):
            self.postal_code = self.postal_code
            return True
        else:
            return False

    def valid_postal_code(self, postal_code):
        if len(postal_code) == 8:
            return True
        else:
            return False

    def access_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.postal_code)
        r = requests.get(url)
        address = r.json()

        if "erro" in address:
            return False
        else:
            return (
                address["uf"],
                address["localidade"],
                address["bairro"],
                address["logradouro"]
            )
