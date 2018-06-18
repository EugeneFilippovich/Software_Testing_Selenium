import pytest
from task13_high.app.application import Application


@pytest.fixture
def app(request):
    applic = Application()
    request.addfinalizer(applic.quit)
    return applic

# Работает
a = Application()
a.main_page_load()
a.item_select()
a.item_to_cart()
a.main_page_load()
a.item_select()
a.item_to_cart()
a.main_page_load()
a.item_select()
a.item_to_cart()
a.checkout_items()
a.clear_cart()

a.quit()

# Не работает
# def test_app(app):
#     app.main_page_load()
#     app.item_select()
#     app.item_to_cart()
#     app.main_page_load()
#     app.item_select()
#     app.item_to_cart()
#     app.main_page_load()
#     app.item_select()
#     app.item_to_cart()
#     app.checkout_items()
#     app.clear_cart()