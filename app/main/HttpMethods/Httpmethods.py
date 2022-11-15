from aiohttp import ClientSession

from app.main import HttpMethods

class MethodGet:

    @staticmethod
    def string():
        return 'get'

    async def test_url(self, session: ClientSession, url: str):
        response = await session.get(url=url)
        return requirement(response, self.string())


class MethodPost:

    @staticmethod
    def string():
        return 'post'

    async def test_url(self, session: ClientSession, url: str):
        response = await session.post(url=url)
        return requirement(response, self.string())


class MethodPut:

    @staticmethod
    def string():
        return 'put'

    async def test_url(self, session: ClientSession, url: str):
        response = await session.put(url=url)
        return requirement(response, self.string())


class MethodsHead:

    @staticmethod
    def string():
        return 'head'

    async def test_url(self, session: ClientSession, url: str):
        response = await session.head(url=url)
        return requirement(response, self.string())


class MethodPatch:

    @staticmethod
    def string():
        return 'patch'

    async def test_url(self, session: ClientSession, url: str):
        response = await session.patch(url=url)
        return requirement(response, self.string())


class MethodOptions:

    @staticmethod
    def string():
        return 'options'

    async def test_url(self, session: ClientSession, url: str):
        response = await session.options(url=url)
        return requirement(response, self.string())


def requirement(response, text) -> dict:
    if response.status != 405:
        dict_result = {text: response.status}
        return dict_result
