from string import ascii_lowercase, digits
import re


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits + " "

    @classmethod
    def check_card_number(cls, number):
        pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
        checker = re.match(pattern, number)
        if checker:
            return True
        else:
            return False

    @classmethod
    def check_card_name(cls, name):

        if not set(name) < set(cls.CHARS_FOR_NAME):
            raise ValueError("некоректное поле name")


is_number = CardCheck.check_card_number("1234-1234-1234-1234")
is_name = CardCheck.check_card_name("SERGEI BALAKEREV")
