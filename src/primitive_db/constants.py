# src/primitive_db/constants.py
from pathlib import Path

COMMANDS = {
  'create_table <имя_таблицы> <столбец1:тип> <столбец2:тип> ..': 'создать таблицу.',
  'drop_table <имя_таблицы>': 'удалить таблицу.',
  'list_tables': 'показать список всех таблиц.',
  'insert into <имя_таблицы> values (<значение1>, <значение2>, ...)': 'создать запись.',
  'select from <имя_таблицы> where <столбец> = <значение>': 'прочитать записи по условию.', # noqa: E501
  'select from <имя_таблицы>': 'прочитать все записи.',
  'update <имя_таблицы> set <столбец1> = <новое_значение1> where <столбец_условия> = <значение_условия>': 'обновить запись.', # noqa: E501
  'delete from <имя_таблицы> where <столбец> = <значение>': 'удалить запись.',
  'info <имя_таблицы>': 'вывести информацию о таблице.',
  'exit': 'выйти из программы.',
  'help': 'справочная информация.'
}

META_FILE = 'db_meta.json'
META_FILEPATH = Path(__file__).parent / META_FILE
TABLE_PATH = Path(__file__).parent / 'data'

CURRENT_TYPES  = ['str', 'int', 'bool']


