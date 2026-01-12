# src/primitive_db/decorators.py
import time


# Декоратор для поимки исключений
def handle_db_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print("Ошибка: Файл данных не найден. Возможно, база данных не инициализирована.") # noqa: E501
        except KeyError as error:
            print(f"Ошибка: Таблица или столбец {error} не найден.")
        except ValueError as error:
            print(f"Ошибка валидации: {error}")
        except Exception as error:
            print(f"Произошла непредвиденная ошибка: {error}")
    return wrapper


# Декоратор для подтверждения действия пользователя
def confirm_action(action_name: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            answer = input(f'Вы уверены, что хотите выполнить "{action_name}"? [y/n]: ')
            if answer.strip().lower() in ('y', 'yes', 'д', 'да'):
                return func(*args, **kwargs)
            print('Операция отменена.')
            return '-1'
        return wrapper
    return decorator
    
    
# Декоратор для подсчета времени выполнения функции
def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.monotonic()
        result = func(*args, **kwargs)
        end_time = time.monotonic()
        elapsed = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {elapsed:.6f} секунд.")
        return result
    return wrapper
