import asyncio

from app.main.get_string.get_string import get_list_string


async def main(lst):
    return await get_list_string(lst)

asyncio.run(main(['']))