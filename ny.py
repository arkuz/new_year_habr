from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from time import sleep


browser.config.hold_browser_open = False
browser.config.timeout = 5000
browser.config.browser_name = 'chrome'
browser.open('https://ny.habr.com/')
browser.driver.maximize_window()


def click():
    btn = "//button[contains(text(),'Ближе')]"
    inc = 0
    while True:
        if inc == 10:
            sleep(1)
            inc = 0
        s(btn).click()
        inc += 1


if __name__ == '__main__':
    click()
