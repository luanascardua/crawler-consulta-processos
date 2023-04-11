
from selenium.common.exceptions import JavascriptException, NoSuchElementException
import time
import json

from utils.functions import format_html_string, convert_to_float, dict_header_data, dict_movimentacoes, format_dict_movimentacoes, dict_partes
from crawler.webdriver import driver


def search_process(n_process, esaj):
    driver.find_element(*esaj.radio_outros).click()
    input_processo = driver.find_element(*esaj.input_processo)
    input_processo.clear(); input_processo.send_keys(n_process)
    driver.find_element(*esaj.btn_consultar).click()
    time.sleep(1)
    try:
        driver.find_element(*esaj.mensagem_retorno)
        return True
    except NoSuchElementException:
        try:
            driver.find_element(*esaj.radio_selecionar_processo).click()
            driver.find_element(*esaj.btn_selecionar).click()
        except(NoSuchElementException, AttributeError):
            pass


def get_data_header(esaj):
    classe = driver.find_element(*esaj.field_classe_processo).text
    assunto = driver.find_element(*esaj.field_assunto_processo).text
    foro = driver.find_element(*esaj.field_foro_processo).text
    vara = driver.find_element(*esaj.field_vara_processo).text
    juiz = driver.find_element(*esaj.field_juiz_processo).text
    try:
        valor = driver.execute_script(
            f"return document.getElementById('{esaj.field_valor_acao}').innerHTML"
        )
        try:
            valor = convert_to_float(valor)
        except ValueError:
            valor = format_html_string(valor)
            valor = convert_to_float(valor)
    except JavascriptException:
        print('Valor da ação não informado')
        valor = None

    dict_header_data(classe, assunto, foro, vara, juiz, valor)


def get_partes_processo(esaj):
    list_dict = []
    for key, value in zip(
        driver.find_elements(*esaj.table_partes_tipo),
        driver.find_elements(*esaj.table_partes_nome)
    ):
        key = key.text.strip()
        list_dict.append(dict_partes(key, value))


def get_movimentacoes(esaj):
    # driver.find_element('aa')
    list_dict = []
    for data, descricao in zip(
        driver.find_elements(*esaj.table_movimentacoes_data),
        driver.find_elements(*esaj.table_movimentacoes_descricao)
    ):
        data = data.get_attribute('innerHTML').strip()
        html_string = descricao.get_attribute('innerHTML')
        descricao = format_html_string(html_string)

        list_dict.append(dict_movimentacoes(data, descricao))
    
    format_dict_movimentacoes(list_dict)
    with open("movimentacoes.json", "w", encoding="utf-8") as json_file:
        json.dump(list_dict, json_file, ensure_ascii=False)