from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import Base, EmailAddress

engine = create_engine('sqlite:///emails.sqlite', echo=True)
# Base.metadata.create_all(engine)

with Session(engine) as sess:
    email_wrong = EmailAddress(email='not_correct')
    email = EmailAddress(email='andrew.dales@ms.com')
    sess.add(email)
    sess.commit()
