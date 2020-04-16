from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

# bcrypt = Bcrypt()
#
# password = 'supersecretpassword'
# hashed_password = bcrypt.generate_password_hash(password=password)
# print(hashed_password)
# print(bcrypt.check_password_hash(hashed_password, 'supersecretpassword'))

hashed_pass = generate_password_hash('supersecretpassword')
print(hashed_pass)
hash = check_password_hash(hashed_pass, 'supersecretpassword')
print(hash)