while True:
    try:
        a = input('calc: ')
        resul = eval(a)
        print(f'Resul: {resul}')
    except:
        print('Erro, reiniciando...')
        continue