list= []
Numbers= [1, 2, 3, 4, 5]
print(len(Numbers))
first_item= Numbers[0]
print(first_item)
middle_item= Numbers[2]
print(middle_item)
last_item= Numbers[4]
print(last_item)


mixed_data_types = ['Harry', 20, 1.74, 'single', 'cape street']
print(mixed_data_types)


it_companies= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
first_company=[0]
print(first_company)
middle_company=[3]
print(middle_company)
last_company=[6]
print(last_company)

it_companies[0] = 'samsung electronics'
print(it_companies)

it_companies.append('facebook')
print(it_companies)
it_companies.insert(2, 'Alibaba')
print(it_companies)
it_companies[1] = 'GOOGLE'
print(it_companies)
['samsung electronics', 'GOOGLE', 'Alibaba', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'facebook']
it_companies= ['samsung electronics', 'GOOGLE', 'Alibaba', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'facebook']
it_company=['#;&nbsp; ']
it_companies . extend(it_company)
print('it_companies and it_company:', it_companies)

does_exist= 'Alibaba' in it_companies
print(does_exist)

it_companies= ['samsung electronics', 'GOOGLE', 'Alibaba', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'facebook']
it_companies.sort()
print(it_companies)

it_companies.sort(reverse=true)
print(it_companies)

it_companies= ['samsung electronics', 'GOOGLE', 'Alibaba', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'facebook']
it_companies.remove('samsung electronics')
print(it_companies)

it_companies. remove('Apple')
print(it_companies)

it_companies. remove('facebook')
print(it_companies)

it_companies= ['samsung electronics', 'GOOGLE', 'Alibaba', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'facebook']
it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

full_stack=['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5, 'python')
 

















