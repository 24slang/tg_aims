from sqlalchemy import select, literal_column, and_, or_
from dbcreator import User
from non import engine
from sqlalchemy.orm import Session


stmt = select(literal_column("'Инфо о пользователе'").label("i"), User).where(User.name == "Uladzislau")
print(stmt)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.i}: name={row.name}, fullname={row.fullname}, id={row.id}")


# OUTPUT:
#     SELECT "user".id, "user".name, "user".fullname
#     FROM "user"
#     WHERE "user".name = :name_1

with Session(engine) as session:
    row = session.execute(stmt).first()
    print(row)
# OUTPUT: (User(id=1, name='Uladzislau', fullname='Shyshko'),)

#
# with engine.connect() as conn:
#     for row in conn.execute(stmt):
#         print(row)
#
# # OUTPUT: (1, 'Uladzislau', 'Shyshko')
