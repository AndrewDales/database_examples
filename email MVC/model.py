import re
import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base

# Base is called an Abstract Base Class - our SQL Alchemy models will inherit from this class
Base = declarative_base()


# Create an email database class
class EmailAddress(Base):
    __tablename__ = 'email'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    @sqlalchemy.orm.validates('email')
    def validate_email(self, key, address):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(pattern, address):
            raise ValueError('Invalid email address')
        return address

    def __repr__(self):
        return f"EmailAddress({self.email})"
