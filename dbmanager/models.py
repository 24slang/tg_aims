from sqlalchemy import String, Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from dbmanager.dbconfig import engine


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    user_ident = Column(Integer, nullable=False, unique=True)
    username = Column(String)

    aims = relationship("Aim", back_populates="user")

    def __repr__(self):
        return f'User(id={self.id!r}, user_id={self.user_ident!r}, username={self.username!r})'


class Aim(Base):
    __tablename__ = 'aims'
    id = Column(Integer, primary_key=True)
    aim = Column(String)
    description = Column(Text)
    is_ready = Column(Boolean)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="aims")

    def __repr__(self):
        return (f'Aim(id={self.id!r}, aim={self.aim!r}, '
                f'description={self.description!r}, '
                f'is_ready={self.is_ready!r},'
                f'user_id={self.user_id!r})')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
