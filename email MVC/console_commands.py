from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import EmailAddress

engine = create_engine('sqlite:///emails.sqlite', echo=True)

with Session(engine) as sess:
    # This line will raise an error
    # email_wrong = EmailAddress(email='not_correct')
    email = EmailAddress(email='andrew.dales@ms.com')
    sess.add(email)
    sess.commit()
