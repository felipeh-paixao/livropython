#Minhas pizzas, suas pizzas
my_pizzas = ['Frango com catupiry', 'Calabresa', 'Nordestina']
friend_pizzas = my_pizzas[:]
my_pizzas.append('Mussarela')
friend_pizzas.append('Chocolate')

print('Minhas pizzas favoritas são: ')
for my in my_pizzas:
    print(my)

print('\nAs pizzas favoritas do meu amigo são: ')
for friend in friend_pizzas:
    print(friend)