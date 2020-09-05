from libpythonpro_doug.spam.email_sender import Sender
from libpythonpro_doug.spam.main import SpamSender


def test_send_spam(session):
    spam_sender = SpamSender(session, Sender())
    spam_sender.send_emails(
        'douglas.fraga@gmail.com',
        'Python Pro Training Course',
        'Email body'
    )
