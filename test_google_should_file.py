from selene.support.shared import browser
from selene import be, have


def test_successful(open_browser, size_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_not_successful(open_browser, size_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('dgdfdgdhdfgfg').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу  ничего не найдено.'))
