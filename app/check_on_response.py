import asyncio

import aiohttp as aiohttp

from app.check_url import check_url


methods = [
    'get', 'put', 'patch',
    'post', 'delete', 'options',
    'head', 'connect', 'trace'
]


async def check_on_response(url: str):
    """Функция проверяет доступные методы для входящего url
    и возвращает словарь со всеми доступными методами для этого url"""
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(check_url(method, url, session)) for method in methods]
        response = await asyncio.gather(*tasks)

        dict_for_url = transformation_tuple_with_responses_in_dict(response, url)
        return dict_for_url


def transformation_tuple_with_responses_in_dict(response: tuple, url: str):
    """Функция принимает tuple со словарями и создаёт один общий словарь для конкретного url"""
    dict_for_url = {}
    dict_from_response_for_url = {}

    # обновляет словарь из ответов на все http запросы, которые прошли проверку
    [dict_from_response_for_url.update(i) for i in response if i is not None]

    # обновляет словарь ключом в качестве url и значением - доступные http методы для этого url
    dict_for_url.update({url: dict_from_response_for_url})
    return dict_for_url


