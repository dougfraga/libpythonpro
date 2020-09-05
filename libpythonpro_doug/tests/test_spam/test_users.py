from libpythonpro_doug.spam.models import User


def test_save_user(session):
    user = User(name='Doug')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_user(session):
    users = [User(name='Doug'), User(name='Carol')]
    for user in users:
        session.save(user)
    assert users == session.list()
