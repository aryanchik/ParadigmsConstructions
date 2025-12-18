import json
import sys
import os
import random
import time
from contextlib import contextmanager


def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)
        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)
        return result
    return wrapper


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"time: {elapsed_time:.1f}")




if len(sys.argv) > 1:
    path = sys.argv[1]
    print(f"используем файл из аргументов: {path}")
else:

    possible_paths = [
        'data_light.json',
        './data_light.json',
        '../data_light.json',
        '../../data_light.json',
        'lab2/data_light.json',
        '../lab2/data_light.json',
    ]

    path = None
    for possible_path in possible_paths:
        if os.path.exists(possible_path):
            path = possible_path
            print(f"Найден файл: {path}")
            break

    if path is None:
        print("Файл data_light.json не найден. Создаем тестовые данные...")
        test_data = [
            {"job-name": "Программист Python"},
            {"job-name": "Программист Java"},
            {"job-name": "Аналитик данных"},
            {"job-name": "Программист C++"},
            {"job-name": "Менеджер проекта"},
            {"job-name": "программист JavaScript"},
            {"job-name": "Дизайнер интерфейсов"}
        ]
        path = 'test_data.json'
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False, indent=2)
        print(f"Создан тестовый файл: {path}")

print(f"Используемый путь: {path}")

if not os.path.exists(path):
    print(f"ОШИБКА: Файл {path} не существует!")
    print("Попробуйте указать полный путь к файлу:")
    print("python process_data.py /полный/путь/к/data_light.json")
    sys.exit(1)


if not os.access(path, os.R_OK):
    print(f"ОШИБКА: Нет прав на чтение файла {path}!")
    sys.exit(1)


try:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"Данные успешно загружены из: {path}")
    print(f"Загружено {len(data)} записей")
except Exception as e:
    print(f"Ошибка при загрузке файла {path}: {e}")
    sys.exit(1)


@print_result
def f1(arg):

    return sorted(set(job['job-name'].lower() for job in arg), key=str.lower)

@print_result
def f2(arg):

    return list(filter(lambda x: x.startswith('программист'), arg))

@print_result
def f3(arg):

    return list(map(lambda x: x + " с опытом Python", arg))

@print_result
def f4(arg):

    salaries = [random.randint(100000, 200000) for _ in arg]
    return [f"{prof}, зарплата {salary} руб." for prof, salary in zip(arg, salaries)]

if __name__ == '__main__':
    print("\n=== ЗАПУСК ОБРАБОТКИ ===")
    with cm_timer_1():
        f4(f3(f2(f1(data))))
