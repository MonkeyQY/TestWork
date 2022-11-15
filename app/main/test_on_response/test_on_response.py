import asyncio

import aiohttp as aiohttp

from app.main.HttpMethods import Httpmethods


async def test_on_response(url: str):
    async with aiohttp.ClientSession() as session:
        dict_result = {}
        methods = [Httpmethods.MethodGet, Httpmethods.MethodOptions, Httpmethods.MethodPatch, Httpmethods.MethodPost,
                   Httpmethods.MethodPut, Httpmethods.MethodsHead]
        dict_interim = {}
        tasks = [asyncio.create_task(test(method, session, url)) for method in methods]
        lst = await asyncio.gather(*tasks)
        [dict_interim.update(dct) for dct in lst if dct is not None]
        dict_result.update({url: dict_interim})
        return dict_result


async def test(http_methods, session: aiohttp.ClientSession, url: str):
    return await http_methods.test_url(self=http_methods, session=session, url=url)