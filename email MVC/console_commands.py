from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import EmailAddress

engine = create_engine('sqlite:///emails.sqlite', echo=True)
