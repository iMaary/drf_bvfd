import re
from validate_docbr import CPF

def cpf_is_valid(cpf_num):
    cpf = CPF()
    return cpf.validate(cpf_num)

def name_is_valid(name):
    return name.isalpha()

def rg_is_valid(rg):
    return len(rg) == 9

def cellphone_is_valid(cellphone):
    """Verifi if cellphone is valid (11) 91234-1234"""
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model, cellphone)

    return response
