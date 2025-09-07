from sqlalchemy import select
from connect import engine
from sqlalchemy.orm import Session
from models import User, Address

with Session(engine) as session:
    stmlt = select(User)
    users = session.scalars(stmlt).all()
    for user in users:
        print(user)