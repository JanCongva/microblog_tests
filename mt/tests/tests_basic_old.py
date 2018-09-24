from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.yield_fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.close()


@pytest.fixture
def log_in(browser, application):
    browser.get(application.address)
    elem = browser.find_element_by_id('username')
    elem.send_keys(application.username)
    elem = browser.find_element_by_id('password')
    elem.send_keys(application.password)
    elem = browser.find_element_by_id('submit')
    elem.click()


def test_login(browser, application):
    log_in(browser, application)
    assert browser.find_elements_by_xpath("//nav//a[.='Logout']"), "Login wasn't successful - logout button not found"


def test_edit_profile(browser, application, log_in, request):

    def set_username(new_username):
        elem = browser.find_element_by_xpath("//nav//a[.='Profile']")
        elem.click()
        elem = browser.find_element_by_xpath("//div//table//p/a[.='Edit your profile']")
        elem.click()
        elem = browser.find_element_by_id('username')
        elem.clear()
        elem.send_keys(new_username)
        elem = browser.find_element_by_id('submit')
        elem.click()

    @request.addfinalizer
    def _revert():
        set_username(application.username)

    set_username('misharov2')
    elem = browser.find_element_by_xpath("//nav//a[.='Profile']")
    elem.click()
    assert browser.find_elements_by_xpath("//div//table//h1[contains(., 'misharov2')]"),\
        "Username change wasn't successful - user profile page title doesn't contain new username"
