import time
import requests
from datetime import datetime
from win10toast import ToastNotifier

toaster = ToastNotifier()

def requisicao(url):
    requisicao = requests.get(url)
    json = requisicao.json()
    return json
url = 'https://copa22.medeiro.tech/matches/current'

antigo_home = 0
antigo_fora = 0
contador = 0
while True:
    try:
        if contador == 1:
            while True:
                json = requisicao(url)
                date2 = json['date']
                date2 = date2[:-1]
                date2 = datetime.fromisoformat(date2)
                homeTeam = json['homeTeam']
                awayTeam = json['awayTeam']
                nome_home = homeTeam['name']
                nome_fora = awayTeam['name']
                novo_gol_home = homeTeam['goals']
                novo_gol_fora = awayTeam['goals']

                if novo_gol_home != antigo_home:
                    saida = f'Da(o) {nome_home}\nPlacar: {nome_home} {novo_gol_home} X {novo_gol_fora} {nome_fora}'
                    toaster.show_toast(title='GOOOOOOOOOOOOOL', msg=saida)
                    contador = 0
                    time.sleep(5)
                if novo_gol_fora != antigo_fora:
                    saida = f'Da(o) {nome_fora}\nPlacar: {nome_fora} {novo_gol_fora} X {novo_gol_home} {nome_home}'
                    toaster.show_toast(title='GOOOOOOOOOOOOOL', msg=saida)
                    contador = 0
                    time.sleep(5)

        if contador == 0:
            json = requisicao(url)
            date2 = json['date']
            date2 = date2[:-1]
            date2 = datetime.fromisoformat(date2)
            homeTeam = json['homeTeam']
            awayTeam = json['awayTeam']
            nome_home = homeTeam['name']
            nome_fora = awayTeam['name']
            antigo_home = homeTeam['goals']
            antigo_fora = awayTeam['goals']
            contador += 1
    except Exception as e:
        continue
