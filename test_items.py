import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button_is_present(browser):
    browser.get(link)
    add_button = browser.find_element_by_class_name("btn-add-to-basket")
    # time.sleep(30)
    assert add_button.is_displayed(), "Button is not displayed"
    assert add_button.is_enabled(), "Button is disabled"
