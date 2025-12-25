

def calculate_sum(a, b):
    """Возвращает сумму двух чисел."""
    return a + b

def calculate_product(a, b):
    """Возвращает произведение двух чисел."""
    return a * b

def main():
    """Основная функция программы."""
    try:
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))

        sum_result = calculate_sum(a, b)
        prod_result = calculate_product(a, b)

        print(f"Сумма: {sum_result}")
        print(f"Произведение: {prod_result}")
    except ValueError:
        print("Ошибка: введите целые числа.")

if __name__ == "__main__":
    main()
