#exercises
my_dict = {
    'word': 'Econometrics',
    "sentence": 'If the implementation is easy to explain, it may be a good idea.',
    'big_list': ["python", 3, "anaconda", 3.6, "jupyter", 10, "lessons", "many", 99],
    "empty_list": []
}


# exercise1
if not my_dict['word'].isupper():
    my_dict['word'] = my_dict['word'].upper() 
    
print (my_dict['word'])


# exercise2
my_dict['word'] ="Applied_"+ my_dict['word']
print (my_dict['word'])


#exercise3
my_dict['sentence'] = my_dict['sentence'].replace("implementation", "no implementation")
print (my_dict['sentence'])


#exercise4
for i in my_dict['big_list']:
    if type(i) == str:
        print(i[0])



#exercise5
sum = 0
for i in my_dict['big_list']:
    if type(i) == int:
        sum+= i
sum1 = 0
my_dict['big_list'].remove(my_dict['big_list'][-1])
my_dict['big_list'].append(87)
for item in my_dict['big_list']:
    if type(item) == int:
        sum1+= item
print(sum1)




#execise6
my_dict['big_list'][7] = "Mika"
print(my_dict)




# execise7
for i in range(10,14):
    my_dict["empty_list"].append(i)
    
print(my_dict)

count_odd = 0
count_prime = 0

for i in my_dict["empty_list"]:
    if i % 2 == 0:
        count_prime += 1
    else:
        count_odd += 1
print(count_odd)
print(count_prime)

