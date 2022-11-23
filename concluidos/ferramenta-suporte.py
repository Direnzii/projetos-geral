from playwright.sync_api import sync_playwright
import time

class FerramentaSuporte:

    def abrir_arquivo(self, arquivo):
        with open(arquivo) as file:
            arquivo = file.read().replace(',', ' ').split() #tratamento do arquivo, se tem virgula, se tem espaço, se esta separado por tab
            time.sleep(1)
        return arquivo

    def autenticar(self, ambiente):
        time.sleep(0.5)
        usuario = 'jamil.almeida@cotefacil.com'
        senha = '1GcwOQP8'
        ambiente.fill('xpath=//*[@id="frm:email"]', usuario)
        ambiente.fill('xpath=//*[@id="frm:senha"]', senha)
        ambiente.locator('xpath=/html/body/div/article/div/div/form/div/div/button/span[1]').click()
        time.sleep(0.2)

    def reenviar_cotacoes(self, ambiente, arquivo, cnpj_fornecedor):
        self.autenticar(ambiente)
        lista = self.abrir_arquivo(arquivo)  # retorna lista com cotações
        time.sleep(0.5)
        ambiente.locator(
            'xpath=/html/body/div/article/div/div/form[6]/div/div/div/div[1]/div[2]/span/span[1]/span[1]/input').click()  # Clica na chave para reenviar cotação
        time.sleep(1)
        ambiente.fill('.MuiInputBase-input', '1123')  # Coloca a senha no input
        ambiente.locator(
            'xpath=/html/body/div[2]/form/button[2]/span[1]').click()  # Clica no "Liberar acesso"
        time.sleep(0.5)
        for cotacoes in lista:
            ambiente.fill('xpath=//*[@id="idCotacao"]', cotacoes)
            ambiente.fill('xpath=//*[@id="cnpj"]', cnpj_fornecedor)
            ambiente.locator(
                'xpath=/html/body/div/article/div/div/form[6]/div/div/div/div[2]/button/span[1]').click() #Reenviar cotação
            time.sleep(0.5)
            #ambiente.locator('xpath=/html/body/div[2]/div[3]/button[1]').click() #Clica no NÃO - PARA TESTES
            ambiente.locator('xpath=/html/body/div[2]/div[3]/button[2]').click() #Clica no reenviar
            time.sleep(0.5)
            ambiente.locator('xpath=/html/body/div[2]/div[3]/button[3]').click()  # Clica no ok
            print(f"Reenviando cotação {cotacoes}")
        print("Fim do processo, fechando.")

    def cancelar_cotacao(self, ambiente, arquivo):
        self.autenticar(ambiente)
        lista = self.abrir_arquivo(arquivo) #retorna lista com cotações
        contador = 0
        for cotacoes in lista:
            time.sleep(0.2)
            ambiente.fill('xpath=//*[@id="idCotacao"]', cotacoes)
            time.sleep(0.2)
            ambiente.locator('xpath=/html/body/div/article/div/div/form[6]/div/div/div/div[2]/button/span[1]').click() #Cencelar cotação
            time.sleep(0.5)
            #ambiente.locator('xpath=/html/body/div[2]/div[3]/button[1]').click() #Clica no NÃO - PARA TESTES
            ambiente.locator('xpath=/html/body/div[2]/div[3]/button[2]').click() #Clica no cancelar
            time.sleep(0.2)
            ambiente.locator('xpath=/html/body/div[2]/div[3]/button[3]').click()  # Clica no ok
            print(f"Cancelando cotação {cotacoes}")
            contador += 1
        if contador ==1:
            print(f"Fim do processo, foi cancelada apenas 1 cotação, fechando.")
            return
        print(f"Fim do processo, foram canceladas {contador} cotações, fechando.")

    def apagar_e_chamar_retorno_faturamento(self, ambiente, arquivo):
        self.autenticar(ambiente)
        lista = self.abrir_arquivo(arquivo)
        contador = 0
        for pedido in lista:
            time.sleep(0.2)
            ambiente.fill('xpath=//*[@id="form-apagarRetorno-idPedido"]', pedido)
            time.sleep(0.2)
            ambiente.fill('xpath=//*[@id="value"]', pedido)
            time.sleep(0.2)
            ambiente.locator('xpath=/html/body/div/article/div/div/form[2]/div/div/div/div/button').click()
            time.sleep(0.2)
            ambiente.locator('xpath=/html/body/div[2]/div[3]/button[2]').click()
            time.sleep(0.2)
            ambiente.locator('xpath=/html/body/div[2]/div[3]/button[3]').click()
            time.sleep(0.2)
            ambiente.locator('xpath=/html/body/div/article/div/div/form[3]/div/div/div/div[2]/button').click()
            time.sleep(0.2)
            ambiente.locator('xpath=/html/body/div[2]/div[3]/button[2]').click()
            time.sleep(0.2)
            ambiente.locator('xpath=/html/body/div[2]/div[3]/button[3]').click()
            time.sleep(0.2)
            print(f'Retorno chamado para o pedido: {pedido}')
            contador += 1
        print(f'Foi apagado e chamado o retorno de {contador} pedidos')

    def rodar(self, navegador, ambiente):
        ambiente = ambiente.lower()
        if ambiente == 'demo':
            demo = navegador.new_page()
            demo.goto('https://develop.d1tek8o3h211fm.amplifyapp.com/')
            argumento1 = int(input('Voce quer:\nREENVIAR COTAÇÕES - 1\nCANCELAR COTAÇÕES - 2\nAPAGAR RETORNO E CHAMAR - 3\nCHAMAR RETORNO - 4\nInsira aqui: '))
            try:
                if argumento1 == 1:
                    arquivo = input('Insira o arquivo das cotações ou caminho do arquivo: ')
                    cnpj_fornecedor = input('Insira o CNPJ do fornecedor para reenviar as cotações: ')
                    print("Autenticando na ferramenta, para realizar os reenvios.")
                    self.reenviar_cotacoes(demo, arquivo, cnpj_fornecedor)
                    return
                if argumento1 == 2:
                    arquivo = input('Insira o arquivo das cotações ou caminho do arquivo: ')
                    print("Autenticando na ferramenta, para realizar os cancelamentos.")
                    self.cancelar_cotacao(demo, arquivo)
                    return
                if argumento1 == 3:
                    arquivo = input('Insira o arquivo dos pedidos ou caminho do arquivo: ')
                    print("Autenticando na ferramenta, para realizar os processos.")
                    self.apagar_e_chamar_retorno_faturamento(demo, arquivo)
                if argumento1 == 4:
                    arquivo = input('Insira o arquivo dos pedidos ou caminho do arquivo: ')
                    print("Autenticando na ferramenta, para realizar os processos.")
                    self.chamar_retorno(demo, arquivo)
                else:
                    print('\n1 ou 2, não tem outra opção !!')
                    return
            except:
                print('\nOcorreu um erro, verifique o arquivo ou as informações passadas !!')
                return

        if ambiente == 'oficial':
            demo = navegador.new_page()
            demo.goto('https://master.d1tek8o3h211fm.amplifyapp.com/')
            argumento1 = int(input('Voce quer:\nREENVIAR COTAÇÕES - 1\nCANCELAR COTAÇÕES - 2\nAPAGAR RETORNO E CHAMAR - 3\nCHAMAR RETORNO - 4\nInsira aqui: '))
            try:
                if argumento1 == 1:
                    arquivo = input('Insira o arquivo das cotações ou caminho do arquivo: ')
                    cnpj_fornecedor = input('Insira o CNPJ do fornecedor para reenviar as cotações: ')
                    self.reenviar_cotacoes(demo, arquivo, cnpj_fornecedor)
                    return
                if argumento1 == 2:
                    arquivo = input('Insira o arquivo das cotações ou caminho do arquivo: ')
                    self.cancelar_cotacao(demo, arquivo)
                    return
                if argumento1 == 3:
                    arquivo = input('Insira o arquivo dos pedidos ou caminho do arquivo: ')
                    print("Autenticando na ferramenta, para realizar os processos.")
                    self.apagar_e_chamar_retorno_faturamento(demo, arquivo)
                if argumento1 == 4:
                    arquivo = input('Insira o arquivo dos pedidos ou caminho do arquivo: ')
                    print("Autenticando na ferramenta, para realizar os processos.")
                    self.chamar_retorno(demo, arquivo)
                else:
                    print('\n1 ou 2, não tem outra opção !!')
                    return
            except:
                print('\nOcorreu um erro, verifique o arquivo ou as informações passadas !!')
                return
        else:
            print('\nDigite ou oficial ou demo, nada mais que isso !!')
            return

    def chamar_retorno(self, ambiente, arquivo):
        self.autenticar(ambiente)
        lista = self.abrir_arquivo(arquivo)
        contador = 0
        for pedido in lista:
            time.sleep(0.2)
            ambiente.fill('xpath=//*[@id="value"]', pedido)
            time.sleep(0.2)
            ambiente.locator('xpath=/html/body/div/article/div/div/form[3]/div/div/div/div[2]/button').click()
            time.sleep(0.2)
            ambiente.locator('xpath=/html/body/div[2]/div[3]/button[2]').click()
            time.sleep(0.2)
            ambiente.locator('xpath=/html/body/div[2]/div[3]/button[3]').click()
            time.sleep(0.2)
            print(f'Retorno chamado para o pedido: {pedido}')
            contador += 1
        print(f'Foi chamado o retorno de {contador} pedidos')


def main():
    ferramenta = FerramentaSuporte()

    with sync_playwright() as p:
        ##### VARIAVEIS DO PLAYWRIGHT #####
        navegador = p.firefox.launch(
            headless=False)  # por padrão esse modo é headless = True (não mostra o navegador abrindo)
        ###################################
        ambiente = str(input('Insira o ambiente que quer realizar o processo, demo ou oficial: '))
        ferramenta.rodar(navegador, ambiente)
if __name__ == "__main__":
    main()