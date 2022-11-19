import asyncio

import urlextract

from app.main.string_handling import string_handling

string = 'https://www.google.com/'
string1 = 'sfgsdfg'


def test_string_handing():
    extractor = urlextract.URLExtract()
    dict_for_string = asyncio.run(string_handling(string, extractor))
    assert dict_for_string == {'https://www.google.com/': {'get': 200, 'head': 200}}
    dict_for_string = asyncio.run(string_handling(string1, extractor))
    assert dict_for_string == print(f"Строка '{string1}' не является ссылкой")
