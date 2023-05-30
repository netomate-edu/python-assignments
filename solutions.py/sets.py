1. 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

other_it_companies={'Alibaba', 'Samsung electonics'}
it_companies.update(other_it_companies)
print(it_companies)

it_companies.remove('Microsoft')
print(it_companies)