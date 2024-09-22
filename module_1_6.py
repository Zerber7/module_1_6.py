my_dict = {'Иванов И.И.' : 1800, 'Петров П.П.' : 1900, 'Сидоров С.С.' : 2000}
print(my_dict)
print(my_dict['Иванов И.И.'])
my_dict['Антонов А.А.'] = 2100
print(my_dict)
my_dict['Котов К.К.'] = 2200
my_dict['Соколов С.С.'] = 2300
print(my_dict)
del my_dict['Иванов И.И.']
print(my_dict)
my_dict['Иванов И.И.'] = 1800
Z = my_dict.pop('Иванов И.И.')
print(Z)
print(my_dict)

my_set = {10, 'АРШИН', 15, 'САЖЕНЬ', 1, 'ПЯДЬ', 1000, 'УЙМА', 1, 10, 15, 25, 1, 1, 15, 'УЙМА', ('ЛОКОТЬ', 2000)}
print(my_set)
list_ = my_set
print(list_.add(3000))
print(list_.add('ШАГ'))
print(list_.remove(1))
print(list_)