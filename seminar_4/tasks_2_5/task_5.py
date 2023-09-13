import os

import multiprocessing
import time

# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте процессы.

count = 0
PATH = "files"
counter = multiprocessing.Value("i", 0)


def get_amount_word(counter, filename):
    with open(filename, encoding="utf-8") as f:
        with counter.get_lock():
            counter.value += len(f.read().split())
    print(f"Значение счетчика: {counter.value:_}")


if __name__ == "__main__":
    processes = []
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            process = multiprocessing.Process(
                target=get_amount_word, args=(counter, file_path)
            )
            processes.append(process)
            process.start()

    for process in processes:
        process.join()
    time.sleep(1)
    print(f"Финальное значение слов: {counter.value}")
