import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def size_browser():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()
