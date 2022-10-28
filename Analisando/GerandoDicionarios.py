def notas(num, sit=False):
    dictnt = dict()
    dictnt['total'] = len(num)
    dictnt['maior'] = max(num)
    dictnt['menor'] = min(num)
    dictnt['média'] = sum(num) / len(num)
    print(type(num))
    if sit:
        if dictnt['média'] >= 9:
            dictnt['sit'] = 'ÓTIMA'
        elif dictnt['média'] >= 7:
            dictnt['sit'] = 'BOA'
        elif dictnt['média'] >= 5:
            dictnt['sit'] = 'REGULAR'
        else:
            dictnt['sit'] = 'RUIM'
    return dictnt
nota = list()
cont = 1
print('Digite as notas dos alunos!')
while True:
    resp = float(input(f'Digite a nota do {cont}º aluno: '))
    nota.append(resp)
    d = input('Deseja continuar [S/N]? ')
    cont+=1
    if d in 'nN':
        break
print(notas(nota, sit=True))