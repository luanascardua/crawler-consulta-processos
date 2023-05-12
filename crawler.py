from structure.utils.functions import split_process, create_dict, write_json, dict_dados_coletados
from structure.crawler.driver import start_urls, get_chrome_driver
from structure.utils.web_selectors import Esaj1Grau, Esaj2Grau
from structure.crawler.scrape import (
    search_process,
    get_data_header,
    get_partes_processo,
    get_movimentacoes
)


def start_crawler(process_number):
    driver = get_chrome_driver()
    list_dict = []
    instancia = 1
    UF = None

    esaj = Esaj1Grau()
   
    cnj = split_process(process_number)
    if cnj == '802': UF = 'Alagoas'
    elif cnj == '806': UF = 'Ceará'
    else: print('processo não corresponde ao TJAL/TJCE')

    if UF is not None:
        urls = start_urls[UF]

        for url in urls:
            driver.get(url)
            if search_process(driver, process_number, esaj):
                list_dict.append({f'{instancia}º Grau':'processo não encontrado'})
                esaj = Esaj2Grau()
                instancia = 2
                continue
            dados_principais = get_data_header(driver, esaj)
            partes_processo = get_partes_processo(driver, esaj)
            movimentacoes = get_movimentacoes(driver, esaj)
            list_dict.append(dict_dados_coletados(instancia, dados_principais, partes_processo, movimentacoes))
            esaj = Esaj2Grau()
            instancia = 2

        json_content = create_dict(process_number, UF, list_dict)
        write_json(json_content)

        return json_content
