from django.core.exceptions import ValidationError


def check_price(value):
    if value < 0:
        raise ValidationError("Cena nie może być mniejsza niż zero")

def check_length(value):
    if len(value) < 3:
        raise ValidationError("za krótkie")

def check_if_mail(value):
    if '@' not in value:
        raise ValidationError("a gdzie małpa Cholero!!!")