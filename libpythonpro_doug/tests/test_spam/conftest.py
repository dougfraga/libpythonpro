import pytest

from libpythonpro_doug.spam.db import Connection


@pytest.fixture(scope='session')
def connection():
    # Setup
    connection_obj = Connection()
    yield connection_obj
    # Tear Down
    connection_obj.close()


@pytest.fixture
def session(connection):
    session_obj = connection.generate_session()
    yield session_obj
    session_obj.roll_back()
    session_obj.close()
