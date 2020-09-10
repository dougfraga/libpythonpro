from unittest.mock import Mock

import pytest

from libpythonpro_doug import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars3.githubusercontent.com/u/61299254?v=4'
    resp_mock.json.return_value = {
        'login': 'dougfraga', 'id': 61299254,
        'avatar_url': url
    }
    get_mock = mocker.patch('libpythonpro_doug.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_search_avatar(avatar_url):
    url = github_api.search_avatar('dougfraga')
    assert avatar_url == url


def test_search_avatar_integration():
    url = github_api.search_avatar('dougfraga')
    assert 'https://avatars3.githubusercontent.com/u/61299254?v=4' == url
