from pytest import fixture
from . import browser_factory

@fixture()
def given_a_browser(browesr_name="chrome"):
    browser = browser_factory.get_browser(browesr_name)

    yield browser

    browser.close()