from urlextract import URLExtract

from app.main.test_on_response.test_on_response import test_on_response


async def string_handling(string: str, extractor: URLExtract):
    urls = extractor.find_urls(string)
    if len(urls) > 0:
        dict_result = {}
        for url in urls:
            dict_result.update(await test_on_response(url))
        return dict_result
    else:
        print(f"Строка '{string}' не является ссылкой")