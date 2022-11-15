import asyncio
import urlextract

from app.main.string_handling.string_handling import string_handling


async def get_list_string(lst: list[str]) -> dict:
    extractor = urlextract.URLExtract()
    tasks = []
    for string in lst:
        if isinstance(string, str):
            task = asyncio.create_task(string_handling(string, extractor))
            tasks.append(task)
        else:
            print(f'{string} не Является строкой')
    list_result = await asyncio.gather(*tasks)
    json_result = transformation(list_result)
    return json_result


def transformation(lst) -> dict:
    dict_result = {}
    [dict_result.update(dct) for dct in lst if dct is not None]
    return dict_result
