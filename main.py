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