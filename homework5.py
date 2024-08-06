print('Работа со списками:')
my_list = ['apple', 'avocado', 'orange', 'banana', 'pineapple']
print('List: ' + str(my_list))
print('First element: ' + str(my_list[0]))
print('Last element: ' + str(my_list[-1]))
print('Sublist: ' + str(my_list[2:6]))
my_list[2] = '55'
print('Modified list: ' + str(my_list))
print()
print('Работа со словарями:')
my_dict = {'apple': 'яблоко', 'avocado': 'авокадо', 'orange': 'апельсин', 'banana': 'бана', 'pineapple': 'ананас'} #
print('Dictionary: ' + str(my_dict))
print('Translation: ' + str(my_dict['orange']))
my_dict ['mango'] = 'манго'
my_dict.pop('apple')
print('Modified dictionary: ' + str(my_dict))