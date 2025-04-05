import json
from datetime import datetime
import locale

# Налаштування локалізації
try:
    locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
except locale.Error:
    print("Не вдалося встановити локалізацію 'uk_UA.UTF-8'. Використовується стандартна локалізація.")

# Ім'я файлу для зберігання даних
DATABASE_FILE = 'files\\salary_data.json'

# Список допустимих місяців
MONTHS = [
    "Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
    "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"
]


# Ініціалізація бази даних
def load_data():
    """Завантажує дані з JSON-файлу або створює порожню базу, якщо файлу немає."""
    try:
        with open(DATABASE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {DATABASE_FILE} не знайдено. Створюється нова база даних.")
        return []
    except json.JSONDecodeError:
        print(f"Помилка: Файл {DATABASE_FILE} пошкоджений. Створюється нова база даних.")
        return []
    except Exception as e:
        print(f"Помилка при завантаженні даних: {e}")
        return []


# Збереження даних у JSON-файл
def save_data(data):
    """Зберігає дані у JSON-файл."""
    try:
        with open(DATABASE_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Помилка при збереженні даних: {e}")


# Ініціалізація бази даних
data = load_data()


def calculate_salary(hours, consultation_cost, coefficient):
    """Розраховує зарплату за формулою (у гривнях)."""
    return coefficient * consultation_cost * 2 * hours


def convert_currency(amount, usd_rate, eur_rate):
    """Переводить суму з гривень у долари та євро за курсами для конкретного місяця."""
    usd = amount / usd_rate
    eur = amount / eur_rate
    return usd, eur


def format_salary(amount, usd_rate, eur_rate):
    """Форматує зарплату у гривнях, доларах і євро."""
    usd, eur = convert_currency(amount, usd_rate, eur_rate)
    return f"{locale.format_string('%.2f', amount, grouping=True)} гривень ({locale.format_string('%.2f', usd, grouping=True)} долар / {locale.format_string('%.2f', eur, grouping=True)} євро)"


def validate_month_format(month):
    """Перевіряє, чи відповідає введений місяць формату 'Місяць Рік'."""
    parts = month.strip().split()
    if len(parts) != 2:
        return False, "Місяць має бути у форматі 'Місяць Рік' (наприклад, 'Січень 2024')!"

    month_name, year = parts
    # Перетворюємо введений місяць у правильний регістр
    month_name = month_name.capitalize()
    if month_name not in MONTHS:
        return False, f"Місяць має бути одним із: {', '.join(MONTHS)}!"

    try:
        year = int(year)
        if year < 1900 or year > 2100:
            return False, "Рік має бути між 1900 і 2100!"
    except ValueError:
        return False, "Рік має бути числом (наприклад, 2024)!"

    return True, month_name + " " + str(year)


def check_month_unique(month, exclude_id=None):
    """Перевіряє, чи місяць уже існує у базі, виключаючи запис із exclude_id."""
    for entry in data:
        if entry['id'] != exclude_id and entry['month'].lower() == month.lower():
            return False
    return True


def get_default_rates():
    """Повертає курси валют за замовчуванням (з останнього запису або стандартні)."""
    if data:
        last_entry = data[-1]
        return last_entry['usd_rate'], last_entry['eur_rate']
    return 41.34, 45.62  # Стандартні значення


def month_to_tuple(month_str):
    """Перетворює місяць у формат (рік, номер місяця) для хронологічного сортування."""
    month_name, year = month_str.split()
    month_num = MONTHS.index(month_name) + 1
    return (int(year), month_num)


def add_salary_data():
    """Додає новий запис про зарплату за місяць."""
    month = input("Введіть місяць (наприклад, 'Січень 2024'): ").strip()
    if not month:
        print("Місяць не може бути порожнім!")
        return

    # Перевірка формату місяця
    is_valid, result = validate_month_format(month)
    if not is_valid:
        print(result)
        return
    month = result

    # Перевірка унікальності місяця
    if not check_month_unique(month):
        print(f"Дані за {month} уже існують! Використовуйте редагування для зміни.")
        return

    try:
        hours = float(input("Введіть робочі години в місяць: "))
        if hours < 0:
            print("Робочі години не можуть бути від'ємними!")
            return

        consultation_cost = float(input("Введіть вартість консультації: "))
        if consultation_cost < 0:
            print("Вартість консультації не може бути від'ємною!")
            return

        coefficient = float(input("Введіть коефіцієнт працівника: "))
        if coefficient < 0:
            print("Коефіцієнт не може бути від'ємним!")
            return

        default_usd, default_eur = get_default_rates()
        usd_rate = float(
            input(f"Введіть курс долара (гривень за 1 USD, за замовчуванням {default_usd}): ") or default_usd)
        if usd_rate <= 0:
            print("Курс долара не може бути від'ємним або нульовим!")
            return
        if usd_rate < 10 or usd_rate > 100:
            print("Курс долара має бути в межах 10–100 гривень!")
            return

        eur_rate = float(
            input(f"Введіть курс євро (гривень за 1 EUR, за замовчуванням {default_eur}): ") or default_eur)
        if eur_rate <= 0:
            print("Курс євро не може бути від'ємним або нульовим!")
            return
        if eur_rate < 10 or eur_rate > 100:
            print("Курс євро має бути в межах 10–100 гривень!")
            return
    except ValueError:
        print("Будь ласка, введіть коректні числові значення!")
        return

    # Розраховуємо зарплату
    salary = calculate_salary(hours, consultation_cost, coefficient)

    # Додаємо новий запис
    entry_id = len(data) + 1
    new_entry = {
        'id': entry_id,
        'month': month,
        'hours': hours,
        'consultation_cost': consultation_cost,
        'coefficient': coefficient,
        'salary': salary,
        'usd_rate': usd_rate,
        'eur_rate': eur_rate,
        'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'history': []
    }

    data.append(new_entry)
    save_data(data)
    print(f'Запис #{entry_id} за {month} успішно додано! Зарплата: {format_salary(salary, usd_rate, eur_rate)}')


def delete_salary_data():
    """Видаляє запис про зарплату за номером."""
    if not data:
        print("Дані відсутні.")
        return

    try:
        entry_id = int(input("Введіть номер запису для видалення: "))
        entry_to_delete = None
        for entry in data:
            if entry['id'] == entry_id:
                entry_to_delete = entry
                break

        if entry_to_delete:
            data.remove(entry_to_delete)
            for index, entry in enumerate(data, start=1):
                entry['id'] = index
            save_data(data)
            print(f'Запис #{entry_id} за {entry_to_delete['month']} видалено!')
        else:
            print("Запис із таким номером не знайдено!")
    except ValueError:
        print("Будь ласка, введіть коректний номер!")


def edit_salary_data():
    """Редагує всі параметри (місяць, години, вартість, коефіцієнт, курси валют) для конкретного запису."""
    if not data:
        print("Дані відсутні.")
        return

    try:
        entry_id = int(input("Введіть номер запису для редагування: "))
        entry_to_edit = None
        for entry in data:
            if entry['id'] == entry_id:
                entry_to_edit = entry
                break

        if not entry_to_edit:
            print("Запис із таким номером не знайдено!")
            return

        print(f"\nПоточні дані за {entry_to_edit['month']}:")
        print(f"Місяць: {entry_to_edit['month']}")
        print(f"Робочі години: {entry_to_edit['hours']}")
        print(f"Вартість консультації: {entry_to_edit['consultation_cost']}")
        print(f"Коефіцієнт: {entry_to_edit['coefficient']}")
        print(f"Курс долара: {entry_to_edit['usd_rate']} UAH")
        print(f"Курс євро: {entry_to_edit['eur_rate']} UAH")
        print(
            f"Зарплата: {format_salary(entry_to_edit['salary'], entry_to_edit['usd_rate'], entry_to_edit['eur_rate'])}")

        new_month = input("Введіть новий місяць (або Enter, щоб залишити без змін): ").strip() or entry_to_edit['month']
        if new_month != entry_to_edit['month']:
            is_valid, result = validate_month_format(new_month)
            if not is_valid:
                print(result)
                return
            new_month = result
            if not check_month_unique(new_month, exclude_id=entry_id):
                print(f"Дані за {new_month} уже існують! Виберіть інший місяць.")
                return

        try:
            hours_input = input("Введіть нові робочі години (або Enter, щоб залишити без змін): ").strip()
            hours = float(hours_input) if hours_input else entry_to_edit['hours']
            if hours < 0:
                print("Робочі години не можуть бути від'ємними!")
                return

            consultation_cost_input = input(
                "Введіть нову вартість консультації (або Enter, щоб залишити без змін): ").strip()
            consultation_cost = float(consultation_cost_input) if consultation_cost_input else entry_to_edit[
                'consultation_cost']
            if consultation_cost < 0:
                print("Вартість консультації не може бути від'ємною!")
                return

            coefficient_input = input("Введіть новий коефіцієнт (або Enter, щоб залишити без змін): ").strip()
            coefficient = float(coefficient_input) if coefficient_input else entry_to_edit['coefficient']
            if coefficient < 0:
                print("Коефіцієнт не може бути від'ємним!")
                return

            usd_rate_input = input("Введіть новий курс долара (або Enter, щоб залишити без змін): ").strip()
            usd_rate = float(usd_rate_input) if usd_rate_input else entry_to_edit['usd_rate']
            if usd_rate <= 0:
                print("Курс долара не може бути від'ємним або нульовим!")
                return
            if usd_rate < 10 or usd_rate > 100:
                print("Курс долара має бути в межах 10–100 гривень!")
                return

            eur_rate_input = input("Введіть новий курс євро (або Enter, щоб залишити без змін): ").strip()
            eur_rate = float(eur_rate_input) if eur_rate_input else entry_to_edit['eur_rate']
            if eur_rate <= 0:
                print("Курс євро не може бути від'ємним або нульовим!")
                return
            if eur_rate < 10 or eur_rate > 100:
                print("Курс євро має бути в межах 10–100 гривень!")
                return
        except ValueError:
            print("Будь ласка, введіть коректні числові значення!")
            return

        # Логування змін
        change_log = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'changes': {
                'month': new_month if new_month != entry_to_edit['month'] else None,
                'hours': hours if hours != entry_to_edit['hours'] else None,
                'consultation_cost': consultation_cost if consultation_cost != entry_to_edit[
                    'consultation_cost'] else None,
                'coefficient': coefficient if coefficient != entry_to_edit['coefficient'] else None,
                'usd_rate': usd_rate if usd_rate != entry_to_edit['usd_rate'] else None,
                'eur_rate': eur_rate if eur_rate != entry_to_edit['eur_rate'] else None
            }
        }
        entry_to_edit['history'].append(change_log)

        # Оновлюємо параметри та перераховуємо зарплату
        entry_to_edit['month'] = new_month
        entry_to_edit['hours'] = hours
        entry_to_edit['consultation_cost'] = consultation_cost
        entry_to_edit['coefficient'] = coefficient
        entry_to_edit['usd_rate'] = usd_rate
        entry_to_edit['eur_rate'] = eur_rate
        entry_to_edit['salary'] = calculate_salary(hours, consultation_cost, coefficient)
        save_data(data)
        print(
            f"Дані для {entry_to_edit['month']} оновлено! Нова зарплата: {format_salary(entry_to_edit['salary'], usd_rate, eur_rate)}")
    except ValueError:
        print("Будь ласка, введіть коректний номер!")


def print_salary_by_month():
    """Виводить зарплату за конкретний місяць."""
    if not data:
        print("Дані відсутні.")
        return

    month = input("Введіть місяць для пошуку (наприклад, 'Січень 2024'): ").strip()
    is_valid, result = validate_month_format(month)
    if not is_valid:
        print(result)
        return
    month = result

    found = False
    for entry in data:
        if entry['month'].lower() == month.lower():
            print(f"\nЗапис за {entry['month']}:")
            print(f"Зарплата: {format_salary(entry['salary'], entry['usd_rate'], entry['eur_rate'])}")
            # print(f"Робочі години: {entry['hours']}")
            # print(f"Вартість консультації: {entry['consultation_cost']}")
            # print(f"Коефіцієнт: {entry['coefficient']}")
            print(f"Курс долара: {entry['usd_rate']} UAH")
            print(f"Курс євро: {entry['eur_rate']} UAH")
            print("-" * 40)
            found = True
            break

    if not found:
        print(f"Дані за {month} не знайдено!")


def calculate_total_salary_by_year(year):
    """Обчислює загальну зарплату за рік і повертає записи."""
    total_salary = 0
    entries = []
    for entry in data:
        entry_year = entry['month'].split()[-1]
        if entry_year == year:
            total_salary += entry['salary']
            entries.append(entry)
    return total_salary, entries


def print_salary_by_year():
    """Виводить загальну зарплату за рік."""
    if not data:
        print("Дані відсутні.")
        return

    year = input("Введіть рік для пошуку (наприклад, '2024'): ").strip()
    total_salary, entries = calculate_total_salary_by_year(year)

    if not entries:
        print(f"Дані за {year} рік не знайдено!")
        return

    avg_usd_rate = sum(entry['usd_rate'] for entry in entries) / len(entries)
    avg_eur_rate = sum(entry['eur_rate'] for entry in entries) / len(entries)
    print(f"\nЗагальна зарплата за {year} рік: {format_salary(total_salary, avg_usd_rate, avg_eur_rate)}")


def print_average_salary_by_year():
    """Виводить середню зарплату за місяць за рік."""
    if not data:
        print("Дані відсутні.")
        return

    year = input("Введіть рік для пошуку (наприклад, '2024'): ").strip()
    total_salary, entries = calculate_total_salary_by_year(year)

    if not entries:
        print(f"Дані за {year} рік не знайдено!")
        return

    average_salary = total_salary / len(entries)
    avg_usd_rate = sum(entry['usd_rate'] for entry in entries) / len(entries)
    avg_eur_rate = sum(entry['eur_rate'] for entry in entries) / len(entries)
    print(f"\nСередня зарплата за місяць у {year} році: {format_salary(average_salary, avg_usd_rate, avg_eur_rate)}")


def print_all_salary_data(sort_by='month', year_filter=None):
    """Виводить усі записи про зарплату з можливістю сортування та фільтрації за роком."""
    if not data:
        print("Дані відсутні.")
        return

    filtered_data = data
    if year_filter:
        filtered_data = [entry for entry in data if entry['month'].split()[-1] == year_filter]
        if not filtered_data:
            print(f"Дані за {year_filter} рік не знайдено!")
            return

    if sort_by == 'month':
        sorted_data = sorted(filtered_data, key=lambda x: month_to_tuple(x['month']))
    elif sort_by == 'salary':
        sorted_data = sorted(filtered_data, key=lambda x: x['salary'], reverse=True)
    else:
        sorted_data = filtered_data

    print("\nУсі записи про зарплату:")
    for entry in sorted_data:
        print(f"\nЗапис #{entry['id']}")
        print(f"Місяць: {entry['month']}")
        # print(f"Робочі години: {entry['hours']}")
        # print(f"Вартість консультації: {entry['consultation_cost']}")
        # print(f"Коефіцієнт: {entry['coefficient']}")
        print(f"Курс долара: {entry['usd_rate']} UAH")
        print(f"Курс євро: {entry['eur_rate']} UAH")
        print(f"Зарплата: {format_salary(entry['salary'], entry['usd_rate'], entry['eur_rate'])}")
        print(f"Дата додавання: {entry['date_added']}")
        print("-" * 40)


def main():
    """Головна функція для управління даними про зарплату."""
    while True:
        print('\n' + '=' * 30)
        print('\nМеню:')
        print('1. Додати дані про зарплату')
        print('2. Видалити запис')
        print('3. Редагувати дані (місяць, години, вартість, коефіцієнт, курси валют)')
        print('4. Показати всі записи (сортувати за місяцем)')
        print('5. Показати всі записи (сортувати за зарплатою)')
        print('6. Показати зарплату за місяцем')
        print('7. Показати загальну зарплату за рік')
        print('8. Показати середню зарплату за місяць за рік')
        print('9. Фільтрувати записи за роком (сортувати за місяцем)')
        print('10. Фільтрувати записи за роком (сортувати за зарплатою)')
        print('11. Вийти')
        print('\n' + '=' * 30)
        choice = input('Виберіть опцію: ')
        print('*!' * 15)

        if choice == '1':
            add_salary_data()
        elif choice == '2':
            delete_salary_data()
        elif choice == '3':
            edit_salary_data()
        elif choice == '4':
            print_all_salary_data(sort_by='month')
        elif choice == '5':
            print_all_salary_data(sort_by='salary')
        elif choice == '6':
            print_salary_by_month()
        elif choice == '7':
            print_salary_by_year()
        elif choice == '8':
            print_average_salary_by_year()
        elif choice == '9':
            year = input("Введіть рік для фільтрації (наприклад, '2024'): ").strip()
            print_all_salary_data(sort_by='month', year_filter=year)
        elif choice == '10':
            year = input("Введіть рік для фільтрації (наприклад, '2024'): ").strip()
            print_all_salary_data(sort_by='salary', year_filter=year)
        elif choice == '11':
            print('Дякую за використання програми! До побачення!')
            break
        else:
            print('Невірний вибір. Спробуйте ще раз.')


if __name__ == "__main__":
    main()