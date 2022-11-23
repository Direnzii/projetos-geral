from randmovie import assistir_filme
import time

def main():
    input("Pressione enter para iniciar ...")
    while True:
        aleatorio = assistir_filme()
        print("***DIGITE UMA OPÇÃO***\n(1) - Aleatório\n(2) - Por rate\n(3) - Por gênero\n(4) - Por rate e gênero")
        try:
            opcao = int(input('Insira aqui: '))
            time.sleep(1)

            if opcao == 1:
                lista_filmes = aleatorio.listar_filmes()
                lista_aleatoria = aleatorio.lista_aleatoria(lista_filmes)
                aleatorio.rodar(lista_aleatoria)
            elif opcao == 2:
                rate = int(input("Insira um rate minimo para a busca, de 1 a 10: "))
                if rate > 10 and rate < 1:
                    print("Rate invalido, fechando !!")
                else:
                    lista_filmes = aleatorio.listar_filmes_rate(rate)
                    lista_aleatoria = aleatorio.lista_aleatoria(lista_filmes)
                    aleatorio.rodar(lista_aleatoria)
            elif opcao == 3:
                print("***Generos disponiveis***")
                print("terror, acao, comedia, drama, ficca_cientifica, fantasia, familia, aventura, misterio, suspense, crime, cinema/tv, romance")
                genero = input("Insira um gênero valido: ")
                genero = genero.lower()
                lista_filmes = aleatorio.listar_filmes_genero(genero)
                lista_aleatoria = aleatorio.lista_aleatoria(lista_filmes)
                aleatorio.rodar(lista_aleatoria)
            elif opcao == 4:
                rate = int(input("Insira um rate minimo para a busca, de 1 a 10: "))
                if rate >= 1 and rate <=10:
                    print("***Generos disponiveis***")
                    print("terror, acao, comedia, drama, ficcao_cientifica, fantasia, familia, aventura, misterio, suspense, crime, cinema/tv, romance")
                    genero = input("Insira um gênero valido: ")
                    genero = genero.lower()
                    lista_filmes = aleatorio.listar_filmes_rate_genero(rate, genero)
                    lista_aleatoria = aleatorio.lista_aleatoria(lista_filmes)
                    aleatorio.rodar(lista_aleatoria)
                    i = False
                else:
                    print("rate inválido, insira um numero de 1 a 10 !!")
            else:
                a = 0/0
                print(a)
        except:
            print("Não existe essa opção !!")
        time.sleep(1)
        input("Pressione enter para uma nova busca ...")

if __name__ == '__main__':
    main()