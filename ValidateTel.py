import re


class ValidateTel:

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
