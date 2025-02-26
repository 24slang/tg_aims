from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

from db_instrument.non import engine


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(20), nullable=False)
    fullname = Column(String(20), nullable=False)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f'User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})'


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, nullable=False)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f'Address(id={self.id!r}, email_address={self.email_address!r})'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
