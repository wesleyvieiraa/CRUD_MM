import re
import requests


class Validate:

    @staticmethod
    def validate_email(email):
        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        answer = re.findall(pattern, email)
        if answer:
            search = re.search(pattern, email)
            format_email = search.group()
            return format_email
        else:
            return False

    @staticmethod
    def validate_tel(tel):
        pattern = "^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$"
        answer = re.findall(pattern, tel)
        if answer:
            search = re.search(pattern, tel)
            number = search.group()
            return number
        else:
            return False

    @staticmethod
    def access_via_cep(postal_code):
        if len(postal_code) == 8 and postal_code.isnumeric():
            url = "https://viacep.com.br/ws/{}/json/".format(postal_code)
            r = requests.get(url)
            address = r.json()

            try:
                return (
                    address["uf"],
                    address["localidade"],
                    address["bairro"],
                    address["logradouro"]
                )
            except:
                return False
        else:
            return False
