from asyncio.subprocess import Process

import requests
import threading
import time
# Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте потоки.

urls = ['https://www.google.ru/',
'https://gb.ru/',
'https://ya.ru/',
'https://www.python.org/',
'https://habr.com/ru/all/',
'https://hh.ru/',
'https://youtube.com',
'https://gb.ru',
'https://avito.ru',
'https://tesla.com'
]

def download(url):
    response = requests.get(url)
    filename = 'files/threding_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f}seconds")

threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
