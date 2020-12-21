# 21/12/2020 dictionary
#Dictionary : sözlükler de aynen set gibi sırasız veri tutar.
# Günlük hayattaki sözlükler gibi düşünebiliriz key value şeklinde değerler tutar.

# empty dict
my_dict = {}

# dictionary with integer keys
my_dict = {1:'apple',2:'bottle'}
print(my_dict)

# dictionary with mixed keys
my_dict = {'name':'John',1:[1,2,3,4]}
print(my_dict)

# using dict
my_dict = dict({'name':'John',1:[1,2,3,4]})
print(my_dict)

my_dict = dict([(1,'apple'),(2,'ball')])
print(my_dict)
