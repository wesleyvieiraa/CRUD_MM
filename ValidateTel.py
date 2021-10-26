import re


class ValidateTel:
    def __init__(self, tel):
        self.tel = tel

    def __str__(self):
        return self.format_number()

    def validate_return(self):
        if self.validate_tel(self.tel):
            self.number = self.tel
        else:
            return False

    def validate_tel(self, tel):
        pattern = "([0-9]{2})([0-9]{5})([0-9]{4})"
        answer = re.findall(pattern, tel)
        if answer:
            return True
        else:
            return False

    def format_number(self):
        pattern = "([0-9]{2})([0-9]{5})([0-9]{4})"
        answer = re.search(pattern, self.number)
        format_number = "({}){}-{}".format(answer.group(1), answer.group(2), answer.group(3))
        return format_number
