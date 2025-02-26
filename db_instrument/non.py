from sqlalchemy import create_engine


engine = create_engine("sqlite+pysqlite:///new.db", echo=True, future=True)
