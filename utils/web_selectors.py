from selenium.webdriver.common.by import By


class Esaj1Grau:

    def __init__(self, driver):

        self.input_processo = By.ID, "nuProcessoAntigoFormatado"
        self.btn_consultar = By.ID, "botaoConsultarProcessos"
        self.radio_outros = By.ID, "radioNumeroAntigo"

        self.mensagem_retorno = By.ID, "spwTabelaMensagem"

        self.field_classe_processo = By.ID, "classeProcesso"
        self.field_assunto_processo = By.ID, "assuntoProcesso"
        self.field_foro_processo = By.ID, 'foroProcesso'
        self.field_vara_processo = By.ID, 'varaProcesso'
        self.field_juiz_processo = By.ID, 'juizProcesso'
        self.field_area_processo = "areaProcesso"
        self.field_valor_acao = "valorAcaoProcesso"

        self.table_partes_tipo = By.XPATH, '//table[@id="tablePartesPrincipais"]//td[@class="label"]'
        self.table_partes_nome = By.XPATH, '//table[@id="tablePartesPrincipais"]//td[@class="nomeParteEAdvogado"]'

        self.table_movimentacoes_data = By.XPATH, '//tbody[@id="tabelaTodasMovimentacoes"]//td[@class="dataMovimentacao"]'
        self.table_movimentacoes_descricao = By.XPATH, '//tbody[@id="tabelaTodasMovimentacoes"]//td[@class="descricaoMovimentacao"]'


class Esaj2Grau:

    def __init__(self, driver):

        self.input_processo = By.ID, "nuProcessoAntigoFormatado"
        self.btn_consultar = By.ID, "pbConsultar"
        self.radio_outros = By.ID, "radioNumeroAntigo"

        self.mensagem_retorno = By.ID, "spwTabelaMensagem"

        self.radio_selecionar_processo = By.ID, 'processoSelecionado'
        self.btn_selecionar = By.ID, "botaoEnviarIncidente"

        self.field_classe_processo = By.ID, "classeProcesso"
        self.field_assunto_processo = By.ID, "assuntoProcesso"
        self.field_foro_processo = By.XPATH, '/html/body/div[2]/table[3]/tbody/tr/td[2]'
        self.field_vara_processo = By.XPATH, '/html/body/div[2]/table[3]/tbody/tr/td[3]'
        self.field_juiz_processo = By.XPATH, '/html/body/div[2]/table[3]/tbody/tr/td[4]'
        self.field_area_processo = "areaProcesso"
        self.field_valor_acao = "valorAcaoProcesso"

        self.table_partes_tipo = By.XPATH, '//table[@id="tablePartesPrincipais"]//td[@class="label"]'
        self.table_partes_nome = By.XPATH, '//table[@id="tablePartesPrincipais"]//td[@class="nomeParteEAdvogado"]'

        self.table_movimentacoes_data = By.XPATH, '//tbody[@id="tabelaTodasMovimentacoes"]//td[@class="dataMovimentacaoProcesso"]'
        self.table_movimentacoes_descricao = By.XPATH, '//tbody[@id="tabelaTodasMovimentacoes"]//td[@class="descricaoMovimentacaoProcesso"]'
