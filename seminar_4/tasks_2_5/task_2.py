import multiprocessing

import requests
from multiprocessing import Process
import time

# Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте процессы.

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


def download(url):
    response = requests.get(url)
    filename = (
        "files/multiprocessing_"
        + url.replace("https://", "").replace(".", "_").replace("/", "")
        + ".html"
    )
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f}seconds")


processes = []
start_time = time.time()

if __name__ == "__main__":
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
for process in processes:
    process.join()
