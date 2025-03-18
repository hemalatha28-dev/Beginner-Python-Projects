import random, string

letters = string.ascii_letters
digits = string.digits
special_chars = "!@#$&_"

password = random.choice(digits)

password += random.choice(special_chars)

password += "".join(random.choices(letters, k=6))

final_password = "".join(random.sample(password, 8))

print(final_password)
