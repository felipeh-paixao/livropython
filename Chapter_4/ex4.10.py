#Fatias

cubes = [value ** 3 for value in range(1, 11)]

print('Os três último ítens da lista são: ')
for cube in cubes[-3:]:
    print(cube)

print('\nOs três primeiros ítens da lista são: ')

for cube in cubes[:3]:
    print(cube)

print('\nAqui está três ítens do meio da lista: ')

for cube in cubes[5:8]:
    print(cube)