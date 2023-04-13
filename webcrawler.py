
from utils.functions import split_process, create_dict, write_json, dict_dados_coletados
from utils.web_selectors import Esaj1Grau, Esaj2Grau
from crawler.webdriver import start_urls, driver
from crawler.scrape import (
    search_process,
    get_data_header,
    get_partes_processo,
    get_movimentacoes
)


def start_crawler(process_number):
    
    list_dict = []
    esaj = Esaj1Grau(driver)
    instancia = 1

    cnj = split_process(process_number)
    if cnj == '802': UF = 'Alagoas'
    elif cnj == '806': UF = 'Ceará'
        
    urls = start_urls[UF]

    for url in urls:
        driver.get(url)
        if search_process(process_number, esaj):
            list_dict.append({f"{instancia}Grau":'processo não encontrado'})
            esaj = Esaj2Grau(driver)
            instancia = 2
            continue
        dados_principais = get_data_header(esaj)
        partes_processo = get_partes_processo(esaj)
        movimentacoes = get_movimentacoes(esaj)
        list_dict.append(dict_dados_coletados(instancia, dados_principais, partes_processo, movimentacoes))
        esaj = Esaj2Grau(driver)
        instancia = 2

    json_content = create_dict(process_number, UF, list_dict)
    # write_json(json_content)
    
    driver.quit()
    return json_content
