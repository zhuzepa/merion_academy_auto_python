import requests

URL = 'https://x-clients-be.onrender.com/company'

import allure


@allure.title("Получение списка компаний")  # название кейса
@allure.description("В этом тесте происходит получение данных компании. Авторизация не требуется")  # подробное описание
@allure.tag("NewAPI", "Essentials", "Company")  # теги
@allure.severity(allure.severity_level.NORMAL)  # серьезность
@allure.label("owner", "ALex Prince")
@allure.link("https://dev.example.com/", name="Website")  # можно указать ссылку на ТК
@allure.link("https://ya.ru/", name="YA")  # можно указать ссылку на требование
@allure.issue("AUTH-123")  # для дефекта, если тест падает, то типо мы знаем и оповещаем команду
@allure.testcase("TMS-456")  # TMS указываем
@allure.epic("Web interface")  # что за за
@allure.feature("Essential features")
@allure.story("Authentication")
def test_get_company_list():

    # получение списка компании
    response = requests.get(URL)
    company_list = response.json()
    content_type = response.headers.get('content-type')

    with allure.step(f'Проверяем, что {company_list} больше 0'):
        assert len(company_list) > 0
    with allure.step(f'Проверяем, что статус код == 200'):
        assert response.status_code == 200
    with allure.step('Проверяем, что content_type не пустой'):
        assert content_type != None
    with allure.step('Проверяем, что content_type == application/json; charset=utf-8'):
        assert content_type == 'application/json; charset=utf-8'
