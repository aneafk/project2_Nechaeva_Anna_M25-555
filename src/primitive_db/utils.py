# src/primitive_db/utils.py
import json as js

import prompt as pr

from .constants import COMMANDS, TABLE_PATH
from .decorators import handle_db_errors


# Функция запроса ввода
@handle_db_errors
def user_input() -> str:
    '''
    Функиця запрашивает пользовательский ввод с клавиатуры
    '''
    user_command = pr.string('Введите команду: ')

    return user_command.strip()


# Функция загрузки мета данных
@handle_db_errors
def load_metadata(filepath: str) -> dict:
    '''
    filepath - путь до .json файла.
    Функция загружает текущие мета данные из файла
    '''
    with open(filepath, encoding='utf-8') as metadata_json:
        loaded_metadata = js.load(metadata_json)
    return loaded_metadata
    
    
# Функция сохранения метаданных таблицы
@handle_db_errors
def save_metadata(filepath: str, data: dict) -> None:
    '''
    filepath - путь до .json файла,
    data - текущие мета данные.
    Функция выгружает текущие мета данные из программы и записывает их
    в файл для мета данных
    '''
    saved_metadata = js.dumps(data)
    with open(filepath, 'w', encoding='utf-8') as metadata_json:
        metadata_json.write(saved_metadata)
    return


# Функция загрузки данных таблицы из .json файла таблицы
@handle_db_errors
def load_table_data(table_name: str) -> dict:
    '''
    table_name - имя таблицы.
    Функция принимает на вход имя таблицы, и если такая таблица существует,
    то загружает данные таблицы в программу.
    '''
    clean_table_name = table_name.strip().lower()
    with open(TABLE_PATH / (clean_table_name + '.json'), encoding='utf-8') as tabledata_json: # noqa: E501
        loaded_tabledata = js.load(tabledata_json)
    return loaded_tabledata
    

# Функция сохранения данных таблицы в .json файл
@handle_db_errors
def save_table_data(table_name: str, data: dict) -> None:
    '''
    table_name - имя таблицы,
    data - загружаемые данные таблицы.
    Функция принимаем имя таблицы и загружаемые данные, и если таблица
    существует (существует ее файл), то загружает в него актуальные данные.
    '''
    clean_table_name = table_name.strip().lower()
    
    saved_tabledata = js.dumps(data)
    with open(TABLE_PATH / (clean_table_name + '.json'), 'w', encoding='utf-8') as tabledata_json: # noqa: E501
        tabledata_json.write(saved_tabledata)
    return

# Функция отображения помощи
def print_help() -> None:
    '''
    Идет по константе с командами и описанием и последовательно выводит
    '''
    for command in COMMANDS.keys():
        print(f'<command> {command} - {COMMANDS[command]}')
    
    return
    

@handle_db_errors
# Функция получения/записи кэша
def create_cacher():
    cache = {}

    def cache_result(key, value_func, mode, *args, **kwargs):
        if mode in ('insert', 'update', 'delete', 'drop'):
            for key_cache in list(cache.keys()):
                if key_cache.split('_')[0] == key.split('_')[0]:
                    del cache[key_cache]
            return
        else:
            if key in cache:
                print('Получено значение из кэша!')
                return cache[key]
            else:
                result = value_func(*args, **kwargs)
                cache[key] = result
                print('Запрос кэширован.')
                return result

    return cache_result
    
    
