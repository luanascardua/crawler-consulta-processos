from bs4 import BeautifulSoup
import json


def split_process(process_number: str):
    '''number = process_number.rsplit('.', 1)
    process_number = number[0].rsplit('.', 2)[0]
    process_origin = number[1]'''
    number = process_number.split('.')
    cnj = f'{number[2]}{number[3]}'

    return cnj


def format(text: str):
    partes_processo = text.split('Advogado')
    nome_parte = partes_processo[0]
    advogado = partes_processo[1].strip(':')

    return nome_parte, advogado


def format_html_string(html_string: str):
    soup = BeautifulSoup(html_string, 'html.parser')
    text_string = soup.get_text(strip=True)

    return text_string


def convert_to_float(string: str):
    string = string.replace('.', '').replace(',', '.').replace('R$', '').strip()
    number = float(string)
    return number


def read_json():
    with open('processos.json') as f:
        json_data = json.load(f)

    return json_data
