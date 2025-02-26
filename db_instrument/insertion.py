from sqlalchemy import insert
from dbcreator import User, Address
from db_instrument.non import engine


def insert_user_address(name: str, fullname: str, email: str) -> None:
    user_insertion = insert(User).values(name=name, fullname=fullname)

    with engine.connect() as conn:
        result = conn.execute(user_insertion)
        conn.commit()

        user_id = result.inserted_primary_key[0]

        address_insertion = insert(Address).values(email_address=email, user_id=user_id)
        conn.execute(address_insertion)
        conn.commit()


if __name__ == '__main__':
    insert_user_address("Stepa", "Vasiliev", "vasiliev@mail.ru")
