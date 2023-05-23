1. 
dog={}
print(dog)

dog['name'] = 'Rocky'
print(dog)
dog['color'] = 'white'
print(dog)
dog['breed'] = 'color'
print(dog)
dog['legs'] = 'color'
print(dog)
dog['age'] = '1'


student= {'first_name':'Sam', 'last_name':'Hamiltion', 'gender': 'male',
           'age': 20, 'marital status': 'single', 
           'skills': ['teaching', 'baking', 'script writting'],
          'country': 'sweeden', 'city': 'stockholm', 'address': 'cape street' }
print(len(student))
print(student['skills'])
print(type('skills'))
student['skills']. append('painting')
print(student)

for key in student:
    print(key,student[key])
