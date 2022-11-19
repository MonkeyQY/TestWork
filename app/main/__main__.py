import asyncio

from app.main.check_list_strings import check_list_strings

lst = ['https://www.google.com/', 'https://ya.ru/', 'caga', 1213, 'hello']


async def main(incoming_list: list):
    """Функция на вход принимает список строк. Проверяет строки, являются ли они ссылками.
    Если ссылкой не является, то вывод сообщение. Если является ссылкой, то проверяет все
    доступные http методы и возвращает словарь в виде:
    {'https://www.google.com/': {'get': 200, 'head': 200}}"""
    return await check_list_strings(incoming_list)


print(asyncio.run(main(lst)))