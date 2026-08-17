# Tuple Exerices
tpl = ()
siblings_tpl = ('Tenesh', 'Karuna', 'Pamina', 'Chiran')
siblings = ''.join(siblings_tpl)
print(siblings)
print(len(siblings_tpl))
siblings_tpl.insert(4, "Nanda")
siblings_tpl.insert(5, "Hari")
print(siblings_tpl)
family_members = ('Tenesh', 'Karuna', 'Pamina', 'Chiran', 'Nanda', 'Hari')
family = slice.family_members[0:4]
print(family)

#food stuff
tpl = ('Apple', 'Banana', 'Orange', 'Potato', 'Cabage', 'cow', 'cat')
food_stuff_tp = ''.join(tpl)
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
slice_food_tp = tpl[1:]
print(slice_food_tp)
slice_food_tp1 = tpl[3:-3]
print(slice_food_tp1)
del tpl
print(tpl)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)



