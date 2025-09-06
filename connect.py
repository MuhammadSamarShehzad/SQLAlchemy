from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os
load_dotenv()

key = os.getenv("db_key")

conn_str = key
 
engine = create_engine(conn_str, echo=True)  # echo=True to see the generated SQL statements in the console

# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE emp (id INT, name VARCHAR(20), salary INT)"))
#     conn.execute(text("INSERT INTO EMP (id, name, salary) values (:id, :name, :salary)"), 
#                  [{"id": 4, "name": "Kyrie", "salary": 4000}, {"id": 5, "name": "Irving", "salary": 3500}]
#                  )
#     conn.commit()  # need to commit when using connect bcz it does not auto commit

# with engine.begin() as conn:
#     conn.execute(text("INSERT INTO EMP (id, name, salary) values (:id, :name, :salary)"), 
#                  [{"id": 5, "name": "Irving", "salary": 3200}]
#                  )
      # no need to commit when using begin bcz it automatically commits if no errors


# with engine.begin() as conn:
#     result = conn.execute(text("SELECT * FROM EMP"))
#     for row in result:
#         print(row)