from passlib.hash import sha256_crypt

password = sha256_crypt.hash("12345")
password2 = sha256_crypt.hash("12345")

print(password)
print(password2)

print(sha256_crypt.verify("12345", "$5$rounds=535000$5aa.vNb8NW4nzNTv$yr3Fuz3dOEmj1XRQXdxCHm8aZdKa0S/8KCKqsloXz5B"))
