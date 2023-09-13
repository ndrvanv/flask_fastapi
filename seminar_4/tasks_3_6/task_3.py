import asyncio
import aiohttp
import time

# Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте асинхронный подход.

urls = [
    "https://www.google.ru/",
    "https://gb.ru/",
    "https://ya.ru/",
    "https://www.python.org/",
    "https://habr.com/ru/all/",
    "https://hh.ru/",
    "https://youtube.com",
    "https://gb.ru",
    "https://avito.ru",
    "https://tesla.com",
]


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()


async def download(url):
    # для iOS
    # async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = (
                "asyncio_"
                + url.replace("https://", "").replace(".", "_").replace("/", "")
                + ".html"
            )
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
