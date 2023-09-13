import os
import asyncio

# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте асинхронный подход

counter = 0
PATH = "files"


async def get_amount_word(file_path):
    global counter
    with open(file_path, encoding="utf-8") as f:
        counter = len(f.read().split())
    print(f"Значение счетчика: {counter:_}")


async def main():
    tasks = []
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            tasks.append(asyncio.create_task(get_amount_word(file_path)))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
    print(f"Финальное значение слов: {counter}")
