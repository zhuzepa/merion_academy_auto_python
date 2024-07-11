import requests

URL = "https://todo-app-sky.herokuapp.com/"


def get_tasks():
    r = requests.get(URL)
    assert r.status_code == 200
    return r.json()


assert get_tasks()[1]['title'] == 'Построить дом - обновление'


# print(r.json()[1][
#           'title'])  # возвращает json, в котором есть список и можно обратится по индексу, а далее по ключу к значению

def get_task_by_id(id: int) -> dict: # В Python аннотация типа -> dict после параметра функции или возвращаемого значения указывает на ожидаемый тип данных. Чтобы работать с методами как в print .get, без него он не видит.
    r = requests.get(URL + str(id))
    assert r.status_code == 200
    return r.json()


print(get_task_by_id(1071).get('title'))


def created_title(title: str) -> dict:
    body = {"title": title, "completed": False}
    r = requests.post(URL, json=body)
    assert r.status_code == 200
    return r.json()


def title_complited(id: int) -> dict:
    body = {"completed": True}
    r = requests.patch(URL + str(id), json=body)
    assert r.status_code == 200
    return r.json()


def rename_title(id: int, rename: str) -> dict:
    body = {"title": rename}
    r = requests.patch(URL + str(id), json=body)
    assert r.status_code == 200
    return r.json()


def delete_title(id: int) -> None:
    r = requests.delete(URL + str(id))
    assert r.status_code == 200


ct = created_title("Работает братья")["id"]
rename_title(ct, "не работаем")
result = title_complited(ct)
result_delete = delete_title(ct)
