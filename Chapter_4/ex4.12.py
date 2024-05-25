#Foods.py

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My')
for my in my_foods:
    print(my)

print('\nFriend')
for friend in friend_foods:
    print(friend)

