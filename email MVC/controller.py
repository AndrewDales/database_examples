from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import EmailAddress


class Controller:
    def __init__(self):
        # self.view = view
        self.engine = create_engine('sqlite:///emails.sqlite', echo=True)

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # create an EmailAddress object and save it to the database
            with Session(self.engine) as sess:
                email_address = EmailAddress(email=email)
                sess.add(email_address)
                sess.commit()

            # show a success message
            return f'The email {email} saved!'

        except ValueError as error:
            # raise the error message
            raise ValueError(error)

    def get_emails(self):
        """
        Get all emails
        :return:
        """
        with Session(self.engine) as sess:
            emails = sess.query(EmailAddress).order_by(EmailAddress.email).all()
            return [email.email for email in emails]
