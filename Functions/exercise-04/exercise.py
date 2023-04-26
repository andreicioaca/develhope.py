def hello(firstname = 'John', lastname = 'Doe'):
    print(f'Hello, {firstname} {lastname}!')

family=['Tristram Mcbride',
        'Baldwin Preston',
        'Wally Collins'
]

hello()

for people in family:
    firstname, lastname = people.split()
    hello(firstname, lastname)