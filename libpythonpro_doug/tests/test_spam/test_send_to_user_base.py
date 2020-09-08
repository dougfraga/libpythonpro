from unittest.mock import Mock

import pytest

from libpythonpro_doug.spam.email_sender import Sender
from libpythonpro_doug.spam.main import SpamSender
from libpythonpro_doug.spam.models import User


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
    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_emails(
        'douglas.fraga@gmail.com',
        'Python Pro Training Course',
        'Email body'
    )
    assert len(users) == sender.send.call_count


def test_spam_params(session):
    user = User(name='Doug', email='douglas.fraga@gmail.com')
    session.save(user)
    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_emails(
        'caroldanelli@gmail.com',
        'Python Pro Training Course',
        'Email body'
    )
    sender.send.assert_called_once_with(
        'caroldanelli@gmail.com',
        'douglas.fraga@gmail.com',
        'Python Pro Training Course',
        'Email body'
    )
