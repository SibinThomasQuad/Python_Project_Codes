class InputValidator:
    @staticmethod
    def is_empty(value):
        return not value

    @staticmethod
    def is_numeric(value):
        return str(value).isnumeric()

    @staticmethod
    def is_valid_email(value):
        import re
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_pattern, value)

    @staticmethod
    def is_valid_username(value):
        import re
        username_pattern = r'^[a-zA-Z0-9]+$'
        return re.match(username_pattern, value)

    @staticmethod
    def has_min_length(value, min_length):
        return len(value) >= min_length

    @staticmethod
    def is_alpha(value):
        return str(value).isalpha()

    @staticmethod
    def is_digit(value):
        return str(value).isdigit()

    @staticmethod
    def is_alpha_numeric(value):
        return str(value).isalnum()

    @staticmethod
    def is_strong_password(value):
        import re
        password_pattern = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^\w\s]).{8,}$'
        return re.match(password_pattern, value)
