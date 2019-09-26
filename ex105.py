def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dificonario com várias informações sobre a situação da turma.
    """
    dic = {}
    dic['total'] = len(num)
    for c,v in enumerate(num):
        if c == 0:
            maior = menor = v
        if v > maior:
            maior = v
        if v < menor:
            menor = v
    dic['maior'] = maior
    dic['menor'] = menor
    media = sum(num)/len(num)
    dic['média'] = media
    if media > 7:
        situa = 'boa'
    if media < 7:
        situa = 'razoável'
    if media < 5:
        situa = 'ruim'
    if sit:
        dic['situação'] = situa
    return dic


print(notas(6.5, 9.5, 10, 6.5, sit=True))