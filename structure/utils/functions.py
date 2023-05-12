from bs4 import BeautifulSoup
import json


def split_process(process_number: str):
    number = process_number.split('.')
    cnj = f'{number[2]}{number[3]}'

    return cnj


def format_html_string(html_string: str):
    soup = BeautifulSoup(html_string, 'html.parser')
    text_string = soup.get_text(strip=True)

    return text_string


def convert_to_float(string: str):
    string = string.replace('.', '').replace(',', '.').replace('R$', '').strip()
    number = float(string)
    return number


def dict_header_data(classe, assunto, foro, vara, juiz, area, valor):
    dict_dados_principais = {
        'dados processuais': {
            'classe': classe,
            'assunto': assunto,
            'foro': foro,
            'vara': vara,
            'juiz': juiz,
            'area': area,
            'valor': valor
        }
    }
    
    return dict_dados_principais


def dict_movimentacoes(data, descricao):
    dict = {
            'data': data,
            'descricao': descricao
        }
    
    return dict


def format_partes(string: str):
    lines = [line.strip() for line in string.split('\n')]
    lawyers = []
    name = lines[0]

    for line in lines[1:]:
        parts = [x.strip() for x in line.split(':')]
        lawyers.append(parts[1])

    return name, lawyers


def dict_partes(key, value):
    partes = format_partes(value.text)
    dict = {
        key: {
            'name': partes[0],
            'advogados': partes[1]
        }
    }

    return dict


def format_dict_movimentacoes(original_list):
    new_list = []

    for item in original_list:
        if '\n' in item["descricao"]:
            new_descricao = {}
            for line in item["descricao"].split('\n'):
                key_value = line.split(':')
                if len(key_value) == 2:
                    key = key_value[0].strip()
                    value = key_value[1].strip()
                    new_descricao[key] = value
            item["descricao"] = new_descricao
        new_list.append(item)

    return new_list


def write_json(data):
    with open("content.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False)


def create_dict(process_number, UF, dados_crawler):
    dict = {
        'processo': {
            'numero': process_number,
            'UF': UF
        },
        'dadosProcessuais': dados_crawler
    }

    return dict


def dict_dados_coletados(instancia, dados_principais, partes_processo, movimentacoes):
    dict = {
        f'{instancia}Grau': {
            'dadosPrincipais': dados_principais,
            'partesProcesso': partes_processo,
            'movimentacoes': movimentacoes
        }
    }
    return dict
