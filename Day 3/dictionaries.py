my_dictionary = {'c1': 'value1', 'c2': 'value2'}
print(type(my_dictionary))

my_dictionary = {'c1': 'value1', 'c2': 'value2'}
print(my_dictionary)

# fetch the content of key 1
my_dictionary = {'c1': 'value1', 'c2': 'value2'}
print(my_dictionary)
result = my_dictionary['c1']
print(result)

my_dictionary = {'c1': 'value1', 'c2': 'value2'}
print(my_dictionary)
result = my_dictionary['c2']
print(result)

# making a query ask for the last name
customer = {'name': 'John', 'last_name':' Lennon', 'weight': 88, "height": 1.76}
query = (customer['last_name'])
print(query)

# ask for the height
customer = {'name': 'John', 'last_name':' Lennon', 'weight': 88, "height": 1.76}
query = (customer['height'])
print(query)

dic = {1: 55, 2:[10, 20, 30], 3: {'s1': 100., 's2': 200}}
print(dic[2])

dic = {1: 55, 2:[10, 20, 30], 3: {'s1': 100., 's2': 200}}
print(dic[2][1])

dic = {1: 55, 2:[10, 20, 30], 3: {'s1': 100., 's2': 200}}
print(dic[3])

dic = {1: 55, 2:[10, 20, 30], 3: {'s1': 100., 's2': 200}}
print(dic[3]['s2'])

# make e uppercase
dic = {'k1': ['a', 'b', 'c', ], 'k2': ['d', 'e', 'f']}
print(dic['k2'][1].upper())
# it must be an index [e] this way won"t work

# add a new key to an existing list
dic = {1: 'a', 2: 'b'}
print(dic)

dic[3] = 'c'
print(dic)

# make b uppercase
dic = {1: 'a', 2: 'b'}
print(dic)

dic[3] = 'c'
print(dic)

dic[2] = 'B'
print(dic)

# how bring all the keys a list has

print(dic.keys())

# how to see all the values
print(dic.values())

# evertyhing in the dictionary
print(dic.items())

# Practice create a dictionary called my_dic that stores the following information about the person
my_dict ={'name':"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}
