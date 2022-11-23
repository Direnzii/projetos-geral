import requests
import random

class assistir_filme():
    token = "7d58db8a79eb8e9309fdff18395faabf"
    dict_genero = {"terror":27, "acao":28, "comedia":35, "drama":18, "ficcao_cientifica":878,
               "fantasia":14, "familia":10751, "aventura":12, "misterio":9648, "suspense":53,
               "crime":80, "cinema/tv":10770, "romance":10749}

    def numero_aleatorio(self):
        numero_aleatorio = random.randrange(1, 501)
        return numero_aleatorio

    def chunks(self, lista):
        for i in range(0, len(lista), 4):
            yield lista[i:i + 4]

    def lista_aleatoria(self, lista):
        lista = list(self.chunks(lista))
        count_list = len(lista)
        numero = random.randrange(0, count_list +1)
        list_aleatoria = lista[numero]
        return list_aleatoria

    def requisicao(self, url):
        requisicao = requests.get(url)
        json = requisicao.json()
        return json

    def listar_filmes_rate_genero(self, rate, genero):
        while True:
            lista_filmes = []
            genero_id = self.dict_genero[f"{genero}"]
            url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                        f"api_key={self.token}&" \
                        "include_adult=false&" \
                        "include_video=false&" \
                        f"page={self.numero_aleatorio()}&" \
                        f"vote_average.gte={rate}&" \
                        f"with_genres={genero_id}"
            filmes = self.requisicao(url_geral)
            filmes = filmes['results']
            if not filmes:
                continue
            else:
                for movie in filmes:
                    id = movie['id']
                    lista_filmes.append(id)
                return lista_filmes

    def listar_filmes_genero(self, genero):
        while True:
            lista_filmes = []
            genero_id=self.dict_genero[f"{genero}"]
            url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                        f"api_key={self.token}&" \
                        "include_adult=false&" \
                        "include_video=false&" \
                        f"page={self.numero_aleatorio()}&" \
                        f"with_genres={genero_id}"
            filmes = self.requisicao(url_geral)
            filmes = filmes['results']
            if not filmes:
                continue
            else:
                for movie in filmes:
                    id = movie['id']
                    lista_filmes.append(id)
                return lista_filmes

    def listar_filmes_rate(self, rate):
        while True:
            lista_filmes = []
            url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                        f"api_key={self.token}&" \
                        "include_adult=false&" \
                        "include_video=false&" \
                        f"page={self.numero_aleatorio()}&" \
                        f"vote_average.gte={rate}"
            filmes = self.requisicao(url_geral)
            filmes = filmes['results']
            if not filmes:
                continue
            else:
                for movie in filmes:
                    id = movie['id']
                    lista_filmes.append(id)
                return lista_filmes

    def listar_filmes(self):
        while True:
            lista_filmes = []
            url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                        f"api_key={self.token}&" \
                        "include_adult=false&" \
                        "include_video=false&" \
                        f"page={self.numero_aleatorio()}"
            filmes = self.requisicao(url_geral)
            filmes = filmes['results']
            if not filmes:
                continue
            else:
                for movie in filmes:
                    id = movie['id']
                    lista_filmes.append(id)
                return lista_filmes

    def rodar(self, lista_filmes):
        i = True
        while i:
            try:
                count_movies = len(lista_filmes)
                random_id = random.randrange(0, count_movies + 1)
                id_filme = lista_filmes[random_id]

                url_filme = f"https://api.themoviedb.org/3/movie/{id_filme}?" \
                            "api_key=7d58db8a79eb8e9309fdff18395faabf"
                filme = self.requisicao(url_filme)

                nome = filme['original_title']
                sinopse = filme['overview']
                if not sinopse:
                    sinopse = "Não encontrado"
                votos = filme['vote_average']
                print("*** SEU FILME É ***")
                print('Nome: ', nome, '\nSinopse: ', sinopse, '\nMédia de votos: ', votos)
                i = False
            except:
                print("Algo deu errado, finalizando !")