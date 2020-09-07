import pytest

from libpythonpro_doug.spam.email_sender import Sender
from libpythonpro_doug.spam.main import SpamSender
from libpythonpro_doug.spam.models import User


class SenderMock(Sender):

    def __init__(self):
        super().__init__()
        self.num_of_sent_emails = 0
        self.sent_params = None

    def send(self, shipper, recipient, title, body):
        self.sent_params = (shipper, recipient, title, body)
        self.num_of_sent_emails += 1


@pytest.mark.parametrize(
    'users',
    [
        [
            User(name='Doug', email='douglas.fraga@gmail.com'),
            User(name='Carol', email='caroldanelli@gmail.com')
        ],
        [
            User(name='Doug', email='douglas.fraga@gmail.com')
        ]
    ]
)
def test_number_of_spam(session, users):
    for user in users:
        session.save(user)
    sender = SenderMock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_emails(
        'douglas.fraga@gmail.com',
        'Python Pro Training Course',
        'Email body'
    )
    assert len(users) == sender.num_of_sent_emails

    def test_spam_params(session):
        user = User(name='Doug', email='douglas.fraga@gmail.com')
        session.save(user)
        sender = SenderMock()
        spam_sender = SpamSender(session, sender)
        spam_sender.send_emails(
            'caroldanelli@gmail.com',
            'Python Pro Training Course',
            'Email body'
        )
        assert sender.sent_params == (
            'caroldanelli@gmail.com',
            'douglas.fraga@gmail.com'
            'Python Pro Training Course',
            'Email body'
        )
