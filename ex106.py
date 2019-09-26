def pyhelp():
    while True:
        print('\033[1;30;45m~'*25)
        print(' Sistema de Ajuda Pyhelp')
        print('~'*25)
        h = (str(input('\033[mFunção ou biblioteca: ')))
        h2 = f' Acessando o manual ou comando {h}'
        print('\033[1;30;46m~'*len(h2))
        print(f'{h2}')
        print('~'*len(h2))
        if h == 'fim':
            break
        print('\033[7;30m')
        help(h)
    print('\033[1;30;41m~'*30)
    print(' Fim do programa volte sempre')
    print('~'*30)

pyhelp()