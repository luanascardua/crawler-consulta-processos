
from utils.functions import read_json, split_process
from utils.web_selectors import Esaj1Grau, Esaj2Grau
from crawler.webdriver import driver, start_urls
from crawler.scrape import (
    search_process,
    get_data_header,
    get_partes_processo,
    get_movimentacoes
)


if __name__ == '__main__':
    json_data = read_json()

    for processo in json_data['processos']:
        print(processo)
        esaj = Esaj1Grau(driver)
        cnj = split_process(processo['numero'])
        if cnj == '802':
            urls = start_urls['Alagoas']
        elif cnj == '806':
            urls = start_urls['Ceará']

        for url in urls:
            driver.get(url)
            if search_process(processo['numero'], esaj):
                continue
            get_data_header(esaj)
            '''get_partes_processo(esaj)
            get_movimentacoes(esaj)
            input('acabou')'''

            esaj = Esaj2Grau(driver)

    driver.quit()
