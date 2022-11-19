import asyncio

import pytest

from app.main.check_on_response import transformation_tuple_with_responses_in_dict, check_on_response


def test_transformation_tuple_with_responses_in_dict():
    url = 'https://www.google.com/'
    response = ({'get': 200}, {'head': 200})
    dict_for_url = transformation_tuple_with_responses_in_dict(response, url)
    assert dict_for_url == {'https://www.google.com/': {'get': 200, 'head': 200}}


def test_check_on_response():
    url = 'https://www.google.com/'
    dict_for_url = asyncio.run(check_on_response(url))
    assert dict_for_url == {'https://www.google.com/': {'get': 200, 'head': 200}}
