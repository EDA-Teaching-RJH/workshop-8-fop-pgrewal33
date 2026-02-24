import re

number = input("what is your number? ")

if re.search(r"^\D$", number ):
    print("valid")