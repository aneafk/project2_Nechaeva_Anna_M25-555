# src/primitive_db/parser.py
import ast

from .constants import CURRENT_TYPES
from .decorators import handle_db_errors


# Функция парсера для парсинга set и where
@handle_db_errors
def parser_clause(clause: str) -> dict:
    '''
    clause - условие where или set
    '''
    if len(clause) != 4:
        print('Неправильный формат условия where или set.')
        return {}
  
    if clause[0] == 'set' and clause[2] == '=':
        value_to_return = ast.literal_eval(clause[3])
        if str(type(value_to_return).__name__) in CURRENT_TYPES:
            return {clause[1]: value_to_return}
    
        print(f'Тип данных {type(value_to_return).__name__} не поддерживается. Попробуйте снова.') # noqa: E501
        return {}

    if clause[0] == 'where' and clause[2] == '=':
        value_to_return = ast.literal_eval(clause[3])
        if str(type(value_to_return).__name__) in CURRENT_TYPES:
            return {clause[1]: value_to_return}
    
        print(f'Тип данных {type(value_to_return).__name__} не поддерживается.')
        return {}
  
    print('Неподдерживаемое ключевое значение.')
    return {}
    
    
