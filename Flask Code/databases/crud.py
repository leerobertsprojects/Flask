from basic import db, Puppy
## create

my_puppy = Puppy('Rufus', 10)
db.session.add(my_puppy)
db.session.commit()

## Reading

all_puppies = Puppy.query.all()
print(all_puppies)

# select by id

puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# filters

puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())

## Update

first_puppy = Puppy.query.get(1)
first_puppy.age = 20
db.session.add(first_puppy)
db.session.commit()
print(all_puppies)

## Delete

second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)
