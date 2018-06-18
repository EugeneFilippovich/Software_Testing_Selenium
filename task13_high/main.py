import pytest
from task13_high.app.application import Application


@pytest.fixture
def app(request):
    applic = Application()
    request.addfinalizer(applic.quit)
    return applic



app.main_page_load()
app.main_page.select_item()
app.item_page.add_item('Small').wait_cart_update()
app.main_page_load()
app.main_page.select_item()
app.item_page.add_item('Small').wait_cart_update()
app.main_page_load()
app.main_page.select_item()
app.item_page.add_item('Small').wait_cart_update().checkout()
app.cart_page.remove_items()