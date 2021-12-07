import re

EMAIL = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')


def email_parse(email_address):
    email = EMAIL.findall(email_address)
    if email:
        name, address = email[0]
    else:
        raise ValueError(f'Адрес не валиден: {email_address}')
    print(name, address)


email_parse('someone@geekbrains.ru')
email_parse('someone.else@geekbrains.ru')
email_parse('someone@geekbrainsru')
