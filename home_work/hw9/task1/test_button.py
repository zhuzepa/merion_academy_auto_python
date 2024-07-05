from home_work.hw9.task1.page import Page


def test_rename_button(browser):
    main = Page(browser)
    main.open()
    main.send_text_button('AQA')
    main.click_button()
    assert main.text_button() == 'AQA'
