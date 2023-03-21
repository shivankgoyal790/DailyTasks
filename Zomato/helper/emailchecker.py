import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def validemailcheck():
    email = input("ENTER YOUR VALID EMAIL ")
    while re.search(regex, email) == None:
        email = input("ENTER YOUR VALID EMAIL ")

    return email
