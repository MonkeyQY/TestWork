import asyncio

from app.main.__main__ import main

lst = ['https://www.google.com/', 'https://ya.ru/', 'caga', 1213, 'hello']


def test_get_list_string():
    result = asyncio.run(main(lst))
    assert type(result) == dict