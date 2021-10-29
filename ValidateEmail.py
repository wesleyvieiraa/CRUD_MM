import re


class ValidateEmail:

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
