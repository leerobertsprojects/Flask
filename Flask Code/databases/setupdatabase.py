from basic import db, Puppy

# creates all the tables model to an actual database table
db.create_all()
sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 5)

print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])

db.session.commit()




