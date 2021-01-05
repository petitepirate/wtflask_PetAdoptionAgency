from models import Pet, db
from app import app

db.drop_all()
db.create_all()

p1 = Pet(name="Banana Waffles", species="dog", photo_url="https://images.unsplash.com/photo-1534361960057-19889db9621e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=450&q=80",
         age=3, notes="rescue pup!")
p2 = Pet(name="Alfred", species="cat", photo_url="https://images.unsplash.com/photo-1574144611937-0df059b5ef3e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=80", age=2,
         notes="not an asshole cat!")
p3 = Pet(name="Mr. Poke", species="hedgehog", photo_url="https://images.unsplash.com/photo-1534278931827-8a259344abe7?ixlib=rb-1.2.1&auto=format&fit=crop&w=450&q=80",
         age=5, notes="sonic's brother")



db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.commit()
