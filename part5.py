import re

number = input("what is your number? ")

if re.search(r"^\d+[07]+{9}+$", number ):
    print("valid")
else:
    print("invalid")