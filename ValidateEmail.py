import re


class ValidateEmail:
    def __init__(self, email):
        self.tel = email

    def __str__(self):
        return self.format_email()

    def validate_return(self):
        if self.validate_email(self.tel):
            self.complete_email = self.tel
        else:
            return False

    def validate_email(self, email):
        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        answer = re.findall(pattern, email)
        if answer:
            return True
        else:
            return False

    def format_email(self):
        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        answer = re.search(pattern, self.complete_email)
        format_email = answer.group()
        return format_email