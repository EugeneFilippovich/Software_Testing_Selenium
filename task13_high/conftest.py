import pytest
from task13_high.app.application import Application


@pytest.fixture
def app(request):
    applic = Application()
    request.addfinalizer(applic.quit)
    return applic

