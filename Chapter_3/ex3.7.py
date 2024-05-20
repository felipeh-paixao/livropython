#Mais convidados

convidados = ['Jéssica', 'Mãe', 'Di']

convidados.insert(0, 'Pai')
convidados.insert(2, 'Janaína')
convidados.append('Fabinho')

print('Boa noite pessoal')
print(convidados)
print('acabei de ser informado que a mesa não chegará a tempo e somente duas pessoas estarão na festa')

while(len(convidados) > 2):
    excluido = convidados.pop()
    print('Sinto muito ' + excluido + ' mas na próxima você estará aqui')

for i in range(2):
    print('Parabéns ' + convidados[0] + ' você é muito especial')
    del convidados[0]
print('O que restou da lista inicial: ')
print(convidados)