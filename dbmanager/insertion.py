from sqlalchemy import insert, select
from dbmanager.models import User, Aim

from dbmanager.dbconfig import engine


def insert_user(user_ident: int, username: str):
    stmt = insert(User).values(user_ident=user_ident, username=username)

    with engine.connect() as conn:
        try:
            res = conn.execute(stmt)
            conn.commit()
        except Exception:
            print(f"Пользователь в базе данных!")


if __name__ == '__main__':
    insert_user(123123123, 'lolol')
