import pytest

from libpythonpro_doug.spam.email_sender import Sender, InvalidEmail


def test_create_email_sender():
    email_sender = Sender()
    assert email_sender is not None


@pytest.mark.parametrize(
    'shipper',
    ['douglas.fraga@gmail.com', 'douglas@threetek.com.br']
)
def test_email_sender(shipper):
    email_sender = Sender()

    result = email_sender.send(
        shipper,
        'dfr_dede@yahoo.com.br',
        'Python Pro training course',
        'email body'
    )
    assert shipper in result


@pytest.mark.parametrize(
    'shipper',
    ['', 'douglas']
)
def test_invalid_email_sender(shipper):
    email_sender = Sender()
    with pytest.raises(InvalidEmail):
        email_sender.send(
            shipper,
            'dfr_dede@yahoo.com.br',
            'Python Pro training course',
            'email body'
        )
