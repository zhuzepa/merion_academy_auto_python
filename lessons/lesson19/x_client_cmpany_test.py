import requests

URL = 'https://x-clients-be.onrender.com/company'


def test_get_company_list():
    # получение списка компании
    response = requests.get(URL)
    company_list = response.json()
    content_type = response.headers.get('content-type')

    assert len(company_list) > 0
    assert response.status_code == 200
    assert content_type != None
    assert content_type == 'application/json; charset=utf-8'
