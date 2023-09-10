import requests
import threading
import time
from pathlib import Path
import argparse
import multiprocessing
import asyncio
import os
# Написать программу, которая скачивает изображения с заданных URL-адресов и
# сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
# файле, название которого соответствует названию изображения в URL-адресе.
# � Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
# image1.jpg
# � Программа должна использовать многопоточный, многопроцессорный и
# асинхронный подходы.
# � Программа должна иметь возможность задавать список URL-адресов через
# аргументы командной строки.
# � Программа должна выводить в консоль информацию о времени скачивания
# каждого изображения и общем времени выполнения программы.

# urls = ['https://gb.ru/',
# 'https://www.python.org/',
# 'https://habr.com/ru/all/',
# 'https://hh.ru/',
# 'https://youtube.com',
# 'https://gb.ru',
# 'https://avito.ru',
# 'https://tesla.com'
# ]


image_urls = []
with open('images_youtube_com.html', 'r') as images:
    for image in images.readline():
        image_urls.append(image.strip())

image_path = Path('./images')

def download_images(url):
    global image_path
    start_time = time.time()
    response = requests.get(url, stream=True)
    filename = image_path.joinpath(os.path.basename(url))
    with open(filename, 'ut') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    end_time = time.time() - start_time
    print(f'Download {filename} in {end_time:.2f} seconds')

async def download_image_async(url):
    start_time = time.time()
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url, {'stream':True})
    filename = image_path.joinpath(os.path.basename(url))
    with open(filename, 'ut') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    end_time = time.time() - start_time
    print(f'Download {filename} in {end_time:.2f} seconds')

def downloading_images_threading(url):
    start_time = time.time()
    threads = []
    for url in urls:
        t = threading.Thread(target=download_images(url), args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end_time = time.time() - start_time
    print(f'Total time using threading in {end_time:.2f} seconds')

def download_images_multiprocessing(urls):
    start_time = time.time()
    processes = []
    for url in urls:
        p = multiprocessing.Process(target=download_images(), args=(url,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end_time = time.time() - start_time
    print(f"Total time using multiprocessing: {end_time:.2f} seconds")

async def download_images_async(urls):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_image_async(url))
        tasks.append(task)


    await asyncio.gather(*tasks)

    end_time = time.time() - start_time
    print(f"Total time using asyncio: {end_time:.2f} seconds")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Save images to the disk')
    parser.add_argument("--urls", nargs="+", help="A list of URLs to download images from.")
    args = parser.parse_args()

    urls = args.urls
    if not urls:
        urls = image_urls

    print(f"Downloading {len(urls)} images using threading...")
    downloading_images_threading(urls)

    print(f"\nDownloading {len(urls)} images using multiprocessing...")
    download_images_multiprocessing(urls)

    print(f"\nDownloading {len(urls)} images using asyncio...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_images_async(urls))

