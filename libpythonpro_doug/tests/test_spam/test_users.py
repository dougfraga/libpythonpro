from libpythonpro_doug.spam.models import User


def test_save_user(session):
    user = User(name='Doug', email='douglas.fraga@gmail.com')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_user(session):
    users = [
        User(name='Doug', email='douglas.fraga@gmail.com'),
        User(name='Carol', email='caroldanelli@gmail.com')
    ]
    for user in users:
        session.save(user)
    assert users == session.list()
