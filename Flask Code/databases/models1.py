from models import db, Puppy, Toy, Owner

# create 2 puppys
rufus = Puppy('Rufus')
fido = Puppy('fido')
db.session.add_all([rufus, fido])
db.session.commit()

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

#create an owner object

jose = Owner('Jose', rufus.id)
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

## give rufus toys

toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

rufus.report_toys()
