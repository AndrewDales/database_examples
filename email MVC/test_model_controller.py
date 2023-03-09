import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from controller import Controller
from model import Base, EmailAddress


class TestModel:
    @pytest.fixture()
    def setup_db(self):
        engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(engine)
        with Session(engine) as sess:
            yield sess

    def test_email(self, setup_db):
        email = EmailAddress(email='andrew@dales.com')
        assert email.email == 'andrew@dales.com'

    def test_database(self, setup_db):
        sess = setup_db
        emails = [EmailAddress(email='andrew@dales.com'),
                  EmailAddress(email='eleonora@font.co.uk')]
        sess.add_all(emails)
        sess.commit()
        assert sess.query(EmailAddress).count() == 2
        email = sess.query(EmailAddress).first()
        assert email.email == 'andrew@dales.com'


class TestController:
    @pytest.fixture()
    def setup_controller(self):
        controller = Controller(':memory:')
        Base.metadata.create_all(controller.engine)
        return controller

    def test_save(self, setup_controller):
        controller = setup_controller
        temp_email = 'bill@ms.com'
        save_message = controller.save(temp_email)
        assert save_message == f"The email {temp_email} saved!"

    def test_save_wrong_email(self, setup_controller):
        controller = setup_controller
        with pytest.raises(ValueError) as error:
            controller.save('not_correct')
            assert str(error.value) == 'Invalid email address'

    def test_get_emails(self, setup_controller):
        controller = setup_controller
        controller.save('bill@ms.com')
        controller.save('steve@apple.com')
        emails = controller.get_emails()
        assert emails == ['bill@ms.com', 'steve@apple.com']
