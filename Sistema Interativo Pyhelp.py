from time import sleep

color = {'clear': '\033[m', 'green': '\033[1;42m', 'blue': '\033[1;44m', 'white': '\033[1;30;107m', 'red': '\033[1;41m'}


def tit(msg, cor='clear'):
    t = len(msg) + 4
    print(f'{color[cor]}', end='')
    print('~' * t)
    print(f'{msg:^{t}}')
    print('~' * t)
    print(f'{color["clear"]}', end='')


def pyhelp(comand, cor='clear'):
    tit(f'Acessando o manual do comando \'{comand}\'', cor='blue')
    sleep(1)
    print(f'{color[cor]}')
    help(comand)
    print(f'{color["clear"]}', end='')
    sleep(2)


while True:
    tit('SISTEMA DE AJUDA PyHELP', cor='green')
    func = input('Função ou Biblioteca > ')
    if func.upper() in 'FIM':
        tit('ATÉ LOGO!', 'red')
        break
    pyhelp(func, cor='white')
