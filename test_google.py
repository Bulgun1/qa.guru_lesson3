from selene import browser, be, have
def test_google_t():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('Pug').press_enter()
    browser.element('[id="search"]').should(have.text('Pug'))

def test_google_f():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('kdjvcnskiv nskiwuvnsdiuv8evjediv').press_enter()
    browser.element('//p[contains(text(), "По запросу")]').should(have.text('ничего не найдено.'))