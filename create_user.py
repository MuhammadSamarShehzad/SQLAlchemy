from sqlalchemy.orm import Session
from connect import engine
from models import User, Address

with Session(engine) as session:
    Saif = User(
        id = 7,
        name = 'Saif',
        addresses = [Address(email="saif@gmail.com"), Address(email="saif.khan@yahoo.com")]
    )

    Aftab = User(
        name = 'Aftab Ali',
    )

    session.add_all([Saif, Aftab])
    session.commit()