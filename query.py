from connect import engine
from sqlalchemy import text
from logger import logger
from sqlalchemy.orm import Session

# with engine.begin() as conn:
#     conn.execute(text("DELETE FROM emp WHERE ctid NOT IN (SELECT MIN(ctid) FROM emp GROUP BY id);"))


# with engine.begin() as conn:
#     result = conn.execute(text("SELECT * FROM EMP"))
#     rows = result.fetchall()
#     logger.info(f"Fetched all records from EMP table.\n {rows}")
#     for row in rows:
#         print(row)


from models import Base, User, Address
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

with Session(engine) as session:
    # Create a user
    u1 = User(id=2, name="John Doe")

    # Create two addresses for that user
    a1 = Address(email="alice@example.com", user=u1)
    a2 = Address(email="alice.doe@example.com", user=u1)

    # Add everything
    session.add_all([u1, a1, a2])
    session.commit()

    # Query all users
    users = session.query(User).all()
    print(users)           # shows User objects

    # Query addresses
    addresses = session.query(Address).all()
    print(addresses)       # shows Address objects

    # Access addresses from user
    print(users[0].addresses)   # list of Alice's addresses

