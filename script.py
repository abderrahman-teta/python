# day Number One in 100day coding challenge (python) :

print('what is your name 😒:')

name = input('> ')

print('how old are you 😑:')

age = input('> ')

print('How tall you are in meters 😒:')

tall = input('> ')

print('what is your weight in kg 😒:')

weight = input('> ')

calo = float(weight) * 2 * 12

water = int(float(weight) * 0.033)

brotin = int(float(weight) * 2 )

perfect_weight = int((float(tall) - 1) * 100)

print('Mr '+name + ' your perfect weight is '+str(perfect_weight)+' kg'+'\n'+'and you are need '+str(water) +' l from water /day')

print('and you need '+str(calo)+' kcal/day ')

print('and  '+str(brotin)+' g/day ')