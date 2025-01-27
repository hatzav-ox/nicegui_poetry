from selenium.webdriver.common.by import By

from nicegui import ui

from .screen import Screen


def test_apply_format_on_blur(screen: Screen):
    ui.number('Number', format='%.4f', value=3.14159)
    ui.button('Button')

    screen.open('/')
    screen.should_contain_input('3.1416')

    element = screen.selenium.find_element(By.XPATH, '//*[@aria-label="Number"]')
    element.send_keys('789')
    screen.click('Button')
    screen.should_contain_input('3.1417')
