from aiohttp import ClientSession


async def check_url(method: str, url: str, session: ClientSession):
    response = await session.request(method=method, url=url)
    return requirement(response, method)


def requirement(response, method: str) -> dict:
    if response.status != 405:
        dict_method = {method: response.status}
        return dict_method
