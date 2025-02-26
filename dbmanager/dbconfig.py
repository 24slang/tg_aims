from sqlalchemy import create_engine


engine = create_engine("sqlite+pysqlite:///tg_users.db", echo=True, future=True)
