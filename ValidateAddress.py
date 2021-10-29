import requests


class ValidateAddress:

    @staticmethod
    def access_via_cep(postal_code):
        if len(postal_code) == 8 and postal_code.isnumeric():
            url = "https://viacep.com.br/ws/{}/json/".format(postal_code)
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
        else:
            return False
