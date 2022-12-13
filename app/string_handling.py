from urlextract import URLExtract

from app.check_on_response import check_on_response


async def string_handling(string: str, extractor: URLExtract):
    """Принимает строку и проверяет её на наличие ссылки.
    Если строка не является ссылкой, то выводит сообщение в терминал.
    Иначе перебирает все ссылки в строке и вызывает функцию с запросами"""
    urls = extractor.find_urls(string)

    if len(urls) > 0:
        dict_for_string = {}
        for url in urls:
            dict_for_string.update(await check_on_response(url))
        return dict_for_string
    else:
        print(f"Строка '{string}' не является ссылкой")