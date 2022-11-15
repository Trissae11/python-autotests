from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

link = 'https://ya.ru/'
login = 'qwa5.123'
password = '123456Aav'


@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


class Test:

    def test_open_enter_page(self, browser):
        browser.get(link)
        auth_button = browser.find_element(By.CLASS_NAME,
                                           'home-link2.headline__personal-enter.home-link2_color_black').click()

    def test_enter_login(self, browser):
        login_field = browser.find_element(By.ID, 'passp-field-login')
        login_field.send_keys(login)
        auth_button2 = browser.find_element(By.ID, 'passp:sign-in').click()

    def test_enter_password(self, browser):
        password_field = browser.find_element(By.ID, 'passp-field-passwd')
        password_field.send_keys(password)
        auth_button2 = browser.find_element(By.ID, 'passp:sign-in').click()

    def test_open_disk(self, browser):
        browser.find_element(By.CLASS_NAME, 'avatar__image-wrapper').click()
        browser.find_element(By.CLASS_NAME, 'usermenu-redesign__icon.usermenu-redesign__icon_disk').click()
        latest_window = browser.window_handles[1]
        browser.close()
        browser.switch_to.window(latest_window)

    def test_create_new_folder(self, browser):
        create_button = browser.find_element(By.CSS_SELECTOR, '.create-resource-popup-with-anchor').click()
        create_folder = browser.find_element(By.CSS_SELECTOR, '.file-icon_dir_plus').click()
        name_field = browser.find_element(By.XPATH, '//form[@class="rename-dialog__rename-form"] // input')
        name_field.click()
        name_field.send_keys(Keys.CONTROL + "a")
        name_field.send_keys(Keys.BACKSPACE)
        name_field.send_keys('new_folder')
        confirmation_button = browser.find_element(By.CLASS_NAME,
                                                   'Button2.Button2_view_action.Button2_size_m.confirmation-dialog__button.confirmation-dialog__button_submit')
        confirmation_button.click()


    def test_copy_file(self, browser):
        browser.find_element(By.CLASS_NAME, 'listing-item.listing-item_theme_tile.listing-item_size_m.listing-item_type_file.listing-item_selected.js-prevent-deselect').click()
        browser.find_element(By.CLASS_NAME,
                             'Button2.Button2_view_clear-inverse.Button2_size_m.groupable-buttons__more-button')
        browser.find_element(By.ID, 'item-16662837811712664-4')
        confirmation_button = browser.find_element(By.CLASS_NAME,
                                                   'Button2.Button2_view_action.Button2_size_m.confirmation-dialog__button.confirmation-dialog__button_submit')
        confirmation_button.click()
