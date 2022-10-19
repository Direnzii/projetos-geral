import requests
import random

token = "7d58db8a79eb8e9309fdff18395faabf"
dict_genero = {"terror":27, "acao":28, "comedia":35, "drama":18, "ficca_cientifica":878,
           "fantasia":14, "familia":10751, "aventura":12, "misterio":9648, "suspense":53,
           "crime":80, "cinema/tv":10770, "romance":10749}

def numero_aleatorio():
    numero_aleatorio = random.randrange(1, 501)
    return numero_aleatorio

def chunks(lista):
    for i in range(0, len(lista), 4):
        yield lista[i:i + 4]

def lista_aleatoria(lista):
    lista = list(chunks(lista))
    count_list = len(lista)
    numero = random.randrange(0, count_list +1)
    list_aleatoria = lista[numero]
    return list_aleatoria

def requisicao(url):
    requisicao = requests.get(url)
    json = requisicao.json()
    return json

def listar_filmes_rate_genero(rate, genero):
    lista_filmes = []
    genero_id = dict_genero[f"{genero}"]
    url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                f"api_key={token}&" \
                "include_adult=false&" \
                "include_video=false&" \
                f"page={numero_aleatorio()}&" \
                f"vote_average.gte={rate}&" \
                f"with_genres={genero_id}"
    filmes = requisicao(url_geral)
    filmes = filmes['results']
    if filmes == []:
        print("Lista de filmes vazia, erro !!")

    for i in filmes:
        id = i['id']
        lista_filmes.append(id)
    return lista_filmes

def listar_filmes_genero(genero):
    lista_filmes = []
    genero_id=dict_genero[f"{genero}"]
    url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                f"api_key={token}&" \
                "include_adult=false&" \
                "include_video=false&" \
                f"page={numero_aleatorio()}&" \
                f"with_genres={genero_id}"
    filmes = requisicao(url_geral)
    filmes = filmes['results']
    if filmes == []:
        print("Lista de filmes vazia, erro !!")

    for i in filmes:
        id = i['id']
        lista_filmes.append(id)
    return lista_filmes

def listar_filmes_rate(rate):
    lista_filmes = []
    url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                f"api_key={token}&" \
                "include_adult=false&" \
                "include_video=false&" \
                f"page={numero_aleatorio()}&" \
                f"vote_average.gte={rate}"
    filmes = requisicao(url_geral)
    filmes = filmes['results']
    if filmes == []:
        print("Lista de filmes vazia, erro !!")

    for i in filmes:
        id = i['id']
        lista_filmes.append(id)
    return lista_filmes

def listar_filmes():
    lista_filmes = []
    url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                f"api_key={token}&" \
                "include_adult=false&" \
                "include_video=false&" \
                f"page={numero_aleatorio()}"
    filmes = requisicao(url_geral)
    filmes = filmes['results']
    if filmes == []:
        print("Lista de filmes vazia, erro !!")

    for i in filmes:
        id = i['id']
        lista_filmes.append(id)
    return lista_filmes

def rodar(lista_filmes):
    try:
        count_movies = len(lista_filmes)
        random_id = random.randrange(0, count_movies + 1)
        id_filme = lista_filmes[random_id]

        url_filme = f"https://api.themoviedb.org/3/movie/{id_filme}?" \
                    "api_key=7d58db8a79eb8e9309fdff18395faabf"
        filme = requisicao(url_filme)

        nome = filme['original_title']
        sinopse = filme['overview']
        votos = filme['vote_average']
        print("*** SEU FILME É ***")
        print('Nome: ', nome, '\nSinopse: ', sinopse, '\nMédia de votos: ', votos)
    except:
        print("Algo deu errado, finalizando !")

print("***DIGITE UMA OPÇÃO***\n(1) - Aleatório\n(2) - Por rate\n(3) - Por gênero\n(4) - Por rate e gênero")

try:
    opcao = int(input('Insira aqui: '))

    if opcao == 1:
        lista_filmes = listar_filmes()
        lista_aleatoria = lista_aleatoria(lista_filmes)
        rodar(lista_filmes)
    if opcao == 2:
        rate = int(input("Insira um rate minimo para a busca, de 1 a 10: "))
        if rate > 10 and rate < 1:
            print("Rate invalido, fechando !!")
        else:
            lista_filmes = listar_filmes_rate(rate)
            lista_aleatoria = lista_aleatoria(lista_filmes)
            rodar(lista_filmes)
    if opcao == 3:
        print("***Generos disponiveis***")
        print("terror, acao, comedia, drama, ficca_cientifica, fantasia, familia, aventura, misterio, suspense, crime, cinema/tv, romance")
        genero = input("Insira um gênero valido: ")
        genero = genero.lower()
        lista_filmes = listar_filmes_genero(genero)
        lista_aleatoria = lista_aleatoria(lista_filmes)
        rodar(lista_filmes)
    if opcao == 4:
        rate = int(input("Insira um rate minimo para a busca, de 1 a 10: "))
        if rate > 10 and rate < 1:
            print("Rate inválido, fechando !!")
        else:
            print("***Generos disponiveis***")
            print("terror, acao, comedia, drama, ficca_cientifica, fantasia, familia, aventura, misterio, suspense, crime, cinema/tv, romance")
            genero = input("Insira um gênero valido: ")
            genero = genero.lower()
            lista_filmes = listar_filmes_rate_genero(rate, genero)
            lista_aleatoria = lista_aleatoria(lista_filmes)
            rodar(lista_filmes)
    if opcao > 4 and opcao < 1:
        print("Não existe essa opção, fechando !!")
except:
    print("Não existe essa opção, fechando !!")