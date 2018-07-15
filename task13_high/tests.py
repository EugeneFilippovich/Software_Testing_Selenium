


def test_app(app):
    app.main_page_load()
    app.item_select()
    app.item_to_cart()
    app.main_page_load()
    app.item_select()
    app.item_to_cart()
    app.main_page_load()
    app.item_select()
    app.item_to_cart()
    app.checkout_items()
    app.clear_cart()
