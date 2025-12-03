import re
import requests
import os

def find_bankcards(text):
    pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    return re.findall(pattern, text)

def is_valid_bankcard(card_number):
    pattern = r'^(?:\d{4}[-\s]?){3}\d{4}$'
    return re.match(pattern, card_number) is not None

def validate_from_user_input():
    print("\n=== Проверка номера банковской карты ===")
    card = input("Введите номер карты: ").strip()
    if is_valid_bankcard(card):
        print(f"✅ Номер карты '{card}' корректен")
    else:
        print(f"❌ Номер карты '{card}' не соответствует формату")


def validate_from_url():
    print("\n=== Поиск номеров карт на веб-странице ===")
    url = input("Введите URL страницы: ").strip()
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        cards = find_bankcards(response.text)
        if cards:
            print(f"Найдено {len(cards)} номер(а/ов) карт:")
            for card in cards:
                print(f"  - {card}")
        else:
            print("Номеров карт не найдено")
    except Exception as e:
        print(f"Ошибка при загрузке страницы: {e}")


def validate_from_file():
    print("\n=== Поиск номеров карт в файле ===")
    file_path = input("Введите путь к файлу: ").strip()
    if not os.path.exists(file_path):
        print("Файл не найден!")
        return
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        cards = find_bankcards(content)
        if cards:
            print(f"Найдено {len(cards)} номер(а/ов) карт:")
            for card in cards:
                print(f"  - {card}")
        else:
            print("Номеров карт не найдено")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


def main():
    while True:
        print("\n" + "=" * 50)
        print("Лабораторная работа №2: Регулярные выражения")
        print("Проверка номеров банковских карт")
        print("=" * 50)
        print("1. Проверить номер карты (ручной ввод)")
        print("2. Найти номера карт на веб-странице (URL)")
        print("3. Найти номера карт в файле")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ").strip()

        if choice == '1':
            validate_from_user_input()
        elif choice == '2':
            validate_from_url()
        elif choice == '3':
            validate_from_file()
        elif choice == '4':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()