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

