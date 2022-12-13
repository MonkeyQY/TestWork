import asyncio

from app.__main__ import main

lst1 = ['https://www.google.com/', 'https://ya.ru/', 'caga', 1213, 'hello']
lst = ['https://www.google.com/']
lst2 = [1213]


def test_check_list_string():
    result = asyncio.run(main(lst))
    assert result == {'https://www.google.com/': {'get': 200, 'head': 200}}
    result_1 = asyncio.run(main(lst1))
    assert type(result_1) == dict
    result_2 = asyncio.run(main(lst2))
    assert result_2 == {}
