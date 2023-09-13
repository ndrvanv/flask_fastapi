import os

import requests
import threading
import time

# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте потоки

count = 0
PATH = "files"


def get_amount_word(filename: str):
    global count
    with open(filename, encoding="utf-8") as f:
        count += len(f.read().split())


if __name__ == "__main__":
    threads = []
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            thread = threading.Thread(target=get_amount_word, args=(file_path,))
            threads.append(thread)
            thread.start()
            print(f"Промежуточное колчиство слов: {count}")

    for thread in threads:
        thread.join()
    time.sleep(1)
    print(f"Финальное значение слов: {count}")
