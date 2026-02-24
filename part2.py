import re

email = input("What's your email? ").strip()
if re.search(r".+@.+\.ac.uk", email):
    print("valid")
else:
    print("invalid")