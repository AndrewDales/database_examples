from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import EmailAddress


class Controller:
    def __init__(self, view):
        self.view = view
        self.engine = create_engine('sqlite:///emails.sqlite', echo=True)

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # create an email address object
            with Session(self.engine) as sess:
                email = EmailAddress(email=email)
                sess.add(email)
                sess.commit()

                # show a success message
                self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)