import json
from pathlib import Path

variant_number = 13

card = json.loads(Path(__file__).with_name("student_variants.json").read_text(encoding="utf-8"))["variants"][variant_number - 1]

# Отримуємо значення температури від користувача
raw = input(f"{card['inputs'][0]['name']}: ")
value = int(raw) if card["inputs"][0]["type"] == "int" else float(raw)

# 1. Перевірка на вихід за припустимий загальний діапазон [-50, 100]
if value < card["domain"]["min"] or value > card["domain"]["max"]:
    print("Помилка: значення поза допустимим діапазоном [-50, 100]")

# 2. Перевірка, чи потрапляє значення в цільове вікно [10, 35] включно
elif card["window"]["min"] <= value <= card["window"]["max"]:
    print("Значення входить у цільовий інтервал [10, 35]")

# 3. Якщо входить у загальний діапазон, але поза цільовим вікном
else:
    print("Значення знаходиться поза цільовим інтервалом")