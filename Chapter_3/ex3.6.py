#Mais convidados

convidados = ['Jéssica', 'Mãe', 'Di']

print('Boa noite pessoal')
print(convidados)
print('acabei encontrado uma mesa maior então vamos poder receber mais pessoas na festa')

convidados.insert(0, 'Pai')
convidados.insert(2, 'Janaína')
convidados.append('Fabinho')

for convidado in convidados:    
    print('Seja bem-vindo ' + convidado)